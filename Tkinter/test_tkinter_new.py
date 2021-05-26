import tkinter as tk


class Window(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)

    def close(self):
        self.destroy()



class App(Window):
    def __init__(self, title):
        super().__init__(title)

        self.btn = tk.Button(self, text="Нажми!",
                             command=self.say_hello)
        self.btn.pack(padx=120, pady=30)

    def say_hello(self):
        print("Привет, Tkinter!")
        self.btn.configure(state='disabled')
        self.login_entry = tk.Entry(self, width=30)
        self.login_entry.pack()
        self.btn1 = tk.Button(self, text="Нажми!",
                             command=self.say_hello1)
        self.btn1.pack(padx=120, pady=30)

    def say_hello1(self):
        self.login_entry.configure(state='disabled')
        self.btn1.configure(state='disabled')
        self.btn1 = tk.Button(self, text="Нажми!",
                             command=self.say_hello2)
        self.btn1.pack(padx=120, pady=30)

    def say_hello2(self):
        self.close()



def main():
    app = App(title="Приложение на Tkinter 2")
    app.mainloop()


if __name__ == "__main__":
    #main(True)
    main()

