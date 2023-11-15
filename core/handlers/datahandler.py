import yaml
from yaml.loader import FullLoader
from functools import reduce


class DataHandler:
    data_path = 'data/sample.yaml'

    @staticmethod
    def update_goal(username, goal):
        with open(DataHandler.data_path, 'r') as f:
            data = yaml.load(f, FullLoader)

        # seq =
        reduce(data.__setitem__, [])

    @staticmethod
    def get_goals(username):
        with open(DataHandler.data_path, 'r') as f:
            data = yaml.load(f, FullLoader)
        return data[username]

    @staticmethod
    def load_data(self):
        with open(self.data_path, 'r') as f:
            data = yaml.load(f, FullLoader)
        return data

    @staticmethod
    def write_data(self, data):
        with open(DataHandler.data_path, 'w') as f:
            yaml.dump(data, f)
