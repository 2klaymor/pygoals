import core.shared.general
from core.repositories.taskrepository import TaskRepository


class Task:
    def __init__(self, id_, goal_id, text, completed):
        self.id = id_
        self.goal_id = goal_id
        self.text = text
        self._completed = bool(completed)

    @property
    def completed(self):
        return int(self._completed)

    @completed.setter
    def completed(self, value):
        self._completed = bool(value)

    def __str__(self):
        return (f'Task ID:{self.id} in Goal ID:{self.goal_id}\n'
                f'\"{self.text}\"\n'
                f'Done: {self.completed}')


class TaskModel:
    def __init__(self):
        self.table = core.shared.general.TASKS
        self.repository = TaskRepository()

    def get_tasks(self):
        tasks = [
            Task(id_, goal_id, text, completed)
            for (id_, goal_id, text, completed)
            in self.repository.get_all()
        ]
        return tasks

    def get_tasks_by_goal_id(self, goal):
        goal_id_expr = f'{goal.id}'
        tasks = [
            Task(id_, goal_id, text, completed)
            for (id_, goal_id, text, completed)
            in self.repository.get_by_goal_id(goal_id_expr)
        ]
        return tasks

    def get_task(self, task: Task):
        id_expr = f'{task.id}'
        id_, goal_id, text, completed = self.repository.get_by_id(id_expr)
        return Task(id_, goal_id, text, completed)

    def create_task(self, goal_id, text, completed):
        column_expr = '(goal_id, text, completed)'
        values_expr = (f'({goal_id}, '
                       f'\"{text}\", '
                       f'{int(completed)})')
        id_, goal_id, text, completed = self.repository.create(column_expr, values_expr)
        return Task(id_, goal_id, text, completed)

    def update_task(self, task: Task):
        set_expr = f'text=\"{task.text}\", completed={task.completed}'
        where_expr = f'id={task.id}'
        self.repository.update(set_expr, where_expr)

    def delete_task(self, task: Task):
        where_expr = f'id={task.id}'
        self.repository.delete(where_expr)
