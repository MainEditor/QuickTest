import flet as ft

class DataSelector():
    def __init__(self):
        self.file = self.subject_selected = self.select_path = None

    def window(self, page: ft.Page):
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.spacing = 10
        page.title = "QuickTest"
        page.window_maximizable = False
        page.window_resizable = False
        page.window_width = 500
        page.window_center()
        page.scroll = ft.ScrollMode.ADAPTIVE 

        buttons = []
        data = dict()

        def click(e):
            self.subject_selected = e.control.content.value
            self.file, self.select_path = data[self.subject_selected]
            page.window_close()

        for file_path in self.pathes_list:
            cur_file = open(file_path, encoding = 'utf-8')
            subject = cur_file.readline().strip()
            data[subject] = ([x.strip('\n').strip('	').split('	') for x in cur_file.readlines()], file_path)
            buttons += [ft.OutlinedButton(content=ft.Text(subject, size=18), on_click = click, width=450)]

        text = ft.Text(f"Выберите необходимую тему из списка:", size = 24)
        warn_messege = (ft.Text('Отсутствуют доступные наборы тестов.', size = 15, color='grey'), )
        page.add(text, *buttons if len(buttons) > 0 else warn_messege)
    
    def select_topic(self, pathes):
        self.pathes_list = pathes
        ft.app(target=self.window)
        return (self.file, self.subject_selected, self.select_path)