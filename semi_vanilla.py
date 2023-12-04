from shared import *

vanilla_truck_list = [
    "daf_xf_b_4x2",
    "daf_xf_c_6x4",
    "daf_xf_euro6_a_4x2",
    "daf_xf_euro6_b_4x2",
    "iveco_hiway_a_6x4",
    "iveco_stralis_a_4x2",
    "iveco_stralis_c_6x4",
    "man_tgx_a_4x2",
    "man_tgx_c_6x4",
    "man_tgx_euro6_a_4x2",
    "man_tgx_euro6_b_6x24",
    "mercedes_actros_a_4x2",
    "mercedes_actros_a_6x4",
    "mercedes_actros_2014_a_4x2",
    "mercedes_actros_2014_b_4x2_p",
    "renault_magnum_c_4x2",
    "renault_premium_a_4x2",
    "renault_premium_b_4x2",
    "renault_t_a_4x2",
    "renault_t_b_6x2",
    "renault_t_evo_a_4x2",
    "renault_t_evo_b_6x2",
    "scania_a_4x2",
    "scania_b_6x2",
    "scania_c_4x2",
    "scania_streamline_a_4x2",
    "scania_streamline_c_6x4",
    "scania_s_2016_a_4x2",
    "scania_s_2016_b_6x2",
    "scania_r_2016_a_4x2",
    "scania_r_2016_b_6x2",
    "volvo_fh16_2009_a_4x2",
    "volvo_fh16_2009_c_6x4",
    "volvo_fh16_2012_a_4x2",
    "volvo_fh16_2012_c_6x4",
]

vanilla_trailer_list = [
    "scs_curtain_traffic",  # 2 variants
    "scs_reefer_traffic",  # 1 variant
    "scs_dryvan_traffic",  # 1 variant
    "scs_dryvan_mfloor_traffic",  # 1 variant
    "scs_foodtank_traffic",  # 2 variants
    "scs_chemtank_traffic",  # 1 variant
    "scs_silo_traffic",  # 1 variant
    "scs_aero_dynamic_traffic",  # 1 variant
    "car_transporter_traffic",  # 4 variants
    "scs_gooseneck_traffic",  # 5 variants
    "scs_flatbed_brick_traffic",  # 9 variants
]

