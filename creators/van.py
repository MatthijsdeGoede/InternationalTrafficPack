from creators.car import CarCreator


class VanCreator(CarCreator):
    def __init__(self, base_folder, mod_folder, configuration):
        super().__init__(base_folder, mod_folder, configuration)
        self.post_fix = "_van"
        self.type = "van"
        self.traffic_storage = "truck_light"

    def get_spawn_config(self):
        return self.configuration.van_spawn_config

    def get_vehicle_list(self):
        return self.configuration.van_list
