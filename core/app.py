import core.window
from core.utils.createdirs import get_dirs
from core.utils.createdirs import prepare_dirs
from core.utils.createdirs import prepare_locales


class App:
    def __init__(self):
        get_dirs()
        prepare_dirs()
        prepare_locales()
        self.window = core.window.Window()

    def run(self):
        self.window.mainloop()
