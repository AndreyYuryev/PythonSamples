from tkinter import *
from tkinter.filedialog import *
import fileinput


def _open():
    op = askopenfilename()
    for i in fileinput.input(op):
        txt.insert(END, i)

def _save():
    sa = asksaveasfilename()
    letter = txt.get(1.0, END)
    f = open(sa, "w")
    f.write(letter)
    f.close()

root = Tk()
m = Menu(root)
root.config(menu=m)

fm = Menu(m)
m.add_cascade(label="File", menu=fm)
fm.add_command(label="Open...", command=_open)
fm.add_command(label="Save", command=_save)

txt = Text(root, width=120, height=15, font="12")
txt.pack()

root.mainloop()