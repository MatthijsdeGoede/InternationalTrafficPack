
from configuration.ai_jazzy import ban_list, car_list

traffic_storage_file = "YOUR_PATH\\traffic_storage_car.jazzycat_ai.sii"

banned_cars = set(ban_list)
existing_vehicles = set(car_list)
found_vehicles = set()


def analyze():
    with open(traffic_storage_file, "r", encoding="utf-8") as src:
        for line in src:
            if "@include" not in line:
                continue
            else:
                vehicle = line.split("\"ai/")[1].split(".sui\"")[0].replace("/", "\\")
                found_vehicles.add(vehicle)

    new_vehicles = found_vehicles.difference(existing_vehicles).difference(banned_cars)
    new_vehicles = list(new_vehicles)
    new_vehicles.sort()
    print(f"Found {len(new_vehicles)} new vehicles: \n")
    for new_vehicle in new_vehicles:
        new_vehicle = new_vehicle.replace("\\", "\\\\")
        print(f"\"{new_vehicle}\",")

    removed_vehicles = existing_vehicles.difference(found_vehicles).difference(banned_cars)
    removed_vehicles = list(removed_vehicles)
    removed_vehicles.sort()
    if len(removed_vehicles) > 0:
        print(f"Found {len(removed_vehicles)} removed vehicles: \n")
        for removed_vehicle in removed_vehicles:
            removed_vehicle = removed_vehicle.replace("\\", "\\\\")
            print(f"\"{removed_vehicle}\",")


# analyze()


def sort(collection):
    collection.sort()
    for vehicle in collection:
        vehicle = vehicle.replace("\\", "\\\\")
        print(f"\"{vehicle}\",")

# sort(ban_list)
analyze()