from shared import *

vanilla_car_list = [
    "a3",
    "accord",
    "audi_a6",
    "bmw5",
    "clio",
    "mercedes_ce",
    "xc90",
    "astra",
    "fabia",
    "golf",

    "seat",
    "punto",
    "mondeo",
    "qashqai",
    "jaguar_xf",
    "lancer_x",
    "passat_cc",
    "citroen_c4",
    "mazda_3",
    "megane",
    "mini",
    "mondeo_2009",
    "octavia_2009",
    "peugeot_407",
    "range_rover",
    "focus_2009",
    "kia_ceed",

    "xc60",

    # Added from dlc_fr

    "tourer",
    "p3008",
    "talisman",
    "ford_smax",
    "passat_2014",

    "captur",
    "peugeot_208",
    "c3",

    "skoda_octavia_iii",
    "alfa_romeo_159",
    "kia_ceed_combi",
    "volvo_xc70",
    "vw_touran",

    # Added from dlc_it

    "mazda_cx3",

    "panda",
    "giulietta",
    "500l",
    "renegade",
    "ypsilon",

    "santafe",
    "huracan",
    "mustang_2015",

    # Added from dlc_balt
    "superb_iii",

    "duster",
    "laguna",
    "majestic_a_2018",

    "bgeed",
    "sand",
    "toyco",

    "ortiz_combi",

    "majestic_suv_luxury_22",

    "scout_fav"
]

