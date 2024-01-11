#!bin/python3
#Capital() is a class, Small() is a method

import tkinter as tk
import os
import sys

main = tk.Tk()
main.title("Unsatisfied_World")

window_width = 600
window_height = 400

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

main.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

#main.resizable(0,0)
#main.attributes('-alpha',0.2)
#main.attributes("-topmost",1)
main.iconbitmap(r"icon.ico")
message = tk.Label(main,text="Hello UnsatisfiedSoul")
message.pack()
main.mainloop()
