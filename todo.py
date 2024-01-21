import flet as ft

TITLE: str = "Flet Todo App"
GEOMETRY: tuple = (480, 720)


class task_item():
    task_name: str
    task: ft.Row
    id: int

    def remove_item(self, e):
        del self.task

    def create_task(self, name: str):
        return ft.Row(
            [
                ft.Text(
                    value=name,
                    font_family='arial',
                    size=36,
                    weight=600
                ),
                ft.Row(
                    [
                        ft.Checkbox(),
                        ft.ElevatedButton(
                            text='REMOVE',
                            on_click=self.remove_item
                        )
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

    def __init__(self, val: str, identifier: int) -> None:
        self.task_name = val
        self.task = self.create_task(val)
        self.id = identifier


tasks = {}


def main(page: ft.Page):
    page.title = TITLE
    page.window_width = GEOMETRY[0]
    page.window_height = GEOMETRY[1]
    page.window_resizable = False

    def add_task_clicked(e):
        value = task_input.value

        if value == '':
            return

        item: task_item = task_item(value, len(tasks.keys()) + 1)

        page.add(
            item.task
        )

        tasks[item.id] = item
        print(tasks)

        task_input.value = ''
        task_input.update()

    page_title: ft.Text = ft.Text(
        value='Todo App',
        text_align=ft.TextAlign.CENTER,
        size=36,
        font_family='Arial',
        weight=600
    )
    page.add(ft.Row([page_title], alignment=ft.MainAxisAlignment.CENTER))

    task_input: ft.TextField = ft.TextField(
        hint_text='What would you like to get done...'
    )
    add_button: ft.ElevatedButton = ft.ElevatedButton(
        text='ADD TASK',
        on_click=add_task_clicked
    )

    page.add(
        ft.Row(
            [
                task_input, add_button
            ]
        )
    )


ft.app(target=main)
