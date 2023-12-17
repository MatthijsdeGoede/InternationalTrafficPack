from base_class import BaseClass
from configuration.vanilla import truck_spawn_config, truck_list, trailer_list


class VanillaTruckCreator(BaseClass):
    def __init__(self, base_folder, mod_folder, trailer_chains):
        super().__init__("truck", base_folder, mod_folder)
        self.trailer_chains = trailer_chains

    def run(self):
        # get all countries and their abbreviations
        self.set_country_dict()
        # ensure that the spawn configuration is of the correct format
        assert self.check_spawn_ratios(truck_spawn_config)
        # create license plate definitions
        self.create_lp_defs(["car", "truck", "trailer"])
        # get all specified trucks from traffic
        self.set_vehicles_per_country(truck_list)
        # make a truck def for each truck for each country and link with all country trailers via trailer_chains
        self.create_vehicle_traffic_defs(trailer_chains=self.trailer_chains)
        # create all other country related files for the trucks
        self.create_country_data(truck_spawn_config)
        # create a traffic storage file for the trucks
        self.create_traffic_storage_file(truck_list)


class VanillaTrailerCreator(BaseClass):
    def __init__(self, base_folder, mod_folder):
        super().__init__("trailer", base_folder, mod_folder)

    def run(self):
        # get all countries and their abbreviations
        self.set_country_dict()
        # create license plate definitions
        self.create_lp_defs(["car", "truck", "trailer"])
        # get all specified trailers from traffic
        self.set_vehicles_per_country(trailer_list)
        # make a truck def for each truck for each country and link with all country trailers via trailer_chains
        self.create_vehicle_traffic_defs()
        # create all other country related files for the trailers
        self.create_country_data(truck_spawn_config)
        # create a traffic storage file for the trailers
        self.create_traffic_storage_file(trailer_list)
