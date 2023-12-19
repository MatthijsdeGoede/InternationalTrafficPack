from car_promods import ProModsCarCreator
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


def check_new_countries():
    pm_folder = "D:\\SVN ProMods\\wip\\"
    car_creator = VanillaCarCreator(base_folder, mod_folder)
    pm_car_creator = ProModsCarCreator(pm_folder, mod_folder)
    car_creator.set_country_dict()
    pm_car_creator.set_country_dict()

    for key in pm_car_creator.country_dict:
        if key not in car_creator.country_dict.keys():
            print(f"{key} ({pm_car_creator.country_dict[key]})")


#check_new_countries()
run_vanilla()
