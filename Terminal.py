import os
from tkinter import messagebox

import customtkinter as ctk

WIDTH, HEIGHT = 900, 500

User_name = os.getlogin()

class Terminal(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.title("Terminal QUX")
        self.resizable(False, False)
        self.configure(fg_color="black")
        
        self.labels = []
        self.label_y = 35
        
        self.user = ctk.CTkLabel(self, text=f"PS C:User/ {User_name}: ", font=("Arial", 20,"bold"), text_color="gray")
        self.user.place(x=5, y=10)
        
        self.command = ctk.CTkEntry(self, font=("Arial", 23, "bold"), width=600, height=10, fg_color="transparent", border_width=0, text_color="yellow")
        self.command.place(x=185, y=8)
        self.command.pack_forget()
        self.command.bind("<Return>", self.function_commnads)
        
        self.function_commnads()
        
    def function_commnads(self, event=None):
        commands = self.command.get().strip()

        if commands.startswith("mkdir"):
            foldername = commands[6:].strip()
            
            if foldername:
                base_path = f"C:Users\\{User_name}\\Desktop"
        
                full_path = os.path.join(base_path, foldername)        
        
                try:
                    os.makedirs(full_path, exist_ok=True)
                    print("Folder Has been Created!")
                    self.command.delete(0, "end")
                except Exception as e:  # noqa: BLE001
                    print(f"Error {e}")
        
        if commands.startswith("echo"):
            name_input = commands[4:].strip()
            
            try:
                self.label = ctk.CTkLabel(self, text=name_input, font=("Arial", 30, "bold"))
                self.label.place(x=5, y=self.label_y)
                
                self.labels.append(self.label)
                
                self.label_y += 45
                            
                print(f"{name_input} has been printed!")
                self.command.delete(0, "end")
            except Exception as e:  # noqa: BLE001
                print(f"Error {e}")
                
        if commands.startswith("messagebox "):
            text_messagebox = commands[11:].strip()
            
            if text_messagebox:
                try:
                    messagebox.showerror("Terminal", text_messagebox)
                    print("Message has been created!")
                    self.command.delete(0, "end")
                except Exception as e:  # noqa: BLE001
                    print(f"Error {e}")
        
terminal = Terminal()
terminal.mainloop()
