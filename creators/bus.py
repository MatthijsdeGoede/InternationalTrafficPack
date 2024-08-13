from creators.car import CarCreator


class BusCreator(CarCreator):
    def __init__(self, base_folder, mod_folder, configuration):
        super().__init__(base_folder, mod_folder, configuration)
        self.type = "bus"
        self.traffic_storage = "bus"
        self.lp_types = ["car", "bus"]

    def get_spawn_config(self):
        return self.configuration.bus_spawn_config

    def get_vehicle_list(self):
        return self.configuration.bus_list