spawn_config = {
    "netherlands": {
        "national": 0.79,
        "international": [("germany", 0.07), ("belgium", 0.05), ("poland", 0.04), ("france", 0.02), ("uk", 0.02)],
        "random": 0.01,
    },
    "germany": {
        "national": 0.79,
        "international": [("netherlands", 0.04), ("switzerland", 0.02), ("austria", 0.02), ("czech", 0.04),
                          ("poland", 0.04), ("france", 0.02), ("denmark", 0.02)],
        "random": 0.01,
    },
    "austria": {
        "national": 0.69,
        "international": [("germany", 0.08), ("netherlands", 0.06), ("switzerland", 0.02), ("czech", 0.03),
                          ("slovenia", 0.02), ("slovakia", 0.03), ("hungary", 0.03), ("italy", 0.03)],
        "random": 0.01,
    },
    "belgium": {
        "national": 0.79,
        "international": [("luxembourg", 0.05), ("netherlands", 0.05), ("germany", 0.03), ("france", 0.05),
                          ("uk", 0.02)],
        "random": 0.01,
    },
    "france": {
        "national": 0.79,
        "international": [("netherlands", 0.05), ("spain", 0.04), ("belgium", 0.02), ("switzerland", 0.01),
                          ("italy", 0.01), ("germany", 0.04), ("uk", 0.02), ("luxembourg", 0.01)],
        "random": 0.01,
    },
    "luxembourg": {
        "national": 0.69,
        "international": [("belgium", 0.08), ("germany", 0.07), ("netherlands", 0.06), ("france", 0.08)],
        "random": 0.01,
    },
    "norway": {
        "national": 0.79,
        "international": [("germany", 0.05), ("netherlands", 0.04), ("denmark", 0.04), ("sweden", 0.07)],
        "random": 0.01,
    },
    "uk": {
        "national": 0.79,
        "international": [("germany", 0.05), ("netherlands", 0.05), ("france", 0.04), ("belgium", 0.03),
                          ("lithuania", 0.01), ("poland", 0.02)],
        "random": 0.01,
    },
    "turkey": {
        "national": 0.79,
        "international": [("germany", 0.05), ("netherlands", 0.005), ("bulgaria", 0.04), ("romania", 0.04),
                          ("sweden", 0.005), ("russia", 0.04), ("macedonia", 0.005), ("bosnia", 0.005)],
        "random": 0.01,
    },
    "lithuania": {
        "national": 0.79,
        "international": [("latvia", 0.07), ("poland", 0.05), ("estonia", 0.04), ("uk", 0.03), ("russia", 0.01)],
        "random": 0.01,
    },
    "bulgaria": {
        "national": 0.79,
        "international": [("romania", 0.07), ("hungary", 0.03), ("germany", 0.03), ("turkey", 0.02),
                          ("macedonia", 0.02), ("serbia", 0.03)],
        "random": 0.01,
    },
    "poland": {
        "national": 0.79,
        "international": [("czech", 0.04), ("slovakia", 0.04), ("germany", 0.03), ("lithuania", 0.04), ("latvia", 0.03),
                          ("estonia", 0.02)],
        "random": 0.01,
    },
    "portugal": {
        "national": 0.79,
        "international": [("spain", 0.06), ("france", 0.05), ("uk", 0.02), ("luxembourg", 0.01), ("netherlands", 0.03),
                          ("germany", 0.03)],
        "random": 0.01,
    },
    "spain": {
        "national": 0.79,
        "international": [("portugal", 0.06), ("france", 0.05), ("uk", 0.02), ("luxembourg", 0.01),
                          ("netherlands", 0.03), ("germany", 0.03)],
        "random": 0.01,
    },
    "romania": {
        "national": 0.79,
        "international": [("germany", 0.05), ("italy", 0.01), ("france", 0.01), ("turkey", 0.02), ("hungary", 0.04),
                          ("serbia", 0.03), ("poland", 0.02), ("bulgaria", 0.02)],
        "random": 0.01,
    },
    "russia": {
        "national": 0.89,
        "international": [("finland", 0.035), ("estonia", 0.03), ("latvia", 0.025), ("lithuania", 0.01)],
        "random": 0.01,
    },
    "estonia": {
        "national": 0.79,
        "international": [("latvia", 0.05), ("lithuania", 0.03), ("finland", 0.05), ("germany", 0.03), ("poland", 0.01),
                          ("russia", 0.03)],
        "random": 0.01,
    },
    "finland": {
        "national": 0.79,
        "international": [("estonia", 0.05), ("latvia", 0.05), ("lithuania", 0.02), ("sweden", 0.02), ("norway", 0.03),
                          ("poland", 0.02), ("russia", 0.01)],
        "random": 0.01,
    },
    "hungary": {
        "national": 0.79,
        "international": [("romania", 0.05), ("slovakia", 0.04), ("austria", 0.02), ("serbia", 0.02),
                          ("slovenia", 0.02), ("croatia", 0.02), ("italy", 0.01), ("germany", 0.01), ("turkey", 0.01)],
        "random": 0.01,

    },
    "switzerland": {
        "national": 0.74,
        "international": [("germany", 0.05), ("france", 0.05), ("austria", 0.05), ("italy", 0.05), ("uk", 0.03),
                          ("netherlands", 0.02)],
        "random": 0.01,
    },
    "latvia": {
        "national": 0.79,
        "international": [("lithuania", 0.06), ("estonia", 0.05), ("finland", 0.02), ("germany", 0.02),
                          ("poland", 0.02), ("russia", 0.03)],
        "random": 0.01,
    },
    "sweden": {
        "national": 0.79,
        "international": [("norway", 0.05), ("finland", 0.04), ("denmark", 0.04), ("germany", 0.03),
                          ("netherlands", 0.03)],
        "random": 0.01,
    },
    "denmark": {
        "national": 0.79,
        "international": [("germany", 0.06), ("sweden", 0.05), ("norway", 0.05), ("netherlands", 0.04)],
        "random": 0.01,
    },
    "czech": {
        "national": 0.79,
        "international": [("germany", 0.04), ("poland", 0.05), ("austria", 0.04), ("slovakia", 0.04),
                          ("hungary", 0.03)],
        "random": 0.01,
    },
    "italy": {
        "national": 0.79,
        "international": [("germany", 0.06), ("netherlands", 0.04), ("switzerland", 0.02), ("france", 0.03),
                          ("slovenia", 0.02), ("austria", 0.03)],
        "random": 0.01,
    },
    "slovakia": {
        "national": 0.79,
        "international": [("czech", 0.04), ("poland", 0.05), ("austria", 0.04), ("germany", 0.03), ("hungary", 0.04)],
        "random": 0.01,
    },
    "albania": {
        "national": 0.79,
        "international": [("montenegro", 0.05), ("kosovo", 0.05), ("macedonia", 0.06), ("germany", 0.01),
                          ("serbia", 0.03)],
        "random": 0.01,
    },
    "bosnia": {
        "national": 0.79,
        "international": [("montenegro", 0.06), ("croatia", 0.06), ("serbia", 0.06), ("hungary", 0.01)],
        "random": 0.01,
    },
    "croatia": {
        "national": 0.79,
        "international": [("montenegro", 0.02), ("slovenia", 0.05), ("hungary", 0.03), ("bosnia", 0.04),
                          ("serbia", 0.03), ("germany", 0.02), ("netherlands", 0.01)],
        "random": 0.01,
    },
    "kosovo": {
        "national": 0.79,
        "international": [("montenegro", 0.03), ("serbia", 0.08), ("macedonia", 0.05), ("albania", 0.04)],
        "random": 0.01,
    },
    "macedonia": {
        "national": 0.79,
        "international": [("kosovo", 0.04), ("turkey", 0.02), ("bulgaria", 0.05), ("serbia", 0.04), ("albania", 0.05)],
        "random": 0.01,
    },
    "montenegro": {
        "national": 0.79,
        "international": [("bosnia", 0.05), ("croatia", 0.02), ("serbia", 0.05), ("kosovo", 0.04), ("albania", 0.04)],
        "random": 0.01,
    },
    "serbia": {
        "national": 0.79,
        "international": [("montenegro", 0.02), ("bosnia", 0.03), ("hungary", 0.03), ("bulgaria", 0.03),
                          ("kosovo", 0.03), ("turkey", 0.02), ("macedonia", 0.02), ("croatia", 0.02)],
        "random": 0.01,
    },
    "slovenia": {
        "national": 0.79,
        "international": [("croatia", 0.03), ("austria", 0.04), ("italy", 0.03), ("croatia", 0.04), ("hungary", 0.03),
                          ("bosnia", 0.02), ("germany", 0.01)],
        "random": 0.01,
    },
}

