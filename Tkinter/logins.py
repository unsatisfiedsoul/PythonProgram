import tkinter as tk
#from tkinter import messagebox

class MyClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Unsatisfied_world")
        self.root.geometry("600x400")

        self.welcome_label = tk.Label(
                self.root,
                text = "Welcome to the Unsatisfied_world",
                justify = "center",
                fg = "blue",
                font = ("Arial",24)
                )
        self.welcome_label.place(x=230,y=40)
        self.username_label = tk.Label(self.root,
                                       text = "Username: "
                                        )
        self.username_label.place(x=140,y=100)
        self.username_box = tk.Entry(self.root,
                                     bd = 3,
                                     selectbackground = "#e5e3e3")
        self.username_box.place(x=230,y=100)

        def log_inn(self):
            ...

        def register(self):
            ...

if __name__ == "__main__":
    roott = tk.Tk()
    app = MyClass(roott)
    roott.mainloop()

