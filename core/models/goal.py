from core.models.task import Task
from datetime import datetime


class Goal:
    def __init__(self, name):
        self._index = None
        self._name = name
        self._due_date = None
        self._tasks = []



