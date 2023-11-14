from core.models.task import Task
from datetime import datetime


class Goal:
    def __init__(self, name):
        self._index = None
        self._name = name
        self._due_date = None
        self._tasks = []

    # Get the Task Object
    def task(self, task_index):
        return self._tasks[task_index]

    # Create new Task object and append it in the list of tasks
    def new_task(self, task_text):
        task = Task(task_text)
        task.index = len(self._tasks)
        self._tasks.append(task)

    # Removes task
    def remove_task(self, task_index):
        self._tasks.pop(task_index)

    # Swaps two tasks inplace
    def switch_tasks(self, task_index, other_task_index):
        a = task_index
        b = other_task_index
        self._tasks[a].index, self._tasks[b].index = self._tasks[b].index, self._tasks[a].index
        self._tasks[a], self._tasks[b] = self._tasks[b], self._tasks[a]

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, new_index):
        self._index = new_index

    @property
    def due_date(self):
        return self._due_date

    def change_due_date(self, new_date: datetime):
        self._due_date = new_date

    def remove_due_date(self):
        self._due_date = None