spawn_config = {
    "netherlands": {
        "national": 0.60,
        "international": [("poland", 0.10), ("romania", 0.04), ("germany", 0.05), ("belgium", 0.04),
                          ("lithuania", 0.02), ("france", 0.01), ("uk", 0.01), ("spain", 0.01), ("hungary", 0.01),
                          ("luxembourg", 0.01)],
        "random": 0.10,
    },
    "germany": {
        "national": 0.60,
        "international": [("poland", 0.13), ("netherlands", 0.03), ("lithuania", 0.03), ("romania", 0.02),
                          ("austria", 0.01), ("czech", 0.01), ("bulgaria", 0.01), ("slovenia", 0.01),
                          ("hungary", 0.01), ("luxembourg", 0.01), ("denmark", 0.01), ("france", 0.01),
                          ("switzerland", 0.01), ("portugal", 0.01)],
        "random": 0.10,
    },
    "austria": {
        "national": 0.60,
        "international": [("germany", 0.08), ("poland", 0.04), ("hungary", 0.03), ("slovenia", 0.03),
                          ("slovakia", 0.03), ("romania", 0.02), ("czech", 0.02), ("croatia", 0.02),
                          ("lithuania", 0.01), ("switzerland", 0.01), ("italy", 0.01)],
        "random": 0.10,
    },
    "belgium": {
        "national": 0.60,
        "international": [("netherlands", 0.07), ("luxembourg", 0.05), ("poland", 0.05), ("france", 0.04),
                          ("romania", 0.02), ("uk", 0.02), ("lithuania", 0.01), ("germany", 0.01), ("italy", 0.01),
                          ("hungary", 0.01), ("portugal", 0.01)],
        "random": 0.10,
    },
    "france": {
        "national": 0.60,
        "international": [("poland", 0.06), ("belgium", 0.04), ("spain", 0.04), ("lithuania", 0.03),
                          ("portugal", 0.03), ("uk", 0.02), ("romania", 0.02), ("germany", 0.02), ("italy", 0.01),
                          ("luxembourg", 0.01), ("netherlands", 0.01), ("switzerland", 0.01)],
        "random": 0.10,
    },
    "luxembourg": {
        "national": 0.60,
        "international": [("belgium", 0.06), ("france", 0.05), ("poland", 0.05), ("germany", 0.03),
                          ("netherlands", 0.05), ("lithuania", 0.03), ("romania", 0.02), ("switzerland", 0.01)],
        "random": 0.10,
    },
    "norway": {
        "national": 0.60,
        "international": [("sweden", 0.08), ("lithuania", 0.07), ("poland", 0.04), ("latvia", 0.03), ("germany", 0.03),
                          ("denmark", 0.02), ("estonia", 0.02), ("netherlands", 0.01)],
        "random": 0.10,
    },
    "uk": {
        "national": 0.60,
        "international": [("poland", 0.08), ("germany", 0.05), ("netherlands", 0.04), ("france", 0.04),
                          ("belgium", 0.03),
                          ("lithuania", 0.02), ("romania", 0.02), ("hungary", 0.02)],
        "random": 0.10,
    },
    "turkey": {
        "national": 0.80,
        "international": [("bulgaria", 0.06), ("romania", 0.03), ("poland", 0.03), ("russia", 0.02), ("serbia", 0.01)],
        "random": 0.05,
    },
    "lithuania": {
        "national": 0.65,
        "international": [("latvia", 0.08), ("poland", 0.06), ("estonia", 0.06), ("finland", 0.02), ("sweden", 0.02),
                          ("russia", 0.01)],
        "random": 0.10,
    },
    "bulgaria": {
        "national": 0.60,
        "international": [("turkey", 0.10), ("romania", 0.08), ("hungary", 0.04), ("serbia", 0.03), ("poland", 0.03),
                          ("macedonia", 0.02)],
        "random": 0.10,
    },
    "poland": {
        "national": 0.60,
        "international": [("germany", 0.08), ("lithuania", 0.08), ("romania", 0.05), ("slovakia", 0.02),
                          ("latvia", 0.02), ("czech", 0.01), ("austria", 0.01), ("slovenia", 0.01), ("hungary", 0.01),
                          ("croatia", 0.01)],
        "random": 0.10,
    },
    "portugal": {
        "national": 0.60,
        "international": [("spain", 0.07), ("romania", 0.04), ("poland", 0.04), ("france", 0.03), ("bulgaria", 0.02),
                          ("lithuania", 0.02), ("uk", 0.02), ("czech", 0.02), ("germany", 0.02), ("hungary", 0.01),
                          ("slovenia", 0.01)],
        "random": 0.10,
    },
    "spain": {
        "national": 0.60,
        "international": [("portugal", 0.07), ("romania", 0.04), ("poland", 0.04), ("france", 0.03), ("bulgaria", 0.02),
                          ("lithuania", 0.02), ("uk", 0.02), ("netherlands", 0.02), ("germany", 0.02), ("hungary", 0.01),
                          ("slovenia", 0.01)],
        "random": 0.10,
    },
    "romania": {
        "national": 0.60,
        "international": [("turkey", 0.08), ("hungary", 0.08), ("poland", 0.07), ("serbia", 0.03), ("bulgaria", 0.04)],
        "random": 0.10,
    },
    "russia": {
        "national": 0.85,
        "international": [("lithuania", 0.06), ("latvia", 0.03), ("poland", 0.02), ("finland", 0.02),
                          ("estonia", 0.01)],
        "random": 0.01,
    },
    "estonia": {
        "national": 0.60,
        "international": [("latvia", 0.07), ("lithuania", 0.06), ("poland", 0.06), ("finland", 0.05), ("russia", 0.02),
                          ("romania", 0.02), ("germany", 0.02)],
        "random": 0.10,
    },
    "finland": {
        "national": 0.60,
        "international": [("poland", 0.09), ("estonia", 0.06), ("germany", 0.03), ("sweden", 0.03), ("norway", 0.03),
                          ("latvia", 0.02), ("lithuania", 0.02), ("russia", 0.02)],
        "random": 0.10,
    },
    "hungary": {
        "national": 0.60,
        "international": [("poland", 0.08), ("romania", 0.06), ("slovakia", 0.05), ("turkey", 0.04),
                          ("czech", 0.02), ("germany", 0.02), ("austria", 0.02), ("croatia", 0.01), ("serbia", 0.01)],
        "random": 0.10,
    },
    "switzerland": {
        "national": 0.60,
        "international": [("germany", 0.11), ("poland", 0.07), ("italy", 0.06), ("austria", 0.01), ("slovakia", 0.01),
                          ("france", 0.01), ("netherlands", 0.01), ("hungary", 0.01), ("lithuania", 0.01)],
        "random": 0.10,
    },
    "latvia": {
        "national": 0.60,
        "international": [("lithuania", 0.08), ("poland", 0.06), ("estonia", 0.06), ("finland", 0.02), ("sweden", 0.02),
                          ("russia", 0.01)],
        "random": 0.10,
    },
    "sweden": {
        "national": 0.60,
        "international": [("poland", 0.08), ("norway", 0.04), ("denmark", 0.04), ("lithuania", 0.03), ("latvia", 0.02),
                          ("germany", 0.02), ("estonia", 0.02), ("netherlands", 0.02), ("finland", 0.02),
                          ("romania", 0.01)],
        "random": 0.10,
    },
    "denmark": {
        "national": 0.60,
        "international": [("poland", 0.08), ("norway", 0.05), ("sweden", 0.05), ("germany", 0.04), ("lithuania", 0.03),
                          ("romania", 0.02), ("netherlands", 0.02), ("czech", 0.01)],
        "random": 0.10,
    },
    "czech": {
        "national": 0.60,
        "international": [("poland", 0.09), ("slovakia", 0.09), ("germany", 0.04), ("lithuania", 0.02),
                          ("hungary", 0.02), ("romania", 0.01), ("austria", 0.02), ("netherlands", 0.01)],
        "random": 0.10,
    },
    "italy": {
        "national": 0.60,
        "international": [("poland", 0.06), ("romania", 0.04), ("france", 0.04), ("lithuania", 0.03), ("germany", 0.03),
                          ("slovenia", 0.03), ("austria", 0.03), ("bulgaria", 0.03), ("slovakia", 0.02),
                          ("switzerland", 0.01)],
        "random": 0.10,
    },
    "slovakia": {
        "national": 0.60,
        "international": [("czech", 0.12), ("poland", 0.09), ("hungary", 0.07), ("austria", 0.01), ("germany", 0.1)],
        "random": 0.10,
    },
    "albania": {
        "national": 0.79,
        "international": [("montenegro", 0.04), ("kosovo", 0.04), ("macedonia", 0.05), ("italy", 0.03),
                          ("serbia", 0.03), ("germany", 0.01)],
        "random": 0.01,
    },
    "bosnia": {
        "national": 0.89,
        "international": [("germany", 0.03), ("austria", 0.02), ("montenegro", 0.01), ("croatia", 0.01),
                          ("serbia", 0.02), ("hungary", 0.01)],
        "random": 0.01,
    },
    "croatia": {
        "national": 0.79,
        "international": [("slovenia", 0.03), ("poland", 0.03), ("hungary", 0.03), ("germany", 0.03),
                          ("slovakia", 0.02), ("turkey", 0.01), ("italy", 0.01), ("lithuania", 0.01),
                          ("montenegro", 0.01), ("bosnia", 0.01), ("serbia", 0.01)],
        "random": 0.01,
    },
    "kosovo": {
        "national": 0.79,
        "international": [("montenegro", 0.03), ("serbia", 0.08), ("macedonia", 0.03), ("albania", 0.08)],
        "random": 0.01,
    },
    "macedonia": {
        "national": 0.79,
        "international": [("turkey", 0.06), ("kosovo", 0.03), ("bulgaria", 0.03), ("serbia", 0.04), ("albania", 0.04)],
        "random": 0.01,
    },
    "montenegro": {
        "national": 0.79,
        "international": [("germany", 0.04), ("bosnia", 0.03), ("croatia", 0.02), ("serbia", 0.03), ("kosovo", 0.04),
                          ("albania", 0.04)],
        "random": 0.01,
    },
    "serbia": {
        "national": 0.69,
        "international": [("turkey", 0.08), ("romania", 0.06), ("hungary", 0.5), ("bulgaria", 0.03),
                          ("montenegro", 0.02), ("bosnia", 0.02), ("kosovo", 0.01), ("macedonia", 0.02),
                          ("croatia", 0.01)],
        "random": 0.01,
    },
    "slovenia": {
        "national": 0.65,
        "international": [("romania", 0.06), ("poland", 0.04), ("slovakia", 0.04), ("hungary", 0.03), ("turkey", 0.03),
                          ("italy", 0.02), ("austria", 0.02), ("slovenia", 0.01), ("croatia", 0.01), ("serbia", 0.01),
                          ("bulgaria", 0.01), ("macedonia", 0.01), ("bosnia", 0.01)],
        "random": 0.05,
    },
}

