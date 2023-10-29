import itertools
import os

base_folder = "D:\\ETS2 Blender\\BaseFolder(1.48)\\"
mod_folder = "C:\\Users\\Matth\\Desktop\\International Traffic Pack - Vanilla Edition\\"
country_src_dir = f"{base_folder}def\\country"
country_dst_dir = f"{mod_folder}def\\country\\"
vehicle_src_dir = f"{base_folder}def\\vehicle\\ai"
vehicle_dst_dir = f"{mod_folder}def\\vehicle\\ai\\mdg"
material_src_dir = f"{base_folder}\\material\\ui\\lp\\"
material_dst_dir = f"{mod_folder}\\material\\ui\\lp\\"


def get_os_path(path):
    return path.replace("/", "\\")


def get_country_abbreviations():
    country_dict = {}

    for filename in os.listdir(country_src_dir):
        f = os.path.join(country_src_dir, filename)
        if os.path.isfile(f):
            country_name = filename.split(".")[0]
            with open(f, encoding="utf8") as opened:
                for line in opened:
                    if "country_code:" in line:
                        abbreviation = line.split("\"")[1]
                        country_dict[country_name] = abbreviation.lower()
                        break

    return country_dict


def get_vehicles_per_country(country_dict, vehicle_list, check_spawn_rates=False, src_dir=vehicle_src_dir,
                             first_variant_only=True):
    vehicle_country_dict = {}
    variant_dict = {}

    # retrieve the variants that belong to the selected vehicles
    for vehicle in vehicle_list:
        vehicle_src_file = os.path.join(src_dir, f'{vehicle}.sui')
        with open(vehicle_src_file, "r", encoding="utf-8") as src:
            for input_line in src:
                # find first entry
                if "traffic_vehicle" in input_line or "traffic_trailer" in input_line:
                    # assume standard 1.00 spawn rate for all variants and update this based on the traffic definitions
                    variant_name = ".".join(input_line.split(".")[1:]).split(" ")[0].strip()
                    variant_name = variant_name.replace("traffic.", "")
                    variant_name = variant_name.replace("trailer.", "")
                    variant_dict[variant_name] = vehicle
                    vehicle_country_dict[variant_name] = [(country_dict[country], 1.00) for country in country_dict]
                    # when working with sub variants, only the top variant should be added to the variant dict
                    if first_variant_only:
                        break

    if check_spawn_rates:
        # check the traffic definitions for custom spawn rates
        adapt_spawn_rates(country_dict, vehicle_country_dict)
    return variant_dict, vehicle_country_dict


def adapt_spawn_rates(country_dict, vehicle_country_dict):
    # check the traffic definitions for custom spawn rates and adapt where needed
    for key in country_dict:
        f = os.path.join(country_src_dir, key, 'traffic.sii')
        with open(f, encoding="utf8") as opened:
            for line1, line2 in itertools.zip_longest(*[opened] * 2):
                if line2 is not None and "spawn_ratio: " in line2:
                    spawn_ratio = float(line2.split("spawn_ratio: ")[1].strip())
                    # take the minimum of 1.00 and the specified spawn rate
                    if spawn_ratio < 1.00:
                        vehicle = ".".join(line1.split(".")[1:]).strip()
                        if vehicle in vehicle_country_dict:
                            for idx, pair in enumerate(vehicle_country_dict[vehicle]):
                                if pair[0] == country_dict[key]:
                                    vehicle_country_dict[vehicle][idx] = (country_dict[key], spawn_ratio)


def create_chassis(vehicle, line, country_code, dst_dir=vehicle_dst_dir):
    chassis_base = line.split("/")[-1].split(".")[0]
    chassis_path = get_os_path(line.split('\"')[1])
    chassis_src_path = f"{base_folder}{chassis_path}"
    is_uk = country_code == "gb"
    chassis_name = f'{chassis_base}_{"gb" if is_uk else "eu"}'
    chassis_dst_folder = f'{dst_dir}\\{vehicle}\\'
    if not os.path.exists(chassis_dst_folder):
        os.makedirs(chassis_dst_folder)
    chassis_dst_path = f'{chassis_dst_folder}{chassis_name}.sii'

    with open(chassis_src_path, "r", encoding="utf-8") as src:
        with open(chassis_dst_path, "w", encoding="utf-8") as dst:
            for input_line in src:
                if "variant:" in input_line and is_uk:
                    continue
                elif "variant_uk:" in input_line and is_uk:
                    variant_name = input_line.split(":")[1].strip()
                    dst.write(f"\tvariant: {variant_name}\n")
                elif "variant_uk:" in input_line and not is_uk:
                    continue
                else:
                    dst.write(input_line)
    return chassis_name


