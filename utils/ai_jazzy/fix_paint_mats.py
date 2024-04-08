import os

src_folder = "C:\\Users\\Matth\\Desktop\\AI Traffic Pack by Jazzycat"
dst_folder = "C:\\Users\\Matth\\Desktop\\Jazzycat Matfix"

for root, _, files in os.walk(src_folder):
    for file in files:
        if file.endswith(".mat"):
            src_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, src_folder)
            change_mat = False
            with open(src_file_path, "r") as src_file:
                updated_data = []
                for line in src_file:
                    if "material : " in line or "material:" in line:
                        if ".paint" in line or ".truckpaint" in line:
                            change_mat = True
                            updated_data.append(line)
                        else:
                            break
                    elif "shininess" in line and change_mat:
                        updated_data.append("\tshininess : 250\n")
                    else:
                        updated_data.append(line)
            if change_mat:
                dst_root_path = os.path.join(dst_folder, relative_path)
                if not os.path.exists(dst_root_path):
                    os.makedirs(dst_root_path)
                dst_file_path = os.path.join(dst_root_path, file)
                with open(dst_file_path, "w") as dst_file:
                    dst_file.writelines(updated_data)
