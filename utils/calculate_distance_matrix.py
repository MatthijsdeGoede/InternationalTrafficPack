import csv
import pandas as pd
import math
from configuration.promods import car_spawn_config

country_dict = {}
file_path = "../data/raw/country_distances.csv"

# code from: https://github.com/mlschneid/country-distance/blob/master/distance.py
def read_file(filename):
    with open(filename, 'r') as f:
        countries = csv.reader(f, delimiter=',', quotechar='|')
        next(countries, None)  # skip header
        for alpha, lat, lon, fname in countries:
            if (len(lat) > 0 and len(lon) > 0):
                country_dict[fname] = Country(fname, alpha, float(lat), float(lon))


def print_standard():
    for countryA in country_dict.values():
        for countryB in country_dict.values():
            print(Distance(countryA, countryB, countryA.distanceTo(countryB)))


class Distance():
    def __init__(self, countryA, countryB, distance_km):
        self.countryA = countryA
        self.countryB = countryB
        self.distance_km = distance_km

    def __str__(self):
        return ", ".join([self.countryA.fname, self.countryB.fname, str(self.distance_km)])


class Country():
    def __init__(self, fname, iso_code, lat, lon):
        self.fname = fname
        self.iso_code = iso_code
        self.latitude = lat
        self.longitude = lon

    # haversine
    def distanceTo(self, otherCountry):
        earth_radius = 6371  # kilometers
        theta1 = math.radians(self.latitude)
        theta2 = math.radians(otherCountry.latitude)
        delta_lat = math.radians(otherCountry.latitude - self.latitude)
        delta_lon = math.radians(otherCountry.longitude - self.longitude)

        a = math.sin(delta_lat / 2) * math.sin(delta_lat / 2) + \
            math.cos(theta1) * math.cos(theta2) * \
            math.sin(delta_lon / 2) * math.sin(delta_lon / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return earth_radius * c


def calculate_distance_matrix():
    for country_name in car_spawn_config.keys():
        capitalized = country_name.capitalize()
        if capitalized in country_dict.keys():
            print("jaja is goed")
        else:
            print(capitalized)

read_file(file_path)
calculate_distance_matrix()


