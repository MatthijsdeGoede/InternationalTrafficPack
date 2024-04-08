from configuration.ai_jazzy import AiJazzyVanillaConfiguration
from creators.car_promods import ProModsCarCreator
from creators.car_vanilla import VanillaCarCreator
from configuration.promods import ProModsConfiguration
from configuration.vanilla import VanillaConfiguration
from creators.semi_promods import ProModsTrailerCreator, ProModsTruckCreator
from creators.semi_vanilla import VanillaTruckCreator, VanillaTrailerCreator

mod_folder = "C:\\Users\\Matth\\Desktop\\International Traffic Pack - Add-on for AI Traffic Pack by Jazzycat\\"
base_folder = "D:\\ETS2 Blender\\BaseFolder(1.48)\\"
pm_folder = "D:\\SVN ProMods\\wip\\"
jazzy_ai_folder = "C:\\Users\\Matth\\Desktop\\AI Traffic Pack by Jazzycat"
lp_folder = "C:\\Users\\Matth\\Desktop\\pm lps\\"


def run_vanilla():
    # retrieve the configuration for the vanilla mod
    configuration = VanillaConfiguration()
    # create car traffic
    car_creator = VanillaCarCreator(base_folder, mod_folder, configuration)
    car_creator.create()
    # create semi traffic
    trailer_creator = VanillaTrailerCreator(base_folder, mod_folder, configuration)
    trailer_creator.create()
    truck_creator = VanillaTruckCreator(base_folder, mod_folder, trailer_creator.vehicle_country_dict, configuration)
    truck_creator.create()


def run_pro_mods():
    # retrieve the configuration for the ProMods mod
    configuration = ProModsConfiguration()
    # create car traffic
    car_creator = ProModsCarCreator(base_folder, mod_folder, lp_folder, pm_folder, configuration)
    car_creator.create()
    # create semi traffic
    trailer_creator = ProModsTrailerCreator(base_folder, mod_folder, lp_folder, pm_folder, configuration)
    trailer_creator.create()
    truck_creator = ProModsTruckCreator(base_folder, mod_folder, lp_folder, pm_folder,
                                        trailer_creator.vehicle_country_dict, configuration)
    truck_creator.create()


def run_ai_jazzy_vanilla():
    # retrieve the configuration for the Jazzycat AI traffic mod
    configuration = AiJazzyVanillaConfiguration()
    car_creator = VanillaCarCreator(jazzy_ai_folder, mod_folder, configuration)
    car_creator.is_addon = True
    car_creator.post_fix = ".jazzy_ai"
    car_creator.search_folders = [jazzy_ai_folder, base_folder]
    # create car traffic
    car_creator.create()


run_ai_jazzy_vanilla()
# run_vanilla()
# run_pro_mods()
