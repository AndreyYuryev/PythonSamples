import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        s = ttk.Style()
        s.theme_use(themename='clam')

    def close(self):
        self.destroy()


class ProgramWindow(Window):
    def __init__(self, title, config, credential, request, double_check):
        super().__init__(title=title)
        self.geometry('300x300+300+300')
        self.config = config
        self.credential = credential
        self.request = request
        self.double_check = double_check

    def run(self):
        self.ask_username()
        if self.config.is_exist_username() is True:
            self.disable_username()
        self.credential.get_credential()
        self.ask_credential()
        if self.credential.is_exist() is True:
            self.disable_credential()
            self.ask_cd_number()

    def ask_username(self):
        self.login_text = ttk.Label(self, text="Please set Username")
        self.login_text.grid(column=1, row=0)
        self.label_login = ttk.Label(self, text="Username")
        self.label_login.grid(column=0, row=1)
        self.login_entry = ttk.Entry(self, width=30)
        self.login_entry.grid(column=1, row=1)
        self.btn_reg = ttk.Button(self, text="Set Username", command=self.set_username)
        self.btn_reg.grid(column=1, row=2)

    def ask_credential(self):
        self.credential_text = ttk.Label(self, text="Please set credential")
        self.credential_text.grid(column=1, row=3)
        self.label_login = ttk.Label(self, text="Login")
        self.label_login.grid(column=0, row=4)
        self.login_entry = ttk.Entry(self, width=30)
        #login, password = self.credential.get_credential()
        self.login_entry.insert(0, self.config.username)
        self.login_entry.configure(state='disabled')
        self.login_entry.grid(column=1, row=4)
        self.label_pswd = ttk.Label(self, text="Password")
        self.label_pswd.grid(column=0, row=5)
        self.pswd_entry = ttk.Entry(self, width=30, show="*")
        self.pswd_entry.grid(column=1, row=5)
        self.btn_cred = ttk.Button(self, text="Save credential", command=self.set_credential)
        self.btn_cred.grid(column=1, row=6)

    def ask_cd_number(self):
        self.cd_text = ttk.Label(self, text="Please set CD number")
        self.cd_text.grid(column=1, row=7)
        self.label_cd = ttk.Label(self, text="CD number")
        self.label_cd.grid(column=0, row=8)
        self.cd_entry = ttk.Entry(self, width=30)
        self.cd_entry.grid(column=1, row=8)
        self.btn_cd = ttk.Button(self, text="Set number", command=self.set_cd)
        self.btn_cd.grid(column=1, row=9)

    def ask_close(self):
        self.btn_exit = ttk.Button(self, text="Exit", command=self.exit)
        self.btn_exit.grid(column=1, row=10)

    def set_username(self):
        self.config.set_config(self.login_entry.get())
        self.disable_username()

    def set_credential(self):
        self.credential.save(self.pswd_entry.get())
        self.disable_credential()
        self.ask_cd_number()

    def set_cd(self):
        self.request.number = self.cd_entry.get()
        if self.request.is_exist() is True:
            self.disable_cd()
            self.ask_close()
            self.double_check.browser()
            self.double_check.login(username=str(self.config.username), password=str(self.credential.password))
            self.double_check.skip_pro()
            self.double_check.select_request(cd_number=self.request.number)
            self.double_check.check()

    def disable_username(self):
        self.login_entry.insert(0, self.config.username)
        self.login_entry.configure(state='disabled')
        self.btn_reg.configure(state='disabled')

    def disable_credential(self):
        self.pswd_entry.insert(0, str(self.credential.password))
        self.pswd_entry.configure(state='disabled')
        self.btn_cred.configure(state='disabled')

    def disable_cd(self):
        self.pswd_entry.insert(0, str(self.request.number))
        self.cd_entry.configure(state='disabled')
        self.btn_cd.configure(state='disabled')

    def exit(self):
        self.double_check.close_double()
        self.close()