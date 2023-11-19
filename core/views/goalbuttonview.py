import tkinter as tk

from core.controllers.goalcontroller import GoalController
import core.shared.theme
import core.shared.font


class GoalButtonView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.goal = None
        self.name_var = tk.StringVar()
        self.controller = GoalController(self)

        self.open_button = tk.Button(
            self,
            textvariable=self.name_var,
            font=core.shared.font.SIDEBAR_PRIMARY_BOLD,
            bg=core.shared.theme.BUTTON_INFORMAL,
            fg=core.shared.theme.FONT_ON_SECONDARY,
            relief=core.shared.theme.RELIEF,
            wraplength=180
        )
        self.open_button.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True
        )

        self.delete_button = tk.Button(
            self,
            text='    ',
            font=core.shared.font.SIDEBAR_PRIMARY_BOLD,
            bg=core.shared.theme.BUTTON_WARNING,
            relief=core.shared.theme.RELIEF
        )
        self.delete_button.pack(
            side=tk.LEFT,
            fill=tk.BOTH
        )
        self.delete_button.pack_propagate(False)

    def create_goal(self):
        self.controller.create_goal()

    def delete_goal(self):
        self.controller.delete_goal(self.goal)

    def update_view(self, goal):
        self.goal = goal
        self.name_var.set(self.goal.name)
        self.update()

    def clear_view(self):
        self.destroy()