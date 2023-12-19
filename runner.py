from car_vanilla import VanillaCarCreator
from semi_vanilla import VanillaTruckCreator, VanillaTrailerCreator

mod_folder = "C:\\Users\\Matth\\Desktop\\International Traffic Pack - ProMods Edition\\"
base_folder = "D:\\ETS2 Blender\\BaseFolder(1.48)\\"


def run_vanilla():
    # create car traffic
    car_creator = VanillaCarCreator(base_folder, mod_folder)
    car_creator.run()
    # create semi traffic
    trailer_creator = VanillaTrailerCreator(base_folder, mod_folder)
    trailer_creator.run()
    truck_creator = VanillaTruckCreator(base_folder, mod_folder, trailer_creator.vehicle_country_dict)
    truck_creator.run()


run_vanilla()
