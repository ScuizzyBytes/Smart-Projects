import pyautogui
import os
import customtkinter as ctk
from PIL import Image

root = ctk.CTk()

root.geometry("400x400")
root.title("Screenshoter")


def make_screenshot():
    pyautogui.screenshot("fullscreen.png")
    os.startfile("fullscreen.png")


label = ctk.CTkLabel(root, text="Screenshoter", width= 300, height= 70, font= ("Arial", 35, "bold")).place(x= 55, y= 20)

button1 = ctk.CTkButton(root, text="Make Screenshot", font=("Arial", 30, "bold"), width=250, height=60, command= make_screenshot)
button1.place(x= 75, y= 250)

root.mainloop()