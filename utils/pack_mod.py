import subprocess

# Path to mod folder
mod_src_folder = r"YOUR_MOD_SRC_FOLDER"

# Mod destination folder
mod_dst_folder = r"YOUR_MOD_DST_FOLDER"

# Archive name
archive_name = r"\YOUR_MOD_NAME.scs"

# Path to executable
exe_path = "scs_packer.exe"

# Arguments for the command
args = ["create", mod_dst_folder + archive_name, "-root", mod_src_folder]

# Combine the executable path and the arguments into a single list
command = [exe_path] + args

# Run the command
result = subprocess.run(command, capture_output=True, text=True)

# Print the output
if result.returncode == 0:
    print(f"Successfully packed mod and exported it to folder: {mod_dst_folder}")
else:
    print("An error occurred! ")
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
