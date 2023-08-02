import flet as ft
from GUI_handler.statistics_window import StatWindow
from data_handler.data_reader import get_pathes

class DataSelector():
    def __init__(self):
        self.GO_TO = None
        self.file = self.subject_selected = self.select_path = None
        self.pathes_list = get_pathes()
        ft.app(target=self.window)

    def topic_click(self, e: ft.ControlEvent):
        self.GO_TO = "TEST"
        self.subject_selected = e.control.content.value
        self.file, self.select_path = self.data_dict[self.subject_selected]
        self.data = [self.file[:-1], self.subject_selected, self.select_path]
        self.close()

    def window(self, page: ft.Page):
        page.window_center()
        page.window_focused = True
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.spacing = 10
        page.title = "QuickTest"
        page.window_maximizable = False
        page.window_resizable = False
        page.window_width = page.window_min_width = 525
        page.window_height = page.window_min_height = 800
        page.scroll = ft.ScrollMode.ADAPTIVE

        self.close = lambda: page.window_close()

        buttons = []
        self.data_dict = dict()

        for file_path in self.pathes_list:
            cur_file = open(file_path, encoding = 'utf-8')
            subject = cur_file.readline().strip()
            self.data_dict[subject] = ([x.strip('\n').strip('	').split('	') for x in cur_file.readlines()], file_path)
            row = ft.Row(controls=[ft.OutlinedButton(content=ft.Text(value=subject, size=18), on_click = self.topic_click, width=425), 
                                   ft.IconButton(icon=ft.icons.AUTO_GRAPH_OUTLINED, on_click=self.stat_click, tooltip=f'Статистика "{subject}"')], 
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=5)
            buttons += [ row ]

        text = ft.Text(f"Выберите необходимую тему из списка:", size = 24)
        warn_messege = (ft.Text('Отсутствуют доступные наборы тестов.', size = 15, color='grey'), )
        page.add(text, *buttons if len(buttons) > 0 else warn_messege)
    
    def stat_click(self, e: ft.ControlEvent):
        self.GO_TO = "STAT"
        self.topic = str(e.control.tooltip).replace('Статистика "', '')[:-1]
        self.statistics = self.data_dict[self.topic][0][-1]
        self.close()