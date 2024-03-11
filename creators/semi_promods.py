from base import BaseCreator


class ProModsTruckCreator(BaseCreator):
    def __init__(self, base_folder, mod_folder, lp_folder, pm_folder, trailer_chains, configuration):
        super().__init__("truck", base_folder, mod_folder)
        self.configuration = configuration
        self.trailer_chains = trailer_chains
        self.search_folders = [lp_folder, pm_folder, base_folder]

    def create(self):
        # get all countries and their abbreviations
        self.set_country_dict()
        # ensure that the spawn configuration is of the correct format
        assert self.check_spawn_ratios(self.configuration.truck_spawn_config)
        # create license plate definitions
        self.create_lp_defs(["car", "truck", "trailer"])
        # get all specified trucks from traffic
        self.set_vehicles_per_country(self.configuration.truck_list)
        # make a truck def for each truck for each country and link with all country trailers via trailer_chains
        self.create_vehicle_traffic_defs(trailer_chains=self.trailer_chains, rhs_countries=self.configuration.rhs_driver_countries)
        # create all other country related files for the trucks
        self.create_country_data(self.configuration.truck_spawn_config)
        # create a traffic storage file for the trucks
        self.create_traffic_storage_file(self.configuration.truck_list)


class ProModsTrailerCreator(BaseCreator):
    def __init__(self, base_folder, mod_folder, lp_folder, pm_folder, configuration):
        super().__init__("trailer", base_folder, mod_folder)
        self.configuration = configuration
        self.vehicle_src_loc = f"def\\vehicle\\trailer"
        self.vehicle_dst_dir = f"{mod_folder}def\\vehicle\\trailer\\{self.sub_dir}"
        self.search_folders = [lp_folder, pm_folder, base_folder]

    def create(self):
        # get all countries and their abbreviations
        self.set_country_dict()
        # create license plate definitions
        self.create_lp_defs(["car", "truck", "trailer"])
        # get all specified trailers from traffic
        self.set_vehicles_per_country(self.configuration.trailer_list)
        # make a trailer definition
        self.create_vehicle_traffic_defs(rhs_countries=self.configuration.rhs_driver_countries)
        # create all other country related files for the trailers
        self.create_country_data(self.configuration.truck_spawn_config)
        # create a traffic storage file for the trailers
        self.create_traffic_storage_file(self.configuration.trailer_list)
