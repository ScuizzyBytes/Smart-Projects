import os

user = os.getlogin()

folder_name = f"C:\\Users\\{user}\\AppData\\Local\\Roblox"

for filename in os.listdir(folder_name):
    if filename.startswith("GlobalBasicSettings_13") and filename.endswith(".xml"):
        file_path = os.path.join(folder_name, filename)
        
        with open(file_path, "r", encoding="utf-8") as f:
            print(f.read())