def create_vehicle_traffic_defs(vehicle_country_dict, variant_dict, type_string, src_dir=vehicle_src_dir,
                                dst_dir=vehicle_dst_dir, trailer_chains={}):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for vehicle in vehicle_country_dict:
        vehicle_src_file = os.path.join(src_dir, f'{variant_dict[vehicle]}.sui')
        with open(vehicle_src_file, "r", encoding="utf-8") as src:
            variants = set()
            data = src.readlines()
            vehicle_dst_file = os.path.join(dst_dir, f'{variant_dict[vehicle]}.sui')
            with open(vehicle_dst_file, "w", encoding="utf-8") as dst:
                cnt = 0
                for pair in vehicle_country_dict[vehicle]:
                    if cnt > 0:
                        dst.write("\n\n")
                    if pair[1] > 0:
                        cnt += 1
                        country_code = pair[0]
                        chassis_name = None
                        is_truck = type_string == "truck"
                        is_trailer = type_string == "trailer"
                        for i, input_line in enumerate(data):
                            if "vehicle_accessory" in input_line and ".chassis" in input_line and not is_trailer:
                                chassis_name = create_chassis(variant_dict[vehicle], data[i + 2], country_code,
                                                              dst_dir=dst_dir)
                            if "variant" in input_line or "traffic_vehicle" in input_line or "traffic_trailer" in input_line:
                                candidate_name = ".".join(input_line.split(".")[1:]).strip()
                                is_new = True
                                for variant in variants:
                                    if variant in candidate_name:
                                        is_new = False
                                if is_new:
                                    variants.add(candidate_name)
                            output_line = input_line
                            for replace in variants:
                                output_line = output_line.replace(f".{replace}", f".{replace}.{country_code}")
                            if "traffic_trailer" in input_line and "traffic." in input_line and "traffic.trailer" not in input_line:
                                output_line = output_line.replace("traffic.", "traffic.trailer.")
                            if "@include \"drivers" in input_line:
                                dst.write(f"\tspawn_ratio: 0\n\tlicense_plate_type: {type_string}_{country_code}\n\n")
                                dst.write(f"@include \"/def/vehicle/ai/drivers{input_line.split('drivers')[1]}\n")
                            elif is_truck and "trailer_chains[]:" in input_line:
                                for trailer in trailer_chains:
                                    dst.write(f"\ttrailer_chains[]: \"traffic.trailer.{trailer}.{country_code}\"\n")
                            elif is_trailer and "cargo_mass:" in input_line:
                                dst.write(f"\tlicense_plate_type: {type_string}_{country_code}\n\n")
                                dst.write(output_line)
                            elif "data_path:" in input_line and chassis_name is not None:
                                dst.write(
                                    f'\tdata_path: \"/def/vehicle/ai/mdg/{variant_dict[vehicle]}/{chassis_name}.sii\"\n')
                                chassis_name = None
                            else:
                                dst.write(output_line)


def create_lp_defs(country_abs, types_to_create):
    country_lp_types = {}
    for country in country_abs:
        lp_src_file = os.path.join(country_src_dir, country, 'license_plates.sii')
        lp_dst_dir = f"{country_dst_dir}{country}"
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
            for line in src:
                if found_vehicle:
                    if "{" not in line and "}" not in line:
                        if "type:" in line:
                            type_name = f"{vehicle_type}_{country_abs[country]}"
                            lines.append(f"\ttype: {type_name}\n")
                        elif "templates[]:" in line:
                            if not wrote_mat:
                                lines.append(f'\tbackground_front: {type_name}_f\n\tbackground_rear: {type_name}_r\n\n')
                                wrote_mat = True
                            parts = line.split('\"')
                            line = f'{parts[0]}\"<font face=/font/license_plate/{country}.font>{parts[1]}</font>\"\n'
                            lines.append(line)
                        elif "background_front" in line:
                            f_lp_mat = line.split(":")[1].strip()
                        elif "background_rear" in line:
                            r_lp_mat = line.split(":")[1].strip()
                        else:
                            lines.append(line)
                    elif "}" in line:
                        lp_dst_file = os.path.join(lp_dst_dir, f'lp_{vehicle_type}_{country_abs[country]}.sui')
                        with open(lp_dst_file, "w", encoding="utf-8") as dst:
                            for line_to_write in lines:
                                dst.write(line_to_write)
                        if country in country_lp_types:
                            country_lp_types[country][vehicle_type] = (f_lp_mat, r_lp_mat)
                        else:
                            country_lp_types[country] = {vehicle_type: (f_lp_mat, r_lp_mat)}
                        lines = []
                        found_vehicle = False
                        wrote_mat = False
                        vehicle_type = None
                        f_lp_mat = "front"
                        r_lp_mat = "rear"
                elif "license_plate_data" in line:
                    for candidate in types_to_create:
                        if candidate in line:
                            found_vehicle = True
                            vehicle_type = candidate
    return country_lp_types

