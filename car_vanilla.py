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

# get all countries and their abbreviations
country_abbreviations = get_country_abbreviations()
# create license plate definitions
country_lps = create_lp_defs(country_abbreviations, ["car"])
# get all specified cars from traffic
variant_dict, cars_per_country = get_vehicles_per_country(country_abbreviations, vanilla_car_list,
                                                          check_spawn_rates=True)
# create car definitions for every country and variant
create_vehicle_traffic_defs(cars_per_country, variant_dict, type_string)
# create all other country related files
create_country_data(country_abbreviations, cars_per_country, type_string, country_lps, spawn_config)
