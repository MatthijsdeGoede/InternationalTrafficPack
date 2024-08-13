from creators.car import CarCreator


class CamperCreator(CarCreator):
    def __init__(self, base_folder, mod_folder, configuration):
        super().__init__(base_folder, mod_folder, configuration)
        self.post_fix = "_camper"
        self.type = "camper"
        self.traffic_storage = "truck_light"

    def get_spawn_config(self):
        return self.configuration.camper_spawn_config

    def get_vehicle_list(self):
        return self.configuration.camper_list
