from core.ui import AppWindow
from core.handlers import DataHandler


class App:
    def __init__(self):
        self.app_window = AppWindow()

    def run(self):
        self.app_window.launch()







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