type_string = "car"


def create_lp_defs(country_abs):
    for country in country_abs:
        lp_src_file = os.path.join(country_src_dir, country, 'license_plates.sii')
        lp_dst_dir = f"{country_dst_dir}{country}"
        if not os.path.exists(lp_dst_dir):
            os.makedirs(lp_dst_dir)
        lp_dst_file = os.path.join(lp_dst_dir, f'lp_car_{country_abs[country]}.sui')
        # open and read file, extract vehicle lp info, put in separate .sui file that can be imported
        with open(lp_src_file, "r", encoding="utf-8") as src:
            with open(lp_dst_file, "w", encoding="utf-8") as dst:
                found_car = False
                type = None
                wrote_mat = False
                # TODO: extend later to work with trucks, trailers and busses as well
                for line in src:
                    if found_car:
                        if "{" not in line and "}" not in line:
                            if "type:" in line:
                                type = f"{line.split(':')[1].strip()}_{country_abs[country]}"
                                dst.write(f"\ttype: {type}\n")
                            elif "templates[]:" in line:
                                if not wrote_mat:
                                    dst.write(f'\tbackground_front: {type}_f\n\tbackground_rear: {type}_r\n\n')
                                    wrote_mat = True
                                parts = line.split('\"')
                                line = f'{parts[0]}\"<font face=/font/license_plate/{country}.font>{parts[1]}</font>\"\n'
                                dst.write(line)
                            else:
                                dst.write(line)
                        elif "}" in line:
                            break
                    elif "license_plate_data" in line and ".lp.car" in line:
                        found_car = True


