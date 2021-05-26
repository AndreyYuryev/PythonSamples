from tkinter import *


root = Tk()
v = StringVar()
ent1 = Entry (root, textvariable = v,bg="black",fg="white")
ent2 = Entry(root, textvariable = v)
ent1.pack()
ent2.pack()
root.mainloop()