import flet as ft

TITLE: str = "Flet Todo App"
SIZE: tuple = (480, 720)


def main(page: ft.Page):
    page.title = TITLE
    page.window_width = SIZE[0]
    page.window_height = SIZE[1]
    page.window_resizable = False

    page.add(ft.Text("Hello, world!"))


ft.app(target=main)
