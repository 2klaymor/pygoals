import tkinter as tk
from core.theme import Theme
from core.widgets.search_entry import SearchEntry


class SideBar(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.search_entry = SearchEntry(
            self,
            hint_text='Search'
        )
        self.search_entry.pack()

        self.configure(
            background=Theme.SECONDARY_BACKGROUND
        )


class MainWindow(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root
        self._min_width = root.root_geometry

        self.configure(
            background=Theme.BACKGROUND
        )

        self.side_bar = SideBar(self)
        self.side_bar.pack(
            side=tk.LEFT,
            fill=tk.Y
        )

    @property
    def root_geometry(self):
        return self.root.root_geometry
















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
