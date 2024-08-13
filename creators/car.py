from creators.base import BaseCreator


class CarCreator(BaseCreator):
    def __init__(self, base_folder, mod_folder, configuration):
        super().__init__("car", base_folder, mod_folder, configuration.rhs_driver_countries)
        self.configuration = configuration

    def create(self):
        # set all countries and their abbreviations
        self.set_country_dict()
        # ensure that the spawn configuration is of the correct format
        assert self.check_spawn_ratios(self.configuration.car_spawn_config)
        # create license plate definitions, for non-addons
        if not self.is_addon:
            self.create_lp_defs(["car"])
        # get all specified cars from traffic
        self.set_vehicles_per_country(self.configuration.car_list, check_spawn_rates=True)
        # create car definitions for every country and variant
        self.create_vehicle_traffic_defs()
        # create all other country related files
        self.create_country_data(self.configuration.car_spawn_config)
        # create a traffic storage file for the cars
        self.create_traffic_storage_file(self.configuration.car_list)


class CarHookCreator(CarCreator):
    def __init__(self, base_folder, mod_folder, configuration, trailer_chains):
        super().__init__(base_folder, mod_folder, configuration)
        self.post_fix = "_hook"
        self.trailer_chains = trailer_chains

    def create(self):
        # set all countries and their abbreviations
        self.set_country_dict()
        # ensure that the spawn configuration is of the correct format
        assert self.check_spawn_ratios(self.configuration.caravan_spawn_config)
        # create license plate definitions, for non-addons
        if not self.is_addon:
            self.create_lp_defs(["car"])
        # get all specified cars from traffic
        self.set_vehicles_per_country(self.configuration.car_hook_list, check_spawn_rates=True, hook=True)
        # create all other country related files
        self.create_country_data(self.configuration.caravan_spawn_config)
        # create car definitions for every country and variant
        self.create_vehicle_traffic_defs(trailer_chains=self.trailer_chains)
