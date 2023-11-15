import json
import os


class DataHandler:
    def __init__(self, app):
        self.app = app
        self.data_path = app.data_path

    @property
    def data_exists(self):
        return os.path.exists(self.data_path)

    def write_data(self, data=None):
        if not data:
            data = self.app.data
        with open(self.data_path, 'w') as d:
            json.dump(data, d)

    def create_data(self):
        self.write_data({})

    def load_data(self):
        if not self.data_exists:
            self.create_data()

        with open(self.data_path, 'r') as d:
            data = json.load(d)

        return data
