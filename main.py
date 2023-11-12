from classes import AppWindow
import flet as ft


def main(page: ft.Page):

    app_window = AppWindow()

    page.title = app_window.title
    page.window_width = app_window.width
    page.window_height = app_window.height
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0

    page.add(app_window)

    page.update()


if __name__ == '__main__':
    ft.app(main)
