import tkinter as tk


class ApplicationLeft(tk.Frame):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.set_widgets_left()

    def set_widgets_left(self):
        # Create widget
        self.login_entry = tk.Entry(self, width=30)
        self.login_entry.pack()



class ApplicationRight(tk.Frame):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.set_widgets_right()

    def set_widgets_right(self):
        # Create widget
        self.login_entry = tk.Entry(self, width=30)
        self.login_entry.pack()


if __name__ == '__main__':
    root_left = tk.Tk()
    root_left.title("Левый")
    root_left.geometry("600x650")

    root_right = tk.Toplevel()
    root_right.title("Правый")
    root_right.geometry("600x650")

    app_left = ApplicationLeft(root_left)
    app_right = ApplicationRight(root_right)
    app_left.mainloop()
