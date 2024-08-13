from configuration.ai_jazzy import AiJazzyVanillaConfiguration
from configuration.folders import *
from configuration.promods import ProModsConfiguration
from configuration.vanilla import VanillaConfiguration
from creators.bus import BusCreator
from creators.camper import CamperCreator
from creators.car import CarCreator, CarHookCreator
from creators.caravan import CaravanCreator
from creators.semi import TrailerCreator, TruckCreator
from creators.van import VanCreator


def run_vanilla():
    # retrieve the configuration for the vanilla mod
    configuration = VanillaConfiguration()
    # create cars
    CarCreator(base_folder, vanilla_dst_folder, configuration).create()
    # create semis
    trailer_creator = TrailerCreator(base_folder, vanilla_dst_folder, configuration)
    trailer_creator.create()
    TruckCreator(base_folder, vanilla_dst_folder, trailer_creator.vehicle_country_dict, configuration).create()
    # create cars with caravans
    caravan_creator = CaravanCreator(base_folder, vanilla_dst_folder, configuration)
    caravan_creator.create()
    CarHookCreator(base_folder, vanilla_dst_folder, configuration, caravan_creator.vehicle_country_dict).create()
    # create campers
    CamperCreator(base_folder, vanilla_dst_folder, configuration).create()
    # create vans
    VanCreator(base_folder, vanilla_dst_folder, configuration).create()
    # create busses
    BusCreator(base_folder, vanilla_dst_folder, configuration).create()


def run_pro_mods():
    # retrieve the configuration for the ProMods mod
    configuration = ProModsConfiguration()
    # create car traffic
    car_creator = CarCreator(base_folder, pm_dst_folder, configuration)
    car_creator.search_folders = [pm_lp_src_folder, pm_src_folder, base_folder]
    car_creator.create()
    # create semi traffic
    trailer_creator = TrailerCreator(base_folder, pm_dst_folder, configuration)
    trailer_creator.search_folders = [pm_lp_src_folder, pm_src_folder, base_folder]
    trailer_creator.create()
    truck_creator = TruckCreator(base_folder, pm_dst_folder, trailer_creator.vehicle_country_dict, configuration)
    truck_creator.search_folders = [pm_lp_src_folder, pm_src_folder, base_folder]
    truck_creator.create()


def run_ai_jazzy_vanilla():
    # retrieve the configuration for the Jazzycat AI traffic mod
    configuration = AiJazzyVanillaConfiguration()
    car_creator = CarCreator(jazzy_ai_src_folder, jazzy_ai_dst_folder, configuration)
    car_creator.is_addon = True
    car_creator.post_fix = ".jazzy_ai"
    car_creator.search_folders = [jazzy_ai_src_folder, base_folder]
    # create car traffic
    car_creator.create()


# run_ai_jazzy_vanilla()
run_vanilla()
# run_pro_mods()

# TODO: configure caravan and camper spawn rates (vanilla)
# TODO: configure bus spawn rates (vanilla)
# TODO: configure van spawn rates (vanilla)