def get_vehicles_for_country(vehicles_country, country_code):
    vehicles = []
    for key, value_list in vehicles_country.items():
        for tuple_item in value_list:
            if tuple_item[0] == country_code:
                vehicles.append((key, tuple_item[1]))
    return vehicles


def create_country_data(country_abs, vehicles_country, type, country_lps, spawn_config):
    for country in spawn_config:
        traffic_dst_dir = f"{country_dst_dir}{country}"
        if not os.path.exists(traffic_dst_dir):
            os.makedirs(traffic_dst_dir)

        national_ratio = spawn_config[country]["national"]
        foreign_ratios = spawn_config[country]["international"].copy()

        # retrieve random countries, and calculate spawn_ratio
        random_countries = [c for c in country_abs.keys() if
                            c not in map(lambda x: x[0], foreign_ratios) and c != country]
        random_ratio = max(0.001, spawn_config[country]["random"] / len(random_countries))
        for random_country in random_countries:
            foreign_ratios.append((random_country, random_ratio))

        # generate license plate data
        generate_lp_data(country_abs, foreign_ratios, traffic_dst_dir, type)
        # generate traffic files (not needed for trailers)
        if type != "trailer":
            generate_spawn_info(vehicles_country, country_abs, foreign_ratios, national_ratio, traffic_dst_dir, type)
        # generate license plate material files
        generate_lp_mats(country, country_abs, foreign_ratios, type, country_lps)


def generate_lp_mats(country, country_abs, foreign_ratios, type, country_lps):
    dst_dir = f"{material_dst_dir}{country}"
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for ratio in foreign_ratios:
        foreign_country = ratio[0]
        # check if type is available, else use fallback car type
        if type in country_lps[foreign_country]:
            f_mat, r_mat = country_lps[foreign_country][type]
        else:
            f_mat, r_mat = country_lps[foreign_country]["car"]
        src_files = [f"{material_src_dir}{foreign_country}/{f_mat}.mat", f"{material_src_dir}{foreign_country}/{r_mat}.mat"]
        for src_file in src_files:
            with open(src_file, "r", encoding="utf-8") as src:
                data = src.readlines()
                dst_file = f"{dst_dir}\\{type}_{country_abs[foreign_country]}_{'f' if 'front' in src_file else 'r'}.mat"
                with open(dst_file, "w", encoding="utf-8") as dst:
                    for line in data:
                        if "texture" in line and "_name" not in line:
                            line = line.replace('\"', f'\"/material/ui/lp/{foreign_country}/', 1)
                        dst.write(line)


def generate_spawn_info(vehicles_country, country_abs, foreign_ratios, national_ratio, traffic_dst_dir, type):
    for ratio in foreign_ratios:
        foreign_abs = country_abs[ratio[0]]
        # filter out the vehicles that should spawn in the foreign country and calculate the rates for this country
        foreign_vehicles = [(vehicle[0], 1 * float(ratio[1]) / national_ratio * vehicle[1]) for vehicle in
                            get_vehicles_for_country(vehicles_country, foreign_abs) if vehicle[1] > 0]
        # generate a foreign traffic definition for this country
        traffic_dst_file = os.path.join(traffic_dst_dir, f"traffic.{type}_{foreign_abs}.sii")
        with open(traffic_dst_file, "w", encoding="utf-8") as dst:
            dst.write("SiiNunit\n{\n")
            for foreign_vehicle in foreign_vehicles:
                dst.write(f"country_traffic_info : .country.info.traffic.{foreign_vehicle[0]}.{foreign_abs} {{\n\t"
                          f"object: traffic.{foreign_vehicle[0]}.{foreign_abs}\n\tspawn_ratio: "
                          f"{str(round(foreign_vehicle[1], 3))}\n}}\n\n")
            dst.write("}")


def generate_lp_data(country_abs, foreign_ratios, traffic_dst_dir, type):
    lp_dst_file = os.path.join(traffic_dst_dir, f"license_plates.{type}_mdg.sii")
    with open(lp_dst_file, "w", encoding="utf-8") as dst:
        dst.write("SiiNunit\n{\n")
        for ratio in foreign_ratios:
            foreign_abs = country_abs[ratio[0]]
            dst.write(
                f"license_plate_data : .lp.{type}_{foreign_abs}\n{{\n@include \"/def/country/{ratio[0]}/lp_{type}_{foreign_abs}.sui\"\n}}\n\n")
        dst.write("}")
