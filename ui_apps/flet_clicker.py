import flet

def main(page: flet.Page):
    page.title = 'Кликер'
    page.theme_mode = 'dark'
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    text_label = flet.TextField('0', text_align=flet.TextAlign.CENTER, width=100)

    def click_remove(event):
        text_label.value = int(text_label.value) - 1
        page.update()


    def click_plus(event):
        text_label.value = int(text_label.value) + 1
        page.update()

    page.add(
        flet.Row(
            [
                flet.IconButton(flet.icons.REMOVE, on_click=click_remove),
                text_label,
                flet.IconButton(flet.icons.ADD, on_click=click_plus)

            ],
            alignment=flet.MainAxisAlignment.CENTER
        )
    )
    
flet.app(target=main)