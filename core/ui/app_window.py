import tkinter as tk
from core.ui.pages.main_page import MainPage


class AppWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('test')
        self.geometry('800x600')
        self.resizable(False, False)
        self.update()

        self.main_window = MainPage(self)
        self.main_window.pack(
            expand=True,
            fill=tk.BOTH
        )

    def launch(self):
        self.mainloop()