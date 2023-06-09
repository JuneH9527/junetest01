import tkinter as tk

# TODO:
class WindowHandler(object):
    def __init__(self, title='window'):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry("{}x{}+{}+{}".format(600, 400, 400, 200))

    def create_window(self):
        self.window.mainloop()

    def add_inputbox(self):
        pass

    def add_button(self):
        pass


if __name__ == '__main__':
    wh = WindowHandler()
    wh.create_window()
