import tkinter as tk
from tkinter import messagebox
import pickle






Window = tk.Tk()
Window.geometry('400x250')
Window.title("Login in system")


def registration(win):
    welcome_text = tk.Label(win, text="Please log on to system")
    welcome_text.grid(column=1, row=0)
    label_login = tk.Label(win, text="Login")
    label_login.grid(column=0, row=1)
    login_entry = tk.Entry(win, width=30)
    login_entry.grid(column=1, row=1)
    label_pswd = tk.Label(win, text="Password")
    label_pswd.grid(column=0, row=2)
    pswd_entry = tk.Entry(win, width=30, show="*")
    pswd_entry.grid(column=1, row=2)
    btn_reg = tk.Button(win, text="Register", command=lambda: save())
    btn_reg.grid(column=1, row=3)

    def save():
        login_pass_save = {}
        login_pass_save[login_entry.get()] = pswd_entry.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()

def execute_check(win):
    welcome_text = tk.Label(win, text="Please set CD number")
    welcome_text.grid(column=1, row=0)
    cd_number = tk.Label(win, text="Login")
    cd_number.grid(column=0, row=1)
    cd_entry = tk.Entry(win, width=10)
    cd_entry.grid(column=1, row=1)
    btn_exe = tk.Button(win, text="Execute")
    btn_exe.grid(column=1, row=2)

registration(Window)
#execute_check(Window)


Window.mainloop()