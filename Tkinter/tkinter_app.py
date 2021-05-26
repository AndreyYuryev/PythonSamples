import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.btn = ttk.Button(self, text="Нажми!",
                             command=self.say_hello)
        self.btn.pack(padx=120, pady=30)
        self.btn = tk.Button(self, text="Нажми!",
                             command=self.say_hello)
        self.btn.pack(padx=120, pady=30)

        self.extra_window = tk.Toplevel(self)
        self.btn1 = tk.Button(self.extra_window, text="Нажми!",
                             command=self.say_hello1)
        self.btn1.pack(padx=120, pady=30)

    def say_hello(self):
        print("Привет, Tkinter!")

    def say_hello1(self):
        print("Привет, Tkinter 1!")

if __name__ == "__main__":
    app = App(title="Приложение на Tkinter")
    app.mainloop()