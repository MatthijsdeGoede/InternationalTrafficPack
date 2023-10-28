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


def get_vehicles_per_country(country_dict, vehicle_list, check_spawn_rates=False, src_dir=vehicle_src_dir, first_variant_only=True):
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
                    # for cars it's enough to take the first variant only, whereas for trailers it's not
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


def create_vehicle_traffic_defs(vehicle_country_dict, variant_dict, type_string, src_dir=vehicle_src_dir, dst_dir=vehicle_dst_dir, trailer_chains={}):
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
                                chassis_name = create_chassis(variant_dict[vehicle], data[i + 2], country_code, dst_dir=dst_dir)
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
