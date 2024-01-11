#!/bin/python3

import tkinter as tk
from tkinter import ttk

main = tk.Tk()
main.geometry("600x400")
main.title("Menu Bar")
main.config(bg="#98F77D")

menubar = tk.Menu(main)
main.config(menu=menubar)

fileMenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Clear")
fileMenu.add_command(label="Save As")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

helpMenu = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="Precautions")
helpMenu.add_command(label="Version Info")
helpMenu.add_command(label="Technical support")

rows =0
while rows<50:
    main.rowconfigure(rows,weight=1)
    main.columnconfigure(rows,weight=1)
    rows +=1

mainFrame = ttk.Notebook(main,width=50)
mainFrame.grid(row=1,column=2,columnspan=45,rowspan=43,sticky="news")

main.mainloop()
