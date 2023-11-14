import tkinter as tk
from core.widgets import MainWindow


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('test')
        self.geometry('800x600')
        self.update()

        self.main_window = MainWindow(self)
        self.main_window.pack(
            expand=True,
            fill=tk.BOTH
        )

    @property
    def root_geometry(self):
        return self.winfo_width(), self.winfo_height()

    def run(self):
        self.mainloop()













# def create_page(page: ft.Page):
#     page.title = 'Test'
#
#     page.theme = Theme.theme
#     page.theme_mode = Theme.mode
#
#     page.window_width = 800
#     page.window_height = 600
#
#     app = AppView(page)
#
#     page.add(app)
#     page.update()
#
#
# def run_app():
#     ft.app(create_page)
