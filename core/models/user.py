from core.models.goal import Goal


class User:
    def __init__(self, username):
        self._username = username
        self._goals = []

    # Get the Goal object
    def goal(self, goal_index):
        return self._goals[goal_index]

    # Create new Goal object and append it to the list of goals
    def new_goal(self, goal_name):
        goal = Goal(goal_name)
        goal.index = len(self._goals)
        self._goals.append(goal)

    # Remove Goal by specified index
    def remove_goal(self, goal_index):
        self._goals.pop(goal_index)


