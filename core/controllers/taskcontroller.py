from core.models.task import TaskModel


class TaskController:
    def __init__(self, view):
        self.view = view
        self.model = TaskModel()

    def get_task(self, task):
        return self.model.get_task(task)

    def get_tasks(self):
        return self.model.get_tasks()

    def get_tasks_by_goal_id(self, goal):
        return self.model.get_tasks_by_goal_id(goal)

    def create_task(self, goal_id):
        text = ''
        completed = False
        task = self.model.create_task(goal_id, text, completed)
        self.view.update_view(task)

    def update_task(self, task):
        self.model.update_task(task)

    def delete_task(self, task):
        self.model.delete_task(task)
        self.view.clear_view()
    