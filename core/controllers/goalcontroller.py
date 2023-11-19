from core.models.goal import Goal
from core.models.goal import GoalModel
import core.shared.general


class GoalController:
    views = []

    def __init__(self, view):
        self.view = view
        # GoalController.views.append(self.view)
        self.model = GoalModel()

    def get_goal(self, goal):
        return self.model.get_goal(goal)

    def get_goals(self):
        return self.model.get_goals()

    def create_goal(self):
        name = core.shared.general.LOCALE['NEW_GOAL_CREATED']
        goal = self.model.create_goal(name)
        self.view.update_view(goal)

    def update_goal(self, goal):
        self.model.update_goal(goal)

    def delete_goal(self, goal):
        self.model.delete_goal(goal)
        self.view.clear_view()

