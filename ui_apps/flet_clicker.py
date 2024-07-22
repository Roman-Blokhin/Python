import flet

def main(page: flet.Page):
    page.title = 'Кликер'
    page.theme_mode = 'light'
    page.vertical_alignment = flet.MainAxisAlignment.CENTER

    text_number = flet.ElevatedButton('Click me')
    text_label = flet.Text('0', width=10, color='#fgfgfg')
    page.update()

    def click(enter):
        pass

        page.add(
            flet.Row(
                [
                    text_number,
                    text_label
                ]
            )
        )
    
    flet.app(target=main)