import os

folder = "YOUR_PATH_TO_JAZZYCAT_AI\\def\\vehicle\\ai"

for root, directories, files in os.walk(folder):
    for file in files:
        if file.endswith(".sui"):
            file_path = os.path.join(root, file)
            updated_data = []
            with open(file_path, "r") as src:
                data = src.readlines()
                name = None
                for line in data:
                    if "traffic_vehicle" in line:
                        name = line.split("traffic.")[1].strip()
                        updated_data.append(line)
                    elif "traffic_trailer" in line:
                        updated_data = data
                        break
                    elif "accessories[]:" in line or "vehicle_accessory" in line or "vehicle_wheel_accessory" in line:
                        to_replace = line.split(".")[1]
                        line = line.replace(to_replace, name)
                        updated_data.append(line)
                    else:
                        updated_data.append(line)

            with open(file_path, "w") as dst:
                dst.writelines(updated_data)
