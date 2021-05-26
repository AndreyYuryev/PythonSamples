import tkinter as tk
from tkinter import  messagebox as msg


def clicked():
    res = "Привет {}".format(text.get())
    label.configure(text=res)
    info = text.get()
    length_text = len(info)
    text.delete(0, length_text)
    msg.showinfo("GUI Python", info )


def check_clicked():
    msg.showinfo("Checkbutton", checked)


def about_clicked():
    msg.showinfo(title="Menu", message="About clicked")


Window = tk.Tk()
Window.geometry('400x250')
Window.title("hello World")
label = tk.Label(Window, text="Hello!")
label.grid(column=0, row=0)
text = tk.Entry(Window, width=10)
text.grid(column=1, row=0)
button = tk.Button(Window, text="Don`t touch", command=clicked)
button.grid(column=2, row=1)
checked = 1
check_button = tk.Checkbutton(text="checked", variable=checked, command=check_clicked)
check_button.grid(column=1, row=2)

file_menu = tk.Menu(tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Save")

main_menu = tk.Menu()
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="About", command=about_clicked)

Window.configure(menu=main_menu)
Window.mainloop()
