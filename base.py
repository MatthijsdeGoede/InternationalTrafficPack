import itertools
import os
import shutil
from utils.helper_methods import *


class BaseCreator:
    def __init__(self, type, base_folder, mod_folder):
        self.type = type
        self.base_folder = base_folder
        self.mod_folder = mod_folder
        self.search_folders = [base_folder]
        self.sub_dir = "esm"
        self.country_src_loc = "def\\country"
        self.country_dst_dir = f"{self.mod_folder}def\\country\\"
        self.vehicle_src_loc = "def\\vehicle\\ai"
        self.vehicle_dst_dir = f"{self.mod_folder}def\\vehicle\\ai\\{self.sub_dir}"
        self.material_src_loc = f"material\\ui\\lp\\"
        self.material_dst_dir = f"{self.mod_folder}\\material\\ui\\lp\\"

        self.country_dict = {}
        self.vehicle_country_dict = {}
        self.variant_dict = {}
        self.country_lp_types = {}

    def get_limited_spawn_rates(self, limited_to, rate=1.00):
        return {self.country_dict[country]: rate if limited_to is None or country in limited_to else 0.00 for country in
                self.country_dict}

    def create_traffic_storage_file(self, vehicle_list):
        storage_dir = f"{self.mod_folder}def\\vehicle"
        storage_dst_file = f"{storage_dir}\\traffic_storage_{'trailer_truck' if self.type == 'trailer' else self.type}.esm.sii"
        with open(storage_dst_file, "w") as dst:
            dst.write("SiiNunit\n{\n")
            for vehicle in vehicle_list:
                dst.write(
                    f"@include \"{'trailer' if self.type == 'trailer' else 'ai'}/{self.sub_dir}/{vehicle}.sui\"\n")
            dst.write("}")

    def set_country_dict(self):
        country_src_dir = os.path.join(self.base_folder, self.country_src_loc)
        for filename in os.listdir(country_src_dir):
            f = os.path.join(country_src_dir, filename)
            if os.path.isfile(f):
                country_name = filename.split(".")[0]
                with open(f, encoding="utf8") as opened:
                    for line in opened:
                        if "country_code:" in line:
                            abbreviation = line.split("\"")[1]
                            self.country_dict[country_name] = abbreviation.lower()
                            break

    def set_vehicles_per_country(self, vehicle_list, check_spawn_rates=False, first_variant_only=True, limited_to=None):

        # retrieve the variants that belong to the selected vehicles
        for vehicle in vehicle_list:
            vehicle_src_file = self.find_file(self.vehicle_src_loc, f'{vehicle}.sui')
            with open(vehicle_src_file, "r", encoding="utf-8") as src:
                variant_name = None
                rate = 1.00
                for input_line in src:
                    if "traffic_vehicle" in input_line or "traffic_trailer" in input_line:
                        finding_spawn_rate = True
                        variant_name = prepare_internal_name(input_line)
                    elif "spawn_ratio" in input_line:
                        # assume standard 1.00 spawn rate, if custom spawn rate is specified, use this
                        rate = float(input_line.split(":")[1].strip())
                    elif finding_spawn_rate and "}" in input_line:
                        finding_spawn_rate = False
                        self.variant_dict[variant_name] = vehicle
                        # limit spawning to a given set of countries if provided
                        self.vehicle_country_dict[variant_name] = self.get_limited_spawn_rates(limited_to, rate=rate)
                        rate = 1.00
                        # when working with sub variants, only the top variant should be added to the variant dict
                        if first_variant_only:
                            break

        if check_spawn_rates:
            # check the country traffic definitions for custom spawn rates
            self.adapt_spawn_rates()

    def adapt_spawn_rates(self):
        # check the traffic definitions for custom spawn rates and adapt where needed
        for key in self.country_dict:
            f = self.find_file(self.country_src_loc, key, 'traffic.sii')
            with open(f, encoding="utf8") as opened:
                for line1, line2 in itertools.zip_longest(*[opened] * 2):
                    if line2 is not None and "spawn_ratio: " in line2:
                        spawn_ratio = float(line2.split("spawn_ratio: ")[1].strip())
                        # take the minimum of 1.00 and the specified spawn rate
                        if spawn_ratio < 1.00:
                            vehicle = ".".join(line1.split(".")[1:]).strip()
                            if vehicle in self.vehicle_country_dict:
                                self.vehicle_country_dict[vehicle][self.country_dict[key]] = spawn_ratio

    def create_chassis(self, vehicle, line, country_code):
        # create eu or uk chassis to ensure the steering wheel is always on the right side
        chassis_base = line.split("/")[-1].split(".")[0]
        chassis_path = get_os_path(line.split('\"')[1])
        chassis_src_path = f"{self.base_folder}{chassis_path}"
        rhs_driver = country_code == "gb"
        chassis_name = f'{chassis_base}_{"gb" if rhs_driver else "eu"}'
        chassis_dst_folder = f'{self.vehicle_dst_dir}\\{vehicle}\\'
        if not os.path.exists(chassis_dst_folder):
            os.makedirs(chassis_dst_folder)
        chassis_dst_path = f'{chassis_dst_folder}{chassis_name}.sii'

        with open(chassis_src_path, "r", encoding="utf-8") as src:
            with open(chassis_dst_path, "w", encoding="utf-8") as dst:
                for input_line in src:
                    if "variant:" in input_line and rhs_driver:
                        continue
                    elif "variant_uk:" in input_line and rhs_driver:
                        variant_name = input_line.split(":")[1].strip()
                        dst.write(f"\tvariant: {variant_name}\n")
                    elif "variant_uk:" in input_line and not rhs_driver:
                        continue
                    else:
                        dst.write(input_line)
        return chassis_name

    def create_vehicle_traffic_defs(self, trailer_chains={}):
        for vehicle in self.vehicle_country_dict:
            vehicle_src_file = self.find_file(self.vehicle_src_loc, f'{self.variant_dict[vehicle]}.sui')
            with open(vehicle_src_file, "r", encoding="utf-8") as src:
                variants = set()
                accessories = set()
                data = src.readlines()
                vehicle_dst_file = os.path.join(self.vehicle_dst_dir, f'{self.variant_dict[vehicle]}.sui')
                if not os.path.exists(self.vehicle_dst_dir):
                    os.makedirs(self.vehicle_dst_dir)
                with open(vehicle_dst_file, "w", encoding="utf-8") as dst:
                    cnt = 0
                    for country_code in self.vehicle_country_dict[vehicle]:
                        if cnt > 0:
                            dst.write("\n\n")
                        if self.vehicle_country_dict[vehicle][country_code] > 0:
                            cnt += 1
                            chassis_name = None
                            is_truck = self.type == "truck"
                            is_trailer = self.type == "trailer"
                            for i, input_line in enumerate(data):
                                # gather original accessory and vehicle variant names
                                if "accessories[]:" in input_line and is_trailer:
                                    accessory_name = prepare_internal_name(input_line, is_accessory=True)
                                    accessories.add(accessory_name)
                                if "vehicle_accessory" in input_line and ".chassis" in input_line and not is_trailer:
                                    # create eu or uk chassis to ensure the steering wheel is always on the right side
                                    chassis_name = self.create_chassis(self.variant_dict[vehicle], data[i + 2], country_code)
                                if "variant" in input_line or "traffic_vehicle" in input_line or "traffic_trailer" in input_line:
                                    candidate_name = prepare_internal_name(input_line)
                                    is_new = True
                                    # only consider variant names which are not a substring of others
                                    for variant in variants:
                                        if variant in candidate_name:
                                            is_new = False
                                    if is_new:
                                        variants.add(candidate_name)
                                # create unique internal names for the accessories and variants based on the country_code
                                output_line = replace_longest_substring(input_line, variants | accessories,
                                                                        country_code)
                                if "traffic_trailer" in output_line:
                                    trailer_name = prepare_internal_name(output_line)
                                    dst.write(f"traffic_trailer : traffic.trailer.{trailer_name}\n")
                                elif "variant[]:" in output_line and is_trailer:
                                    variant_name = prepare_internal_name(output_line)
                                    dst.write(f"	variant[]: traffic.trailer.{variant_name}\n")
                                elif "@include \"drivers" in input_line:
                                    # set spawn ratio, parking settings and license plate type for non trailer types
                                    dst.write(
                                        f"\tspawn_ratio: 0\n\tallow_parked: true\n\tlicense_plate_type: {self.type}_{country_code}\n\n")
                                    dst.write(f"@include \"/def/vehicle/ai/drivers{input_line.split('drivers')[1]}\n")
                                elif is_truck and "trailer_chains[]:" in input_line:
                                    # match the truck with trailers of the corresponding country
                                    for trailer in trailer_chains.items():
                                        if trailer[1][country_code] > 0:
                                            dst.write(
                                                f"\ttrailer_chains[]: \"traffic.trailer.{trailer[0]}.{country_code}\"\n")
                                elif is_trailer and "cargo_mass:" in input_line:
                                    # set custom license plate type for trailer type
                                    dst.write(f"\tlicense_plate_type: {self.type}_{country_code}\n\n")
                                    dst.write(output_line)
                                elif "data_path:" in input_line and chassis_name is not None:
                                    # in case of a custom chassis, link to the newly created chassis file
                                    dst.write(
                                        f'\tdata_path: \"/def/vehicle/ai/{self.sub_dir}/{self.variant_dict[vehicle]}/{chassis_name}.sii\"\n')
                                    chassis_name = None
                                elif "spawn_ratio" in output_line or "allow_parked" in output_line:
                                    # ignore the old spawn and parking settings
                                    continue
                                else:
                                    dst.write(output_line)

    def create_lp_defs(self, types_to_create):
        for country in self.country_dict:
            lp_src_file = self.find_file(self.country_src_loc, country, 'license_plates.sii')
            lp_dst_dir = f"{self.country_dst_dir}{country}"
            if not os.path.exists(lp_dst_dir):
                os.makedirs(lp_dst_dir)
            # open and read file, extract vehicle lp info, put in separate .sui file that can be imported
            with open(lp_src_file, "r", encoding="utf-8") as src:
                # read the file and gather truck, trailer and car types if present
                found_vehicle = False
                vehicle_type = None
                wrote_mat = False
                f_lp_mat = "front"
                r_lp_mat = "rear"
                lines = []
                templates = []
                found_custom_font = False
                for line in src:
                    if found_vehicle:
                        if "{" not in line and "}" not in line:
                            if "type:" in line:
                                type_name = f"{vehicle_type}_{self.country_dict[country]}"
                            elif "templates[]:" in line:
                                if not wrote_mat:
                                    post_fix = ("", "") if vehicle_type == "trailer" else ("_f", "_r")
                                    lines.append(
                                        f'\tbackground_front: {type_name}{post_fix[0]}\n\tbackground_rear: {type_name}{post_fix[1]}\n\n')
                                    wrote_mat = True
                                parts = line.split('\"')
                                line = f'{parts[0]}\"<font face=/font/license_plate/{country}.font>{parts[1]}</font>\"\n'
                                lines.append(line)
                                templates.append((len(lines) - 1, parts))
                            # retrieve custom license plate materials
                            elif "background_front" in line:
                                f_lp_mat = line.split(":")[1].strip()
                            elif "background_rear" in line:
                                r_lp_mat = line.split(":")[1].strip()
                            elif "<font" in line:
                                # custom font settings found, specify country font face here
                                found_custom_font = True
                                lines.append(line.replace("<font", f"<font face=/font/license_plate/{country}.font"))
                            else:
                                lines.append(line)
                        elif "}" in line:
                            side_mats = []
                            lp_dst_file = os.path.join(lp_dst_dir, f'lp_{vehicle_type}_{self.country_dict[country]}.sui')
                            if found_custom_font:
                                # remove our font wrap from the templates lines again to prevent warnings
                                for (index, info) in templates:
                                    lines[index] = f'{info[0]}\"{info[1]}\"\n'
                            with open(lp_dst_file, "w", encoding="utf-8") as dst:
                                for line_to_write in lines:
                                    dst.write(line_to_write)
                                    # save materials specified with $SIDE$
                                    if "$SIDE$" in line_to_write:
                                        side_mats.append(line_to_write.split("$SIDE$")[1].split(".")[0])
                            # save the lp materials for this country and vehicle type
                            if country in self.country_lp_types:
                                self.country_lp_types[country][vehicle_type] = (f_lp_mat, r_lp_mat, side_mats)
                            else:
                                self.country_lp_types[country] = {vehicle_type: (f_lp_mat, r_lp_mat, side_mats)}
                            lines = []
                            templates = []
                            found_vehicle = False
                            found_custom_font = False
                            wrote_mat = False
                            vehicle_type = None
                            f_lp_mat = "front"
                            r_lp_mat = "rear"
                    elif "license_plate_data" in line:
                        for candidate in types_to_create:
                            if candidate in line and f"{candidate}_" not in line:
                                found_vehicle = True
                                vehicle_type = candidate

    def get_vehicles_for_country(self, country_code):
        vehicles = []
        for key, country_dict in self.vehicle_country_dict.items():
            vehicles.append((key, country_dict[country_code]))
        return vehicles

    def create_country_data(self, spawn_config):
        for country in spawn_config:
            traffic_dst_dir = f"{self.country_dst_dir}{country}"
            if not os.path.exists(traffic_dst_dir):
                os.makedirs(traffic_dst_dir)

            national_ratio = spawn_config[country]["national"]
            foreign_ratios = spawn_config[country]["international"].copy()

            # retrieve random countries, and calculate spawn ratios
            random_countries = [c for c in self.country_dict.keys() if
                                c not in map(lambda x: x[0], foreign_ratios) and c != country]
            random_ratio = max(0.001, spawn_config[country]["random"] / len(random_countries))
            for random_country in random_countries:
                foreign_ratios.append((random_country, random_ratio))

            # generate license plate data
            self.generate_lp_data(foreign_ratios, traffic_dst_dir)
            # generate traffic files (not needed for trailers)
            if self.type != "trailer":
                self.generate_spawn_info(foreign_ratios, national_ratio, traffic_dst_dir)
            # generate license plate material files
            self.generate_lp_mats(country, foreign_ratios)

    def generate_lp_mats(self, country, foreign_ratios):
        dst_dir = f"{self.material_dst_dir}{country}"
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for ratio in foreign_ratios:
            foreign_country = ratio[0]
            # check if type is available, else use fallback car type
            if self.type in self.country_lp_types[foreign_country]:
                f_mat, r_mat, side_mats = self.country_lp_types[foreign_country][self.type]
            else:
                f_mat, r_mat, side_mats = self.country_lp_types[foreign_country]["car"]
            src_locs = [f"{self.material_src_loc}{foreign_country}/{f_mat}.mat",
                         f"{self.material_src_loc}{foreign_country}/{r_mat}.mat"]

            for side, src_loc in enumerate(src_locs):
                src_file = self.find_file(src_loc)
                with open(src_file, "r", encoding="utf-8") as src:
                    data = src.readlines()
                    post_fix = "" if self.type == "trailer" else ("_f" if side == 0 else "_r")
                    plate_name = f"{self.type}_{self.country_dict[foreign_country]}{post_fix}"
                    dst_file = f"{dst_dir}\\{plate_name}.mat"
                    with open(dst_file, "w", encoding="utf-8") as dst:
                        for line in data:
                            if "texture" in line and "_name" not in line:
                                line = line.replace('\"', f'\"/material/ui/lp/{foreign_country}/', 1)
                            dst.write(line)
                    # generate materials required for the $SIDE$ parameter
                    for side_mat in side_mats:
                        original_prefix = "front" if side == 0 else "rear"
                        copy_src = self.find_file(f"{self.material_src_loc}{foreign_country}/{original_prefix}{side_mat}.mat")
                        copy_dst_folder = f"{self.material_dst_dir}{foreign_country}"
                        copy_dst = f"{copy_dst_folder}/{plate_name}{side_mat}.mat"
                        if not os.path.exists(copy_dst_folder):
                            os.makedirs(copy_dst_folder)
                        shutil.copy(copy_src, copy_dst)

    def generate_spawn_info(self, foreign_ratios, national_ratio, traffic_dst_dir):
        for ratio in foreign_ratios:
            foreign_abs = self.country_dict[ratio[0]]
            # filter out the vehicles that should spawn in the foreign country and calculate the rates for this country
            foreign_vehicles = [(vehicle[0], 1 * float(ratio[1]) / national_ratio * vehicle[1]) for vehicle in
                                self.get_vehicles_for_country(foreign_abs) if vehicle[1] > 0]
            # generate a foreign traffic definition for this country
            traffic_dst_file = os.path.join(traffic_dst_dir, f"traffic.{self.type}_{foreign_abs}.sii")
            with open(traffic_dst_file, "w", encoding="utf-8") as dst:
                dst.write("SiiNunit\n{\n")
                for foreign_vehicle in foreign_vehicles:
                    dst.write(f"country_traffic_info : .country.info.traffic.{foreign_vehicle[0]}.{foreign_abs} {{\n\t"
                              f"object: traffic.{foreign_vehicle[0]}.{foreign_abs}\n\tspawn_ratio: "
                              f"{str(round(foreign_vehicle[1], 3))}\n}}\n\n")
                dst.write("}")

    def generate_lp_data(self, foreign_ratios, traffic_dst_dir):
        lp_dst_file = os.path.join(traffic_dst_dir, f"license_plates.{self.type}_esm.sii")
        with open(lp_dst_file, "w", encoding="utf-8") as dst:
            dst.write("SiiNunit\n{\n")
            for ratio in foreign_ratios:
                foreign_country = ratio[0]
                foreign_abs = self.country_dict[foreign_country]
                lp_ref = self.type if self.type in self.country_lp_types[foreign_country] else "car"
                dst.write(
                    f"license_plate_data : .lp.{self.type}_{foreign_abs}\n{{\n\ttype: {self.type}_{foreign_abs}\n@include \"/def/country/{foreign_country}/lp_{lp_ref}_{foreign_abs}.sui\"\n}}\n\n")
            dst.write("}")

    def check_spawn_ratios(self, spawn_config):
        supported_countries = set(self.country_dict.keys())
        for country in spawn_config:
            foreign_countries = set()
            for ratio in spawn_config[country]["international"]:
                foreign_country = ratio[0]
                if foreign_country in foreign_countries:
                    print(f"Country {foreign_country} appears more than once in spawn configuration for {country}")
                    return False
                elif foreign_country not in supported_countries:
                    print(f"Unsupported country {foreign_country} in spawn configuration for {country}")
                    return False
                foreign_countries.add(foreign_country)
        return True

    def find_file(self, *args):
        for folder_path in self.search_folders:
            file_path = os.path.join(folder_path, *args)
            if os.path.exists(file_path):
                return file_path
        print(f"Could not find file: {args}")
