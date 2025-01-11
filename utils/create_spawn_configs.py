import csv
import math
import os
import heapq

from configuration.folders import base_folder
from configuration.vanilla import VanillaConfiguration
from utils.helper_methods import check_spawn_ratios

all_country_dict = {}
country_coordinates = "../data/raw/country_coordinates.csv"
caravan_camper_sales = "../data/raw/caravan_camper_sales.csv"


class Country:
    def __init__(self, name, iso_code, lat, lon):
        self.name = name
        self.iso_code = iso_code
        self.latitude = lat
        self.longitude = lon

    # haversine
    def distance_to(self, other):
        earth_radius = 6371  # kilometers
        theta1 = math.radians(self.latitude)
        theta2 = math.radians(other.latitude)
        delta_lat = math.radians(other.latitude - self.latitude)
        delta_lon = math.radians(other.longitude - self.longitude)

        a = math.sin(delta_lat / 2) * math.sin(delta_lat / 2) + \
            math.cos(theta1) * math.cos(theta2) * \
            math.sin(delta_lon / 2) * math.sin(delta_lon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return earth_radius * c


# code from: https://github.com/mlschneid/country-distance/blob/master/distance.py
def read_coordinates(filename):
    with open(filename, 'r') as f:
        countries = csv.reader(f, delimiter=',', quotechar='|')
        next(countries, None)  # skip header
        for alpha, lat, lon, name in countries:
            identifier = name.lower()
            if len(lat) > 0 and len(lon) > 0:
                all_country_dict[identifier] = Country(identifier, alpha, float(lat), float(lon))


def read_caravan_camper_sales(filename):
    caravan_sales_list = []
    camper_sales_list = []
    with open(filename, 'r') as f:
        sales = csv.reader(f, delimiter=',', quotechar='|')
        for country, caravan_sales, camper_sales in sales:
            caravan_sales_list.append((country, float(caravan_sales)))
            camper_sales_list.append((country, float(camper_sales)))
    return caravan_sales_list, camper_sales_list


def calculate_distance(name_a, name_b):
    country_a = all_country_dict[name_a]
    country_b = all_country_dict[name_b]
    return country_a.distance_to(country_b)


def get_nearest_neighbours(countries, name_a, num_neighbours=10):
    min_heap = []
    for name_b in countries:
        if name_b != name_a:
            distance = calculate_distance(name_a, name_b)
            heapq.heappush(min_heap, (-distance, name_b))
            if len(min_heap) > num_neighbours:
                heapq.heappop(min_heap)
    # return 1/distance to allow for easier processing
    closest_countries = [(name, -1 / distance) for distance, name in min_heap]
    closest_countries.sort(key=lambda x: x[1], reverse=True)
    return closest_countries


def get_country_dict(search_folders):
    country_dict = {}
    abbreviations = set()
    for folder in search_folders:
        country_src_dir = os.path.join(folder, "def\\country")
        for filename in os.listdir(country_src_dir):
            f = os.path.join(country_src_dir, filename)
            if os.path.isfile(f):
                country_name = filename.split(".")[0]
                with open(f, encoding="utf8") as opened:
                    for line in opened:
                        if "country_code:" in line:
                            abbreviation = line.split("\"")[1].lower()
                            if country_name not in country_dict and country_name != "x_land":
                                if abbreviation in abbreviations:
                                    abbreviation += "_"
                                abbreviations.add(abbreviation)
                                country_dict[country_name] = abbreviation
                            break
    return country_dict


def calculate_avg(value_1, value_2, weight_1=0.5, weight_2=0.5):
    return round(value_1 * weight_1 + value_2 * weight_2, 2)


def calculate_shares(weight_factor, fraction=1.0):
    shares = []
    total_distance = sum(entry[1] for entry in weight_factor)
    for country, inv_dist in weight_factor:
        shares.append((country, round(inv_dist / total_distance * fraction, 2)))
    return shares


def get_country_value(tuple_list, name):
    for spawn_rate in tuple_list:
        if spawn_rate[0] == name:
            return spawn_rate[1]
    return 0.0


def create_van_spawn_config(car_spawn_config, truck_spawn_config):
    van_spawn_config = {}
    # average of car and truck spawn rates
    for country in car_spawn_config.keys():
        spawn_config = van_spawn_config[country] = {}
        car_country = car_spawn_config[country]
        truck_country = truck_spawn_config[country]
        spawn_config["national"] = calculate_avg(car_country["national"], truck_country["national"])
        spawn_config["international"] = []
        spawn_config["random"] = calculate_avg(car_country["random"], truck_country["random"])

        spawn_sum = 0
        for foreign_country in car_spawn_config.keys():
            spawn_rate = calculate_avg(get_country_value(car_country["international"], foreign_country),
                                       get_country_value(truck_country["international"], foreign_country))
            if spawn_rate > 0:
                spawn_config["international"].append((foreign_country, spawn_rate))
                spawn_sum += spawn_rate

            correct_spawn_rates(spawn_config, spawn_sum)

    return van_spawn_config


def create_bus_spawn_config(country_dict):
    bus_spawn_config = {}
    # 70% national
    # 25% taken from distance weighted 10 nearest countries
    # 5% random
    for country in country_dict.keys():
        spawn_config = bus_spawn_config[country] = {}
        spawn_config["national"] = 0.70
        spawn_config["random"] = 0.05
        spawn_config["international"] = []
        neighbour_shares = calculate_shares(get_nearest_neighbours(country_dict.keys(), country), 0.25)
        spawn_sum = 0
        for entry in neighbour_shares:
            spawn_config["international"].append(entry)
            spawn_sum += entry[1]
        correct_spawn_rates(spawn_config, spawn_sum)
    return bus_spawn_config


def create_camper_caravan_spawn_config(car_spawn_config, sales_list):
    res_spawn_config = {}
    # 40% national
    # 40% taken from top 15 countries, weighted by (60% of total sales, 40% distance)
    # 15% taken from car configs
    # 5% random
    for country in car_spawn_config.keys():
        spawn_config = res_spawn_config[country] = {}
        spawn_config["national"] = 0.40
        spawn_config["random"] = 0.05
        spawn_config["international"] = []
        filtered_sales = [entry for entry in sales_list if entry[0] != country]
        camper_sales_countries = [entry[0] for entry in filtered_sales]
        sale_shares = dict(calculate_shares(filtered_sales, 0.40))
        distance_shares = dict(calculate_shares(get_nearest_neighbours(camper_sales_countries, country, 15), 0.40))

        spawn_sum = 0
        whitelist = []
        for foreign_country in sale_shares.keys():
            total_share = round(sale_shares[foreign_country] * 0.6 + distance_shares[foreign_country] * 0.4, 2)
            if total_share > 0:
                spawn_config["international"].append((foreign_country, total_share))
                spawn_sum += total_share
            else:
                whitelist.append(foreign_country)

        # only consider car_config countries that have not yet been included in camper_sales, or had 0 spawn rate
        car_config_shares = calculate_shares([entry for entry in car_spawn_config[country]["international"] if entry[0] not in camper_sales_countries or entry[0] in whitelist], 0.15)
        for entry in car_config_shares:
            spawn_config["international"].append(entry)
            spawn_sum += entry[1]

        correct_spawn_rates(spawn_config, spawn_sum)

    return res_spawn_config


def correct_spawn_rates(spawn_config, spawn_sum):
    total_spawn = spawn_config["national"] + spawn_config["random"] + spawn_sum
    if total_spawn != 1.0:
        spawn_config["random"] = round(1.0 - spawn_sum - spawn_config["national"], 2)


def print_spawn_config(spawn_config):
    print("{")
    for key in spawn_config.keys():
        print(f"\t\"{key}\": {{")
        print(f"\t\t\"national\": {spawn_config[key]['national']},")
        international_string = str(spawn_config[key]['international']).replace('\'', '\"')
        print(f"\t\t\"international\": {international_string},")
        print(f"\t\t\"random\": {spawn_config[key]['random']},")
        print("\t},")
    print("}")


config = VanillaConfiguration()
search_folders = [base_folder]

read_coordinates(country_coordinates)
caravan_sales, camper_sales = read_caravan_camper_sales(caravan_camper_sales)
country_dict = get_country_dict(search_folders)

created_config = create_bus_spawn_config(country_dict)
# created_config = create_van_spawn_config(config.car_spawn_config, config.truck_spawn_config)
# created_config = create_camper_caravan_spawn_config(config.car_spawn_config, camper_sales)
# created_config = create_camper_caravan_spawn_config(config.car_spawn_config, caravan_sales)

check_spawn_ratios(created_config, country_dict)
print_spawn_config(created_config)
