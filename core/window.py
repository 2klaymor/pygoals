import tkinter as tk

import core.shared.theme
import core.shared.font
import core.shared.general
from core.controllers.goalcontroller import GoalController
from core.views.goalbuttonview import GoalButtonView
from core.views.goalpageview import GoalPageView


class SideBar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.controller = GoalController(self)

        # Configuring the sidebar
        self.configure(
            bg=core.shared.theme.BACKGROUND_SECONDARY,
            width=250
        )
        self.propagate(False)

        self.goalbutton_views = {}

        # Search Entry
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(
            self,
            bg=core.shared.theme.BACKGROUND_PRIMARY,
            font=core.shared.font.SIDEBAR_PRIMARY,
            borderwidth=6,
            relief=core.shared.theme.RELIEF_ENTRY,
            textvariable=self.search_var
        )
        self.search_entry.pack(
            fill=tk.X,
            padx=10,
            pady=(10, 0)
        )

        self.create_button = tk.Button(
            self,
            bg=core.shared.theme.BUTTON_ACCENT,
            fg=core.shared.theme.FONT_ON_ACCENT,
            text=core.shared.general.LOCALE['NEW_GOAL_BUTTON'],
            font=core.shared.font.SIDEBAR_PRIMARY_BOLD,
            command=self.create_goal,
            relief=core.shared.theme.RELIEF
        )
        self.create_button.pack(
            pady=10,
            padx=10,
            fill=tk.X
        )

        self.update_views()

    def update_views(self):
        for goal in self.controller.get_goals():
            if goal.id in self.goalbutton_views:
                self.goalbutton_views[goal.id].update_view(goal)
            else:
                goalbutton_view = GoalButtonView(self)
                goalbutton_view.update_view(goal)

                self.goalbutton_views[goalbutton_view.goal.id] = goalbutton_view
                self.bind_view(goalbutton_view)
                self.show_view(goalbutton_view)

    def show_view(self, view):
        view.pack(
            before=self.create_button,
            pady=(10, 0),
            padx=10,
            fill=tk.X
        )

    def bind_view(self, view):
        view.open_button.configure(
            command=lambda: self.master.open_goal_page(view.goal)
        )
        view.delete_button.configure(
            command=lambda: self.delete_goal(view)
        )

    def create_goal(self):
        goalbutton_view = GoalButtonView(self)
        goalbutton_view.create_goal()

        self.goalbutton_views[goalbutton_view.goal.id] = goalbutton_view
        self.bind_view(goalbutton_view)
        self.show_view(goalbutton_view)

    def delete_goal(self, goalbutton):
        self.goalbutton_views.pop(goalbutton.goal.id)
        self.master.goalpage_view.tasklist_view.on_goal_delete(goalbutton.goal)
        goalbutton.delete_goal()
        self.master.close_goal_page(goalbutton.goal)


class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(
            bg=core.shared.theme.BACKGROUND_PRIMARY
        )

        self.side_bar = SideBar(self)
        self.side_bar.pack(
            side=tk.LEFT,
            fill=tk.Y
        )

        self.goalpage_view = GoalPageView(self)
        self.update()

    def open_goal_page(self, goal):
        self.goalpage_view.update_view(goal)
        self.goalpage_view.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )
        self.goalpage_view.tasklist_view.update_all_tasks()
        self.goalpage_view.tasklist_view.on_goalpage_change()

    def close_goal_page(self, deleted_goal=None):
        if not self.goalpage_view.goal:
            return
        if not deleted_goal:
            self.goalpage_view.pack_forget()
            return
        if self.goalpage_view.goal.id == deleted_goal.id:
            self.goalpage_view.pack_forget()

    def update_sidebar_views(self):
        self.side_bar.update_views()


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(f'{core.shared.general.APP_NAME} {core.shared.general.APP_VER}')
        self.geometry(f'{core.shared.general.DEFAULT_WIDTH}x{core.shared.general.DEFAULT_HEIGHT}')
        self.minsize(core.shared.general.MIN_WIDTH, core.shared.general.MIN_HEIGHT)
        self.update()

        self.main_page = MainPage(self)
        self.main_page.pack(
            expand=True,
            fill=tk.BOTH
        )

    def launch(self):
        self.mainloop()