truck_type_string = "truck"
trailer_type_string = "trailer"


# get all countries and their abbreviations
country_abbreviations = get_country_abbreviations()
# ensure that the spawn configuration is of the correct format
assert check_spawn_ratios(spawn_config, country_abbreviations)
# create license plate definitions
country_lps = create_lp_defs(country_abbreviations, ["car", "truck", "trailer"])
# get all specified trucks from traffic
truck_variant_dict, trucks_per_country = get_vehicles_per_country(country_abbreviations, vanilla_truck_list)
# get all specified vanilla trailers from traffic
trailer_variant_dict, trailer_per_country = get_vehicles_per_country(country_abbreviations, vanilla_trailer_list,
                                                                     src_dir=trailer_src_dir)
# make a trailer def for each trailer for each country, set custom license plate
create_vehicle_traffic_defs(trailer_per_country, trailer_variant_dict, trailer_type_string, src_dir=trailer_src_dir,
                            dst_dir=trailer_dst_dir)
# make a truck def for each truck for each country and link with all country trailers via trailer_chains
create_vehicle_traffic_defs(trucks_per_country, truck_variant_dict, truck_type_string,
                            trailer_chains=trailer_per_country)
# create all other country related files for the trucks
create_country_data(country_abbreviations, trucks_per_country, truck_type_string, country_lps, spawn_config)
# create all other country related files for the trailers
create_country_data(country_abbreviations, trailer_per_country, trailer_type_string, country_lps, spawn_config)
# create a traffic storage file for the trucks
create_traffic_storage_file(vanilla_truck_list, truck_type_string)
# create a traffic storage file for the trailers
create_traffic_storage_file(vanilla_trailer_list, trailer_type_string)
