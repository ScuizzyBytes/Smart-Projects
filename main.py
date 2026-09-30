import math
import tkinter as tk
        
root = tk.Tk()
root.title("Animated Circle")

radius = 200
lines =  300

root.geometry(f"{int(radius*2)}x443",)

canvas = tk.Canvas(root, width=radius*2, height=radius*2, bg="black")
canvas.pack(pady=20)

def draw_lines(i=0):
        if i >= lines:
            root.destroy()
            return
        
        angle = (2 * math.pi / lines) * i
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        
        canvas.create_line(radius, radius, radius + x, radius + y, fill="white", width=2)

        canvas.after(1, draw_lines, i + 1)

draw_lines(0)

root.mainloop()

