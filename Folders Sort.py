import shutil
from pathlib import Path

import customtkinter as ctk
from PIL import Image

root = ctk.CTk()

root.geometry("600x600")
root.title("Folders to Folders")

DESKTOP = Path.home() / "Desktop"

def replace_Images():
    raw_dir = entry1.get().strip().replace('"', '')
    raws_dir = entry2.get().strip().replace('"', '')

    target_dir = Path(raw_dir) if Path(raw_dir).is_absolute() else DESKTOP / raws_dir
    source_dir = Path(raws_dir) if Path(raws_dir).is_absolute() else DESKTOP / raw_dir

    if not source_dir.exists() or not source_dir.is_dir():
        print("netu takoi")
        return

    target_dir.mkdir(parents=True, exist_ok=True)
    
    for item in source_dir.rglob("*"):
        if item.is_file():
            dest = target_dir / item.name
            shutil.move(item, dest)
            

label = ctk.CTkLabel(root, text="Folders to Folders", font=("Arial", 50, "bold")).place(x=110, y=10)

label1 = ctk.CTkLabel(root, text="Entry Your First Folder: ", font=("Arial", 25, "bold")).place(x=160, y=90)

entry1 = ctk.CTkEntry(root, width=350,height=40, font=("Arial", 30, "bold"))
entry1.place(x=130, y= 140)

label2 = ctk.CTkLabel(root, text="Entry Your Second Folder: ", font=("Arial", 25, "bold")).place(x=150, y=195)

entry2 = ctk.CTkEntry(root, width=350,height=40, font=("Arial", 30, "bold"))
entry2.place(x=130, y=240)

button1 = ctk.CTkButton(root, width=400, height=30, font=("Arial", 40, "bold"), text="Replace", command = replace_Images)
button1.place(x=110, y=310)

icon_image = ctk.CTkImage(light_image=Image.open("Explorer.png"), size=(500, 200))

image_label = ctk.CTkLabel(root, image=icon_image, text="")
image_label.place(x=55, y=385)

root.mainloop()


