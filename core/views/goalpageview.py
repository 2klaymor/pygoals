import tkinter as tk

from core.controllers.goalcontroller import GoalController
from core.views.tasklistview import TaskListView
import core.shared.theme
import core.shared.font
import core.shared.general


class GoalPageView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.goal = None
        self.name_var = tk.StringVar()
        self.controller = GoalController(self)

        self.configure(
            bg=core.shared.theme.BACKGROUND_PRIMARY
        )

        self.header = tk.Frame(
            self,
            bg=core.shared.theme.BACKGROUND_ACCENT,
            height=55
        )
        self.header.propagate(False)
        self.header.pack(
            fill=tk.X
        )

        self.name_entry = tk.Entry(
            self.header,
            textvariable=self.name_var,
            bg=core.shared.theme.BACKGROUND_ACCENT,
            fg=core.shared.theme.FONT_ON_ACCENT,
            font=core.shared.font.GOALPAGE_LABEL,
            relief=core.shared.theme.RELIEF_ENTRY,
            justify=tk.CENTER
        )
        self.name_entry.bind(
            '<FocusOut>',
            self.update_goal_name
        )
        self.name_entry.bind(
            '<KeyPress-Return>',
            self.update_goal_name
        )
        self.name_entry.pack(
            side=tk.LEFT,
            pady=15,
            padx=(15, 5),
            fill=tk.X,
            expand=True
        )
        self.close_button = tk.Button(
            self.header,
            font=core.shared.font.SIDEBAR_PRIMARY_BOLD,
            fg=core.shared.theme.FONT_ON_PRIMARY,
            bg=core.shared.theme.BUTTON_INFORMAL,
            text=core.shared.general.LOCALE['CLOSE_BUTTON'],
            command=self.close_page,
            relief=core.shared.theme.RELIEF
            # width=2
        )
        self.close_button.pack(
            padx=(5, 10),
            side=tk.LEFT
        )

        self.tasklist_view = TaskListView(self)
        self.tasklist_view.pack(
            expand=True,
            fill=tk.BOTH
        )

    def update_view(self, goal):
        self.goal = goal
        self.name_var.set(self.goal.name)
        self.tasklist_view.update_views()

    def update_goal_name(self, *args):
        self.goal.name = self.name_var.get()
        self.controller.update_goal(self.goal)
        self.master.update_sidebar_views()

    def close_page(self):
        self.update_goal_name()
        self.tasklist_view.update_all_tasks()
        self.master.close_goal_page()
