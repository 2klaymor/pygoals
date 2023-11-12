import flet as ft
from flet import icons
from flet import colors
import constants as c


class TaskList(ft.UserControl):
    def __init__(self, master):
        super().__init__()

        self.master = master

        self.content = ft.Column()

    def build(self):
        return self.content


class NewTask(ft.UserControl):
    def __init__(self, master):
        super().__init__()

        self.master = master

        self.hint = 'What\'s on your mind today?'  # TODO language specific text variables
        self.textfield_var = ''

        self.textfield = ft.TextField(
            height=50,
            # text_size=15,
            border_color=colors.BLUE_600,
            border_width=3,
            border_radius=10,
            hint_text=self.hint,
            # color=colors.GREY_900,
            expand=True
        )

        self.add_button = ft.FloatingActionButton(
            content=ft.Icon(
                ft.icons.ADD,
                color=colors.WHITE
            ),
            bgcolor=colors.BLUE_600,
            width=50,
            height=50,
            on_click=self.master.add_task
        )

        self.content = ft.Row(
            [
                self.textfield,
                self.add_button
            ],
            spacing=10
        )

    def build(self):
        return self.content


class AppWindow(ft.UserControl):
    def __init__(self):
        super().__init__()

        self.width = c.WINDOW_WIDTH
        self.height = c.WINDOW_HEIGHT
        self.title = c.APP_NAME

        self.newtask = NewTask(self)
        self.tasklist = TaskList(self)

        self.content = ft.Container(
            ft.Column(
                [
                    self.newtask,
                    self.tasklist
                ]
            ),
            padding=15
        )

    def add_task(self, e: ft.ControlEvent):
        pass

    def build(self):
        return self.content
