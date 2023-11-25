import itertools
import os
import random

base_folder = "D:\\ETS2 Blender\\BaseFolder(1.48)\\"
mod_folder = "C:\\Users\\Matth\\Desktop\\International Traffic Pack - Vanilla Edition\\"
sub_dir = "esm"
country_src_dir = f"{base_folder}def\\country"
country_dst_dir = f"{mod_folder}def\\country\\"
vehicle_src_dir = f"{base_folder}def\\vehicle\\ai"
vehicle_dst_dir = f"{mod_folder}def\\vehicle\\ai\\{sub_dir}"
trailer_src_dir = f"{base_folder}def\\vehicle\\trailer"
trailer_dst_dir = f"{mod_folder}def\\vehicle\\trailer\\{sub_dir}"
material_src_dir = f"{base_folder}\\material\\ui\\lp\\"
material_dst_dir = f"{mod_folder}\\material\\ui\\lp\\"


def create_traffic_storage_file(vehicle_list, type):
    storage_dir = f"{mod_folder}def\\vehicle"
    storage_dst_file = f"{storage_dir}\\traffic_storage_{'trailer_truck' if type == 'trailer' else type}.esm.sii"
    with open(storage_dst_file, "w") as dst:
        dst.write("SiiNunit\n{\n")
        for vehicle in vehicle_list:
            dst.write(f"@include \"{'trailer' if type == 'trailer' else 'ai'}/{sub_dir}/{vehicle}.sui\"\n")
        dst.write("}")


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


def get_limited_spawn_rates(country_dict, limited_to):
    return {country_dict[country]: 1.00 if limited_to is None or country in limited_to else 0.00 for country in country_dict}

def get_vehicles_per_country(country_dict, vehicle_list, check_spawn_rates=False, src_dir=vehicle_src_dir,
                             first_variant_only=True, limited_to=None):
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
                    variant_name = prepare_internal_name(input_line)
                    variant_dict[variant_name] = vehicle

                    vehicle_country_dict[variant_name] = get_limited_spawn_rates(country_dict, limited_to)
                    # when working with sub variants, only the top variant should be added to the variant dict
                    if first_variant_only:
                        break

    if check_spawn_rates:
        # check the country traffic definitions for custom spawn rates
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
                            vehicle_country_dict[vehicle][country_dict[key]] = spawn_ratio


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


def get_characters_surrounding_substring(input_string, substring):
    index = input_string.find(substring)
    ancestor = input_string[index - 1] if index > 0 else ""
    successor = input_string[index + len(substring)] if index > 0 and index + len(substring) < len(
        input_string) else "\n"
    return ancestor, successor


def replace_longest_substring(line, replacements, code):
    longest_replacement = ""
    for replacement in replacements:
        # find the longest matching substring
        if replacement in line and len(replacement) > len(longest_replacement):
            longest_replacement = replacement
    if longest_replacement:
        # ignore comments
        start = "\t" if "\t" in line else ""
        line = f"{start}{line.split('#')[0].strip()}\n"
        prev_char, next_char = get_characters_surrounding_substring(line, longest_replacement)
        # only replace internal names containing a .
        if next_char == "\n" or next_char == "." and prev_char == ".":
            # put country code after occurrence
            line = line.replace(longest_replacement, f"{longest_replacement}.{code}")
        elif prev_char == ".":
            # put country code at the end of the internal name
            line = line.replace("\n", f".{code}\n")
    return line


