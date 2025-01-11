from creators.base import BaseCreator


class CaravanCreator(BaseCreator):
    def __init__(self, base_folder, mod_folder, configuration):
        super().__init__("trailer", base_folder, mod_folder, configuration.rhs_driver_countries)
        self.configuration = configuration
        self.traffic_storage = "trailer_car"

    def create(self):
        # get all countries and their abbreviations
        self.set_country_dict()
        # create license plate definitions
        self.create_lp_defs(["car", "trailer"])
        # get all specified trailers from traffic
        self.set_vehicles_per_country(self.configuration.caravan_list)
        # make a trailer definition
        self.create_vehicle_traffic_defs()
        # create all other country related files for the caravans
        self.create_country_data(self.configuration.caravan_spawn_config, self.configuration.excluded_countries)
        # create a traffic storage file for the trailers
        self.create_traffic_storage_file(self.configuration.caravan_list)
