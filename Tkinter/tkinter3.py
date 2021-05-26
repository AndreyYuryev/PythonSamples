from tkinter import *

root = Tk()
fra1 = Frame(root, width=500, height=100, bg="darkred")
fra2 = Frame(root, width=300, height=200, bg="green", bd=20)
fra3 = Frame(root, width=500, height=150, bg="darkblue")

fra1.pack()
fra2.pack()
fra3.pack()

ent1 = Entry(fra2, width=20)
ent1.pack()

sca1 = Scale(fra3, orient=HORIZONTAL, length=300, from_=0, to=100, tickinterval=10, resolution=5)
sca2 = Scale(root, orient=VERTICAL, length=400, from_=1, to=2, tickinterval=0.1, resolution=0.1)
sca1.pack()
sca2.pack()

root.mainloop()