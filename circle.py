import math
import random
import tkinter as tk

colors = ["#00FF00","#FF1212","#0000FF","#EFFF12", "#21B9FF"]

root = tk.Tk()

root.geometry("400x400")
root.title("math")
root.configure(bg="black")

canvas = tk.Canvas(root, width=400, height=400, bg="black")
canvas.pack(fill="both", expand=True)

lines = 120
radius = 120
center_y, center_x = 200, 200

angle_step = (math.pi * 2) / radius

for i in range(lines):

    random_color = random.choice(colors)

    angle = i * angle_step

    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)

    canvas.create_line(center_x, center_y, x, y, fill=random_color, width=2)

root.mainloop()
