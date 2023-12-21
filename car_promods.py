from base import BaseCreator


class ProModsCarCreator(BaseCreator):
    def __init__(self, base_folder, mod_folder, pm_folder, configuration):
        super().__init__("car", base_folder, mod_folder)
        self.configuration = configuration
        self.search_folders = [pm_folder, base_folder]

    def create(self):
        # set all countries and their abbreviations
        self.set_country_dict()
        # ensure that the spawn configuration is of the correct format
        assert self.check_spawn_ratios(self.configuration.car_spawn_config)
        # create license plate definitions
        self.create_lp_defs(["car"])
        # get all specified cars from traffic
        self.set_vehicles_per_country(self.configuration.car_list, check_spawn_rates=True)
        # create car definitions for every country and variant
        self.create_vehicle_traffic_defs(rhs_countries=self.configuration.rhs_driver_countries)
        # create all other country related files
        self.create_country_data(self.configuration.car_spawn_config)
        # create a traffic storage file for the cars
        self.create_traffic_storage_file(self.configuration.car_list)


# TODO: adapt methods so that they copy over @include files in lp defs
# TODO: adapt methods to properly deal with custom fonts, so when font is specified explicitly
