import tkinter as tk


class Window(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)

    def close(self):
        self.destroy()


class Username(Window):
    def __init__(self, title, config):
        super().__init__(title)
        self.geometry('300x100+300+300')
        self.login_entry = str()
        self.config = config

    def start(self):
        welcome_text = tk.Label(self, text="Please set Username")
        welcome_text.grid(column=1, row=0)
        label_login = tk.Label(self, text="Username")
        label_login.grid(column=0, row=1)
        self.login_entry = tk.Entry(self, width=30)
        self.login_entry.grid(column=1, row=1)
        btn_reg = tk.Button(self, text="Set Username", command=self.save)
        btn_reg.grid(column=1, row=3)
        self.mainloop()

    def save(self):
        self.config.username = self.login_entry.get()
        self.close()


class Login(Window):
    def __init__(self, title, credential):
        super().__init__(title)
        self.geometry('300x100+300+300')
        self.credential = credential
        self.login_entry = str()
        self.pswd_entry = str()

    def start(self):
        welcome_text = tk.Label(self, text="Please set credential")
        welcome_text.grid(column=1, row=0)
        label_login = tk.Label(self, text="Login")
        label_login.grid(column=0, row=1)
        self.login_entry = tk.Entry(self, width=30)
        self.login_entry.insert(0, self.credential.login)
        self.login_entry.configure(state='disabled')
        self.login_entry.grid(column=1, row=1)
        label_pswd = tk.Label(self, text="Password")
        label_pswd.grid(column=0, row=2)
        self.pswd_entry = tk.Entry(self, width=30, show="*")
        self.pswd_entry.grid(column=1, row=2)
        btn_reg = tk.Button(self, text="Save credential", command=self.save)
        btn_reg.grid(column=1, row=3)
        self.mainloop()

    def save(self):
        self.credential.login = self.login_entry.get()
        print("credential", self.credential.login)
        self.credential.password = self.pswd_entry.get()
        self.credential.save()
        self.close()


class CD_number(Window):
    def __init__(self, title, request):
        super().__init__(title)
        self.geometry('300x100+300+300')
        self.cd_entry = str()
        self.request = request

    def start(self):
        welcome_text = tk.Label(self, text="Please set CD number")
        welcome_text.grid(column=1, row=0)
        label_login = tk.Label(self, text="CD number")
        label_login.grid(column=0, row=1)
        self.cd_entry = tk.Entry(self, width=30)
        self.cd_entry.grid(column=1, row=1)
        btn_reg = tk.Button(self, text="Set number", command=self.save)
        btn_reg.grid(column=1, row=3)
        self.mainloop()

    def save(self):
        self.request.number = self.cd_entry.get()
        self.close()


class Close_app(Window):
    def __init__(self, title):
        super().__init__(title)
        self.geometry('300x100+300+300')

    def start(self):
        btn_reg = tk.Button(self, text="Exit", command=self.close())
        btn_reg.grid(column=1, row=3)
        self.mainloop()