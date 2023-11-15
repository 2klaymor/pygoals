import tkinter as tk
from core.ui.theme import (Theme, Font)
from pprint import pprint


class GoalView(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.configure(
            bg=Theme.BACKGROUND_PRIMARY
        )

        self.goal_label = tk.Label(
            self,
            font=Font.GOALVIEW_NAME,
            bg=Theme.BACKGROUND_PRIMARY
        )
        self.goal_label.pack(
            fill=tk.X,
            pady=20
        )


class SideBar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.configure(
            bg=Theme.BACKGROUND_SECONDARY,
            width=230
        )

        self.goals = Window.app().get_data('goals')
        pprint(self.goals)

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
            bg=Theme.BACKGROUND_PRIMARY
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
