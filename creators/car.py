from creators.base import BaseCreator
from utils.helper_methods import check_spawn_ratios


class CarCreator(BaseCreator):
    def __init__(self, base_folder, mod_folder, configuration):
        super().__init__("car", base_folder, mod_folder, configuration.rhs_driver_countries)
        self.configuration = configuration
        self.lp_types = ["car"]

    def get_spawn_config(self):
        return self.configuration.car_spawn_config

    def get_vehicle_list(self):
        return self.configuration.car_list

    def create(self):
        # set all countries and their abbreviations
        self.set_country_dict()
        # ensure that the spawn configuration is of the correct format
        assert check_spawn_ratios(self.get_spawn_config(), self.country_dict)
        # create license plate definitions, for non-addons
        if not self.is_addon:
            self.create_lp_defs(self.lp_types)
        # get all specified cars from traffic
        self.set_vehicles_per_country(self.get_vehicle_list(), check_spawn_rates=True)
        # create car definitions for every country and variant
        self.create_vehicle_traffic_defs()
        # create all other country related files
        self.create_country_data(self.get_spawn_config())
        # create a traffic storage file for the cars
        self.create_traffic_storage_file(self.get_vehicle_list())


class CarHookCreator(CarCreator):
    def __init__(self, base_folder, mod_folder, configuration, trailer_chains):
        super().__init__(base_folder, mod_folder, configuration)
        self.post_fix = "_hook"
        self.trailer_chains = trailer_chains

    def get_spawn_config(self):
        return self.configuration.caravan_spawn_config

    def get_vehicle_list(self):
        return self.configuration.car_hook_list

    def create(self):
        # set all countries and their abbreviations
        self.set_country_dict()
        # ensure that the spawn configuration is of the correct format
        assert check_spawn_ratios(self.get_spawn_config(), self.country_dict)
        # create license plate definitions, for non-addons
        if not self.is_addon:
            self.create_lp_defs(["car"])
        # get all specified cars from traffic
        self.set_vehicles_per_country(self.get_vehicle_list(), check_spawn_rates=True, hook=True)
        # create all other country related files
        self.create_country_data(self.get_spawn_config())
        # create car definitions for every country and variant
        self.create_vehicle_traffic_defs(trailer_chains=self.trailer_chains)
