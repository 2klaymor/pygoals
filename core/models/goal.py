import core.shared.general
from core.repositories.goalrepository import GoalRepository


class Goal:
    def __init__(self, id_, name):
        self.id = id_
        self.name = name

    def __str__(self):
        return (f'Goal ID:{self.id}\n'
                f'\"{self.name}\"')


class GoalModel:
    def __init__(self):
        self.table = core.shared.general.GOALS
        self.repository = GoalRepository()

    def get_goals(self):
        goals = [
            Goal(id_, name)
            for (id_, name)
            in self.repository.get_all()
        ]

        return goals

    def get_goal(self, goal: Goal):
        id_expr = f'{goal.id}'
        id_, name = self.repository.get_by_id(id_expr)
        return Goal(id_, name)

    def create_goal(self, goal_name):
        column_expr = '(name)'
        values_expr = f'(\"{goal_name}\")'
        id_, name = self.repository.create(column_expr, values_expr)
        return Goal(id_, name)

    def update_goal(self, goal: Goal):
        set_expr = f'name=\"{goal.name}\"'
        where_expr = f'id={goal.id}'
        self.repository.update(set_expr, where_expr)

    def delete_goal(self, goal: Goal):
        where_expr = f'id={goal.id}'
        self.repository.delete(where_expr)
