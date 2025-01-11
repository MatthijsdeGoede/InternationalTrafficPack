from creators.base import BaseCreator
from utils.helper_methods import check_spawn_ratios


class TruckCreator(BaseCreator):
    def __init__(self, base_folder, mod_folder, trailer_chains, configuration):
        super().__init__("truck", base_folder, mod_folder, configuration.rhs_driver_countries)
        self.configuration = configuration
        self.traffic_storage = "truck"
        self.trailer_chains = trailer_chains

    def create(self):
        # get all countries and their abbreviations
        self.set_country_dict()
        # ensure that the spawn configuration is of the correct format
        assert check_spawn_ratios(self.configuration.truck_spawn_config, self.country_dict)
        # create license plate definitions, for non-addons
        if not self.is_addon:
            self.create_lp_defs(["car", "truck", "trailer"])
        # get all specified trucks from traffic
        self.set_vehicles_per_country(self.configuration.truck_list)
        # make a truck def for each truck for each country and link with all country trailers via trailer_chains
        self.create_vehicle_traffic_defs(trailer_chains=self.trailer_chains)
        # create all other country related files for the trucks
        self.create_country_data(self.configuration.truck_spawn_config, self.configuration.excluded_countries)
        # create a traffic storage file for the trucks
        self.create_traffic_storage_file(self.configuration.truck_list)


class TrailerCreator(BaseCreator):
    def __init__(self, base_folder, mod_folder, configuration):
        super().__init__("trailer", base_folder, mod_folder, configuration.rhs_driver_countries)
        self.configuration = configuration
        self.traffic_storage = "trailer_truck"
        self.vehicle_src_loc = f"def\\vehicle\\trailer"
        self.vehicle_dst_dir = f"{mod_folder}def\\vehicle\\trailer\\{self.sub_dir}"

    def create(self):
        # get all countries and their abbreviations
        self.set_country_dict()
        # create license plate definitions
        self.create_lp_defs(["car", "truck", "trailer"])
        # get all specified trailers from traffic
        self.set_vehicles_per_country(self.configuration.trailer_list)
        # make a trailer definition
        self.create_vehicle_traffic_defs()
        # create all other country related files for the trailers
        self.create_country_data(self.configuration.truck_spawn_config, self.configuration.excluded_countries)
        # create a traffic storage file for the trailers
        self.create_traffic_storage_file(self.configuration.trailer_list)
