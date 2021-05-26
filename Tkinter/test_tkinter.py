import tkinter as tk


class Window(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)

    def close(self):
        self.destroy()



class App1(Window):
    def __init__(self, title):
        super().__init__(title)
        self.btn = tk.Button(self, text="Нажми!",
                             command=self.say_hello)
        self.btn.pack(padx=120, pady=30)

    def say_hello(self):
        print("Привет, Tkinter!")
        self.close()


class App2(Window):
    def __init__(self, title):
        super().__init__(title)
        self.btn = tk.Button(self, text="Нажми!",
                             command=self.say_hello)
        self.btn.pack(padx=120, pady=30)

    def say_hello(self):
        print("Привет, Tkinter!")
        self.close()


def main(condition):
    if condition is False:
        app1 = App1("1 App")
        app1.mainloop()

    app2 = App2("Приложение на Tkinter 2")
    app2.mainloop()


if __name__ == "__main__":
    #main(True)
    main(False)

