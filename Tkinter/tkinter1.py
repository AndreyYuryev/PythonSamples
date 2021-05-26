from tkinter import *


class ButtonPrint:
    def __init__(self):
        self.but = Button(root)
        self.but["text"] = "Print"
        self.but.bind("<Button-1>", self.print)
        self.but.pack()

    def print(self, event):
        print("hello World")


root = Tk()
obj = ButtonPrint()
root.mainloop()
