from base import BaseCreator
from configuration.vanilla import car_spawn_config, car_list


class VanillaCarCreator(BaseCreator):
    def __init__(self, base_folder, mod_folder):
        super().__init__("car", base_folder, mod_folder)

    def run(self):
        # set all countries and their abbreviations
        self.set_country_dict()
        # ensure that the spawn configuration is of the correct format
        assert self.check_spawn_ratios(car_spawn_config)
        # create license plate definitions
        self.create_lp_defs(["car"])
        # get all specified cars from traffic
        self.set_vehicles_per_country(car_list, check_spawn_rates=True)
        # create car definitions for every country and variant
        self.create_vehicle_traffic_defs()
        # create all other country related files
        self.create_country_data(car_spawn_config)
        # create a traffic storage file for the cars
        self.create_traffic_storage_file(car_list)
