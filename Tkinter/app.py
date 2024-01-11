#!bin/python3

import tkinter as tk
from tkinter import ttk 
main = tk.Tk()

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

window_width = 600
window_height = 400

center_x = int((screen_width - window_width)/2)
center_y = int((screen_height - window_height)/2)

geometry = main.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

title = main.title("Unsatisfied_World")

photo = tk.PhotoImage(file ="./icon.png" )

label = ttk.Label(main)
label["text"] = "Welcome Welcome Welcome!!!!! To the Unsatisfied_World"
label["font"] = ("Helvatica",14)
label["image"] = photo
label["compound"] = "top"
label.pack()

mainloop = main.mainloop()