def create_vehicle_traffic_defs(vehicle_country_dict, variant_dict, type_string, src_dir=vehicle_src_dir,
                                dst_dir=vehicle_dst_dir, trailer_chains={}):
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for vehicle in vehicle_country_dict:
        vehicle_src_file = os.path.join(src_dir, f'{variant_dict[vehicle]}.sui')
        with open(vehicle_src_file, "r", encoding="utf-8") as src:
            variants = set()
            accessories = set()
            data = src.readlines()
            vehicle_dst_file = os.path.join(dst_dir, f'{variant_dict[vehicle]}.sui')
            with open(vehicle_dst_file, "w", encoding="utf-8") as dst:
                cnt = 0
                for country_code in vehicle_country_dict[vehicle]:
                    if cnt > 0:
                        dst.write("\n\n")
                    if vehicle_country_dict[vehicle][country_code] > 0:
                        cnt += 1
                        chassis_name = None
                        is_truck = type_string == "truck"
                        is_trailer = type_string == "trailer"
                        for i, input_line in enumerate(data):
                            if "accessories[]:" in input_line and is_trailer:
                                accessory_name = prepare_internal_name(input_line, is_accessory=True)
                                accessories.add(accessory_name)
                            if "vehicle_accessory" in input_line and ".chassis" in input_line and not is_trailer:
                                chassis_name = create_chassis(variant_dict[vehicle], data[i + 2], country_code,
                                                              dst_dir=dst_dir)
                            if "variant" in input_line or "traffic_vehicle" in input_line or "traffic_trailer" in input_line:
                                candidate_name = prepare_internal_name(input_line)
                                is_new = True
                                for variant in variants:
                                    if variant in candidate_name:
                                        is_new = False
                                if is_new:
                                    variants.add(candidate_name)

                            output_line = replace_longest_substring(input_line, variants | accessories, country_code)
                            if "traffic_trailer" in output_line:
                                trailer_name = prepare_internal_name(output_line)
                                dst.write(f"traffic_trailer : traffic.trailer.{trailer_name}\n")
                            elif "variant[]:" in output_line and is_trailer:
                                variant_name = prepare_internal_name(output_line)
                                dst.write(f"	variant[]: traffic.trailer.{variant_name}\n")
                            elif "@include \"drivers" in input_line:
                                dst.write(f"\tspawn_ratio: 0\n\tlicense_plate_type: {type_string}_{country_code}\n\n")
                                dst.write(f"@include \"/def/vehicle/ai/drivers{input_line.split('drivers')[1]}\n")
                            elif is_truck and "trailer_chains[]:" in input_line:
                                for trailer in random.sample(list(trailer_chains.items()), 5):
                                    # check if trailer is suitable for this foreign country
                                    if trailer[1][country_code] > 0:
                                        dst.write(f"\ttrailer_chains[]: \"traffic.trailer.{trailer[0]}.{country_code}\"\n")
                            elif is_trailer and "cargo_mass:" in input_line:
                                dst.write(f"\tlicense_plate_type: {type_string}_{country_code}\n\n")
                                dst.write(output_line)
                            elif "data_path:" in input_line and chassis_name is not None:
                                dst.write(
                                    f'\tdata_path: \"/def/vehicle/ai/{sub_dir}/{variant_dict[vehicle]}/{chassis_name}.sii\"\n')
                                chassis_name = None
                            elif "spawn_ratio" in output_line:
                                continue
                            else:
                                dst.write(output_line)


def prepare_internal_name(input_line, is_accessory=False):
    split_line = input_line.split(".")[1:]
    accessory = ".".join(split_line[:-1] if is_accessory else split_line).split(" ")[0].strip()
    accessory = accessory.replace("traffic.", "")
    accessory = accessory.replace("trailer.", "")
    return accessory


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
                        elif "templates[]:" in line:
                            if not wrote_mat:
                                post_fix = ("", "") if vehicle_type == "trailer" else ("_f", "_r")
                                lines.append(f'\tbackground_front: {type_name}{post_fix[0]}\n\tbackground_rear: {type_name}{post_fix[1]}\n\n')
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
                # make it so that truck and trailer are always exported, if not specified they receive the same as car
    return country_lp_types


def get_vehicles_for_country(vehicles_country, country_code):
    vehicles = []
    for key, country_dict in vehicles_country.items():
        vehicles.append((key, country_dict[country_code]))
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
        generate_lp_data(country_abs, foreign_ratios, traffic_dst_dir, type, country_lps)
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
        src_files = [f"{material_src_dir}{foreign_country}/{f_mat}.mat",
                     f"{material_src_dir}{foreign_country}/{r_mat}.mat"]
        for src_file in src_files:
            with open(src_file, "r", encoding="utf-8") as src:
                data = src.readlines()
                post_fix = "" if type == "trailer" else ("_f" if "front" in src_file  else "_r")
                dst_file = f"{dst_dir}\\{type}_{country_abs[foreign_country]}{post_fix}.mat"
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


def generate_lp_data(country_abs, foreign_ratios, traffic_dst_dir, type, country_lps):
    lp_dst_file = os.path.join(traffic_dst_dir, f"license_plates.{type}_esm.sii")
    with open(lp_dst_file, "w", encoding="utf-8") as dst:
        dst.write("SiiNunit\n{\n")
        for ratio in foreign_ratios:
            foreign_country = ratio[0]
            foreign_abs = country_abs[foreign_country]
            lp_ref = type if type in country_lps[foreign_country] else "car"
            dst.write(
                f"license_plate_data : .lp.{type}_{foreign_abs}\n{{\n\ttype: {type}_{foreign_abs}\n@include \"/def/country/{foreign_country}/lp_{lp_ref}_{foreign_abs}.sui\"\n}}\n\n")
        dst.write("}")