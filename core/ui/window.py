import tkinter as tk
import core
from pprint import pprint


class GoalView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.configure(
            bg=core.ui.theme.BACKGROUND_PRIMARY
        )

        self.goal_label = tk.Label(
            self,
            font=core.ui.font.GOALVIEW_NAME,
            bg=core.ui.theme.BACKGROUND_PRIMARY
        )
        self.goal_label.pack(
            fill=tk.X,
            pady=20
        )


class SideBar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(
            bg=core.ui.theme.BACKGROUND_SECONDARY,
            width=230
        )

        self.goals = core.App.get_data('goals')

        for goal in self.goals:
            print(goal['name'])

        # self.search_entry = SearchEntry(
        #     self,
        #     hint_text='Search',
        #     bg=Theme.BACKGROUND_SECONDARY
        # )
        # self.search_entry.pack(
        #     fill=tk.X,
        #     padx=10,
        #     pady=10
        # )


class MainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(
            bg=core.ui.theme.BACKGROUND_PRIMARY
        )

        self.side_bar = SideBar(self)
        self.side_bar.pack(
            side=tk.LEFT,
            fill=tk.Y
        )

        self.goal_view = GoalView(self)
        self.goal_view.pack(
            expand=True,
            fill=tk.BOTH
        )


class Window(tk.Tk):

    _instance = None
    _app = None

    def __new__(cls, *args, **kwargs):
        if not Window._instance:
            Window._instance = super().__new__(cls)
        return Window._instance

    def __init__(self, app):
        super().__init__()

        Window._app = app

        self.title(f'{self.app().get_data('user')}')
        self.geometry('800x600')
        self.resizable(False, False)
        self.update()

        self.main_window = MainPage(self)
        self.main_window.pack(
            expand=True,
            fill=tk.BOTH
        )

    @staticmethod
    def app():
        return Window._app

    def launch(self):
        self.mainloop()