def get_cars_for_country(cars_country, country_code):
    cars = []
    for key, value_list in cars_country.items():
        for tuple_item in value_list:
            if tuple_item[0] == country_code:
                cars.append((key, tuple_item[1]))
    return cars


def create_country_data(country_abs, cars_country, type):
    for country in spawn_config:
        traffic_dst_dir = f"{country_dst_dir}{country}"
        if not os.path.exists(traffic_dst_dir):
            os.makedirs(traffic_dst_dir)

        national_ratio = spawn_config[country]["national"]
        foreign_ratios = spawn_config[country]["international"]

        # retrieve random countries, and calculate spawn_ratio
        random_countries = [c for c in country_abs.keys() if c not in map(lambda x: x[0], foreign_ratios) and c != country]
        random_ratio = max(0.001, spawn_config[country]["random"] / len(random_countries))
        for random_country in random_countries:
            foreign_ratios.append((random_country, random_ratio))

        # generate license plate data
        generate_lp_data(country_abs, foreign_ratios, traffic_dst_dir, type)
        # generate traffic files
        generate_spawn_info(cars_country, country_abs, foreign_ratios, national_ratio, traffic_dst_dir, type)
        # generate license plate material files
        generate_lp_mats(country, country_abs, foreign_ratios, type)


def generate_lp_mats(country, country_abs, foreign_ratios, type):
    dst_dir = f"{material_dst_dir}{country}"
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    for ratio in foreign_ratios:
        # TODO: change this system to work with other types as well.
        src_files = [f"{material_src_dir}{ratio[0]}/front.mat", f"{material_src_dir}{ratio[0]}/rear.mat"]
        for src_file in src_files:
            with open(src_file, "r", encoding="utf-8") as src:
                data = src.readlines()
                dst_file = f"{dst_dir}\\{type}_{country_abs[ratio[0]]}_{'f' if 'front' in src_file else 'r'}.mat"
                with open(dst_file, "w", encoding="utf-8") as dst:
                    for line in data:
                        if "texture" in line and "_name" not in line:
                            line = line.replace('\"', f'\"/material/ui/lp/{ratio[0]}/', 1)
                        dst.write(line)


def generate_spawn_info(cars_country, country_abs, foreign_ratios, national_ratio, traffic_dst_dir, type):
    for ratio in foreign_ratios:
        foreign_abs = country_abs[ratio[0]]
        # filter out the vehicles that should spawn in the foreign country and calculate the rates for this country
        foreign_cars = [(car[0], 1 * float(ratio[1]) / national_ratio * car[1]) for car in
                        get_cars_for_country(cars_country, foreign_abs) if car[1] > 0]
        # generate a foreign traffic definition for this country
        traffic_dst_file = os.path.join(traffic_dst_dir, f"traffic.{type}_{foreign_abs}.sii")
        with open(traffic_dst_file, "w", encoding="utf-8") as dst:
            dst.write("SiiNunit\n{\n")
            for foreign_car in foreign_cars:
                dst.write(f"country_traffic_info : .country.info.traffic.{foreign_car[0]}.{foreign_abs} {{\n\t"
                          f"object: traffic.{foreign_car[0]}.{foreign_abs}\n\tspawn_ratio: "
                          f"{str(round(foreign_car[1], 3))}\n}}\n\n")
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


# get all countries and their abbreviations
country_abbreviations = get_country_abbreviations()
# get all specified cars from traffic
variant_dict, cars_per_country = get_vehicles_per_country(country_abbreviations, vanilla_car_list, check_spawn_rates=True)
# create car definitions for every country and variant
create_vehicle_traffic_defs(cars_per_country, variant_dict, type_string)
# create license plate definitions
create_lp_defs(country_abbreviations)
# create all other country related files
create_country_data(country_abbreviations, cars_per_country, type_string)
