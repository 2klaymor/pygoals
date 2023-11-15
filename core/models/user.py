from core.models.goal import Goal


class User:
    def __init__(self, username):
        self._username = username
        self._goals = []
