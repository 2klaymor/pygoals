import tkinter as tk

from core.controllers.taskcontroller import TaskController
from core.shared.widgets.checkbox import CheckBox
import core.shared.theme
import core.shared.font
import core.shared.general


class TaskView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.task = None
        self.lines = 1
        self.controller = TaskController(self)

        self.configure(
            bg=core.shared.theme.BACKGROUND_ACCENT
        )

        self.text_var = tk.StringVar()
        self.text_entry = tk.Entry(
            self,
            font=core.shared.font.GOALPAGE_TASK,
            bg=core.shared.theme.BACKGROUND_PRIMARY,
            fg=core.shared.theme.FONT_ON_PRIMARY,
            relief=core.shared.theme.RELIEF_ENTRY,
            borderwidth=2,
            textvariable=self.text_var
        )
        self.text_entry.pack(
            side=tk.LEFT,
            pady=2,
            padx=4,
            fill=tk.X,
            expand=True
        )
        self.text_entry.bind(
            '<FocusOut>',
            self.update_task
        )
        self.text_entry.bind(
            '<KeyPress-Return>',
            self.update_task
        )

        self.check_button = CheckBox(
            self,
            font=core.shared.font.GOALPAGE_TASK
        )
        self.check_button.pack(
            side=tk.LEFT
        )
        self.check_button.add_binding(self.update_task)

        self.delete_button = tk.Button(
            self,
            text='    ',
            font=core.shared.font.GOALPAGE_TASK,
            bg=core.shared.theme.BUTTON_WARNING,
            relief=core.shared.theme.RELIEF
        )
        self.delete_button.pack(
            side=tk.LEFT
        )

    def create_task(self, goal_id):
        self.controller.create_task(goal_id)

    def delete_task(self):
        self.controller.delete_task(self.task)

    def update_view(self, task):
        self.check_button.state = task.completed
        self.task = task
        self.text_var.set(task.text)

    def update_task(self, *args):
        self.task.text = self.text_var.get()
        self.task.completed = self.check_button.state
        self.controller.update_task(self.task)

    def clear_view(self):
        self.destroy()


class TaskListView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.controller = TaskController(self)

        self.configure(
            bg=core.shared.theme.BACKGROUND_PRIMARY
        )

        self.goal = None
        self.task_views = {}
        self.create_button = tk.Button(
            self,
            text=core.shared.general.LOCALE['NEW_TASK_BUTTON'],
            font=core.shared.font.GOALPAGE_CONTENT,
            bg=core.shared.theme.BUTTON_ACCENT,
            fg=core.shared.theme.FONT_ON_ACCENT,
            width=15,
            relief=core.shared.theme.RELIEF,
            command=self.create_task
        )
        self.create_button.pack(
            pady=30
        )

    def update_views(self):
        self.goal = self.master.goal
        for task in self.controller.get_tasks_by_goal_id(self.goal):
            if self.goal.id != task.goal_id:
                continue
            if task.id in self.task_views:
                self.task_views[task.id].update_view(task)
            else:
                task_view = TaskView(self)
                task_view.update_view(task)

                self.task_views[task_view.task.id] = task_view
                self.bind_view(task_view)
                self.show_view(task_view)

    def on_goalpage_change(self):
        self.clear_view()
        self.update_views()

    def on_goal_delete(self, goal):
        for task in self.controller.get_tasks_by_goal_id(goal):
            self.controller.delete_task(task)

    def clear_view(self):
        for task_view in self.task_views.values():
            task_view.pack_forget()
        self.task_views = {}

    def show_view(self, view):
        view.pack(
            before=self.create_button,
            pady=(10, 0),
            padx=30,
            fill=tk.X
        )

    def bind_view(self, view):
        view.delete_button.configure(
            command=lambda: self.delete_task(view)
        )

    def create_task(self):
        task_view = TaskView(self)
        task_view.create_task(self.master.goal.id)
        task_view.check_button.state = False
        self.task_views[task_view.task.id] = task_view
        self.bind_view(task_view)
        self.show_view(task_view)

    def delete_task(self, task_view):
        task_view.delete_task()

    def update_all_tasks(self):
        for task_view in self.task_views.values():
            task_view.update_task()


