import random
import sys

import customtkinter as ctk

question = int(input("How much cubes towards X (Tipp: I wouldn't recommend taking more than fifty): "))
question1 = int(input("How much cubes towards Y (Tipp: I wouldn't recommend taking more than fifty): "))

root = ctk.CTk()

root.geometry("300x300")
root.resizable(False, False)
root.configure(fg_color="black")

colors = ["#eb4034", "#49eb34", "#3437eb", "#e8eb34", "#eb7a34", "#e632ad", "#7a32e6", "#32e6c5"]
cubes = []
presed_cubes = 0

def black_niper(btn):

    choise = random.choice(colors)
    btn.configure(fg_color=choise)

    white_button = [c for c in cubes if c.cget("fg_color") == "white"]

    if len(white_button) == 0:
        for c in cubes:
            c.configure(fg_color="white")

try:
    for i in range(question):
        for x in range(question1):
            cube = ctk.CTkButton(root, width = 26, height = 26, bg_color="black", text="", fg_color="white", hover_color="black")
            cube.configure(command=lambda current_btn=cube: black_niper(current_btn))
            cube.grid(row=i,column=x,pady=2, padx=2)

        cubes.append(cube)
except KeyboardInterrupt:
    print("Ti eblan?")
    sys.exit()
    
root.mainloop()