from core.ui import Window
from core.handlers import DataHandler
from functools import reduce
from operator import getitem


class App:

    _instance = None
    data_path = 'data/data.json'
    data = None

    def __new__(cls):
        if not App._instance:
            App._instance = super().__new__(cls)
        return App._instance

    def __init__(self):
        self.data_handler = DataHandler(self)
        App.data = self.data_handler.load_data()

        self.window = Window(self)

    @classmethod
    def get_data(cls, requested_data):
        if isinstance(requested_data, str):
            requested_data = (requested_data, )
        return reduce(getitem, requested_data, App.data)

    def run(self):
        self.window.launch()
