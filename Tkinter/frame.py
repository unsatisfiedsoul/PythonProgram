#!/bin/python3

import tkinter as tk
from tkinter import ttk

main = tk.Tk()
main.title("Apps")
main.geometry("600x400")
main.config(bg="#879685")

mainFrame = ttk.Frame(main)
mainFrame.pack(anchor="center",expand=True)

loginFrame = ttk.LabelFrame(mainFrame,text="Login Credentials",padding=20)
loginFrame.grid(row=0,column=0)


userNameLabel = ttk.Label(loginFrame,text="Username: ",padding=20)
userNameEntry = ttk.Entry(loginFrame,width=50)
passWordLabel = ttk.Label(loginFrame,text="Password: ",padding=20)
passWordEntry = ttk.Entry(loginFrame,width=50,show="*")

buttonFrame = ttk.Frame(mainFrame)
buttonFrame.grid(row=1,column=0)

loginButton = ttk.Button(buttonFrame,text="Login")
regiButton = ttk.Button(buttonFrame,text="Registration")


userNameLabel.grid(row=0,column=0)
userNameEntry.grid(row=0,column=1)
passWordLabel.grid(row=1,column=0)
passWordEntry.grid(row=1,column=1)

loginButton.grid(row=0,column=0,padx=20,pady=10)
regiButton.grid(row=0,column=1,padx=20,pady=10)

main.mainloop()
