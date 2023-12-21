from car_vanilla import VanillaCarCreator
from configuration.vanilla import VanillaConfiguration
from semi_vanilla import VanillaTruckCreator, VanillaTrailerCreator

mod_folder = "C:\\Users\\Matth\\Desktop\\International Traffic Pack - ProMods Edition\\"
base_folder = "D:\\ETS2 Blender\\BaseFolder(1.48)\\"
pm_folder = "D:\\SVN ProMods\\wip"


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


run_vanilla()
