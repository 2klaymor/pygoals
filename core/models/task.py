class Task:
    def __init__(self, text):
        self._index = None
        self._text = text
        self._completed = False

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, new_index):
        self._index = new_index

    # Returns the boolean value of _completed
    @property
    def is_completed(self):
        return self._completed

    # Switches _completed attr value
    def switch_complete_state(self):
        if self.is_completed:
            self._completed = False
        else:
            self._completed = True

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):
        self._text = new_text


# class TaskList:
#     def __init__(self):
#         self._tasks = []
#
#     def add_task(self, task_text):
#         task = Task(task_text)
#         task.index = len(self._tasks)
#         self._tasks.append(task)
#
#     def remove_task(self, task_index: Task.index):
#         self._tasks.pop(task_index)
#
#     def switch_tasks(self, task_index: Task.index, other_task_index: Task.index):
#         a = task_index
#         b = other_task_index
#         self._tasks[a].index, self._tasks[b].index = self._tasks[b].index, self._tasks[a].index
#         self._tasks[a], self._tasks[b] = self._tasks[b], self._tasks[a]
#
#     def get_task(self, task_index: Task.index):
#         return self._tasks[task_index]
#
#     def __repr__(self):
#         return f'[{[f'{task.index}: {task.text}' for task in self._tasks]}]'




    