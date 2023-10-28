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

truck_type_string = "truck"
trailer_type_string = "trailer"
trailer_src_dir = f"{base_folder}def\\vehicle\\trailer"
trailer_dst_dir = f"{mod_folder}def\\vehicle\\trailer\\mdg"

# get all countries and their abbreviations
country_abbreviations = get_country_abbreviations()
# get all specified trucks from traffic
truck_variant_dict, trucks_per_country = get_vehicles_per_country(country_abbreviations, vanilla_truck_list)
# get all specified trailers from traffic
trailer_variant_dict, trailer_per_country = get_vehicles_per_country(country_abbreviations, vanilla_trailer_list, src_dir=trailer_src_dir, first_variant_only=False)
# make a trailer def for each trailer for each country, set custom license plate
create_vehicle_traffic_defs(trailer_per_country, trailer_variant_dict, trailer_type_string, src_dir=trailer_src_dir, dst_dir=trailer_dst_dir)
# make a truck def for each truck for each country, set spawn_ratio to 0, custom license plate and link with all country trailers via trailer_chains
create_vehicle_traffic_defs(trucks_per_country, truck_variant_dict, truck_type_string, trailer_chains=trailer_per_country)
# create license plate definitions

# use spawn config to generate country specific traffic definitions

# export truck and trailer license plate materials and defs