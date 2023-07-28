import flet as ft

file, subject_selected, select_path = None, None, None

def window(page: ft.Page) -> None:
    global pathes_list
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 10
    page.title = "QuickTest"
    page.window_maximizable = False
    page.window_resizable = False
    page.window_width = 500
    page.scroll = ft.ScrollMode.ADAPTIVE 

    buttons = []
    data = dict()

    def click(e):
        global file, subject_selected, select_path
        subject_selected = e.control.content.value
        file, select_path = data[subject_selected]
        page.window_close()

    for file_path in pathes_list:
        cur_file = open(file_path, encoding = 'utf-8')
        subject = cur_file.readline().strip()
        data[subject] = ([x.strip('\n').strip('	').split('	') for x in cur_file.readlines()], file_path)
        buttons += [ft.OutlinedButton(content=ft.Text(subject, size=18), on_click = click, width=450)]
    
    text = ft.Text(f"Выберите необходимую тему из списка:", size = 24)
    warn_messege = (ft.Text('Отсутствуют доступные наборы тестов.', size = 15, color='grey'), )
    
    page.add(text, *buttons if len(buttons) > 0 else warn_messege)

def select_topic(pathes: str) -> tuple:
    global pathes_list
    pathes_list = pathes
    ft.app(target=window)
    return (file, subject_selected, select_path)