import flet as ft

TITLE: str = "Flet Todo App"


def main(page: ft.Page):
    page.title = TITLE

    page.add(ft.Text("Hello, world!"))


ft.app(target=main)
