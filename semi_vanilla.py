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
    "truck_transporter_traffic",
    "car_transporter_traffic",
    "willig_fuel_cistern_traffic",
    "scs_curtain_traffic",
    "scs_reefer_traffic",
    "scs_dryvan_traffic",
    "scs_dryvan_mfloor_traffic",
    "scs_aero_dynamic_traffic",
    "glass_trailer_traffic",
    "scs_flatbed_brick_traffic",


    # double
    #"scs_curtain_bdouble_traffic",
    #"scs_curtain_double_traffic",

    #"scs_reefer_bdouble_traffic",
    #"scs_reefer_double_traffic",

    #"scs_dryvan_bdouble_traffic",
    #"scs_dryvan_double_traffic",

    # log trailer
    "scs_log_traffic",
    "scs_gooseneck_traffic",

    # food trailer
    "scs_foodtank_traffic",

    # lowbed
    "scs_lowbed_traffic",

    # lowloader
    "scs_lowloader_traffic",

    "van_transporter_traffic",

    #dumper
    #"scs_dumper_traffic",

    #fueltank
    "scs_fueltank_traffic",
    #silo
    "scs_silo_traffic",

    #chemtank
    "scs_chemtank_traffic",

    #gastank
    "scs_gastank_traffic",

    # livestock trailer
    "scs_livestock_traffic",


    ## DLC Feldbinder

    "feldbinder_eut_35_traffic",
    "feldbinder_kip_60_traffic",
    "feldbinder_tsa_adr_22_traffic",
    "feldbinder_tsa_lm_32_traffic",


    # DLC Krone

    "krone_profiliner_2017_traffic",
    "krone_dryliner_2017_traffic",
    "krone_profiliner_hd_2017_traffic",
    "krone_coolliner_2017_traffic",
    "krone_boxliner_2017_traffic",
    "krone_profiliner_bm_traffic",


    ## DLC North

    "scs_dry_van_3_stw_traffic.dlc_north",
    "scs_curtain_3_stw_traffic.dlc_north",
    "scs_m_floor_3_stw_traffic.dlc_north",
    "scs_reefer_3_stw_traffic.dlc_north",

    # lowbed
    "scs_lowbed_traffic.dlc_north",


    ## DLC Schwarzmuller

    "schwarzmuller_curtain_traffic",
    "schwarzmuller_reefer_traffic",
    "schwarzmuller_slidepost_traffic",
    "schwarzmuller_cistern_food_traffic",
    "schwarzmuller_lowloader_traffic",

    ## DLC Trailers

    # lowbed
    "scs_lowbed_traffic.dlc_trailers",
    # lowloader
    "scs_lowloader_traffic.dlc_trailers",


    ## DLC Wielton

    "wielton_curtain_master_traffic",
    "wielton_dry_master_traffic",
    #"wielton_dropside_master_traffic",
    #"wielton_weight_master_traffic",
    #"wielton_strong_master_traffic",
]

spawn_config = {
    "netherlands": {
        "national": 0.60,
        "international": [("poland", 0.10), ("romania", 0.06), ("lithuania", 0.04), ("germany", 0.04), ("belgium", 0.03), ("france", 0.02), ("uk", 0.01)],
        "random": 0.10,
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


truck_type_string = "truck"
trailer_type_string = "trailer"
trailer_src_dir = f"{base_folder}def\\vehicle\\trailer"
trailer_dst_dir = f"{mod_folder}def\\vehicle\\trailer\\mdg"

# get all countries and their abbreviations
country_abbreviations = get_country_abbreviations()
# create license plate definitions
country_lps = create_lp_defs(country_abbreviations, ["car", "truck", "trailer"])
# get all specified trucks from traffic
truck_variant_dict, trucks_per_country = get_vehicles_per_country(country_abbreviations, vanilla_truck_list)
# get all specified trailers from traffic
trailer_variant_dict, trailer_per_country = get_vehicles_per_country(country_abbreviations, vanilla_trailer_list, src_dir=trailer_src_dir, first_variant_only=False)
# make a trailer def for each trailer for each country, set custom license plate
create_vehicle_traffic_defs(trailer_per_country, trailer_variant_dict, trailer_type_string, src_dir=trailer_src_dir, dst_dir=trailer_dst_dir)
# make a truck def for each truck for each country, set spawn_ratio to 0, custom license plate and link with all country trailers via trailer_chains
create_vehicle_traffic_defs(trucks_per_country, truck_variant_dict, truck_type_string, trailer_chains=trailer_per_country)
# create all other country related files for the trucks
create_country_data(country_abbreviations, trucks_per_country, truck_type_string, country_lps, spawn_config)
# create all other country related files for the trailers
create_country_data(country_abbreviations, trailer_per_country, trailer_type_string, country_lps, spawn_config)
