import tkinter as tk
from core.ui.widgets import SearchEntry
from core.ui.theme import (Theme, Font)


class GoalPage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.configure(
            bg=Theme.BACKGROUND_PRIMARY
        )

        self.goal_label = tk.Label(
            self,
            text='Test goal label',
            font=Font.GOALVIEW_NAME,
            bg=Theme.BACKGROUND_PRIMARY
        )
        self.goal_label.pack(
            fill=tk.X,
            pady=20,
            # anchor=tk.N
        )


class SideBar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.search_entry = SearchEntry(
            self,
            hint_text='Search',
            bg=Theme.BACKGROUND_SECONDARY
        )
        self.search_entry.pack(
            fill=tk.X,
            padx=10,
            pady=10
        )


class MainPage(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root

        self.configure(
            bg=Theme.BACKGROUND_PRIMARY
        )

        self.side_bar = SideBar(self)
        self.side_bar.pack(
            side=tk.LEFT,
            fill=tk.Y
        )

        self.goal_view = GoalPage(self)
        self.goal_view.pack(
            expand=True,
            fill=tk.BOTH
        )
















# import flet as ft
# from core.themes import Theme
#
#
# class MainView(ft.UserControl):
#     def __init__(self, page: ft.Page):
#         super().__init__()
#         self.page = page
#
#         self.content = ft.Column(
#             [
#
#             ]
#         )
#
#     def build(self):
#         return self.content
#
#
# class SideBarView(ft.UserControl):
#     def __init__(self, page: ft.Page):
#         super().__init__()
#         self.page = page
#
#         self.search_bar = ft.TextField(
#             prefix_icon=ft.icons.SEARCH,
#             hint_text='Search'
#         )
#
#         self.content = ft.Column(
#             [
#                 self.search_bar
#             ],
#         )
#
#         self.container = ft.Container(
#             self.content,
#             width=self.page.window_width // 2,
#             height=self.page.window_height,
#             border=ft.border.all(2, Theme.primary)
#         )
#
#         self.goals = []
#
#     def build(self):
#         return self.container
#
#
# class AppView(ft.UserControl):
#     def __init__(self, page: ft.Page):
#         super().__init__()
#         self.page = page
#
#         self.sidebar = SideBarView(page)
#         self.mainview = MainView(page)
#
#         self.content = ft.Row(
#             [
#                 self.sidebar,
#                 self.mainview
#             ]
#         )
#
#     def build(self):
#         return self.content
