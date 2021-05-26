from tkinter import *
from tkinter.messagebox import *

def close_win():
    if askyesno("Exit", "Do you want to quie?"):
        root.destroy()


def about():
    showinfo("Editor", "This is text editor.\n(test version)")

root = Tk()
m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label="Help", menu=fm)
fm.add_command(label="Exit", command=close_win)
fm.add_command(label="About", command=about)

txt = Text(root, width=120, height=15, font="12")
txt.pack()

root.mainloop()