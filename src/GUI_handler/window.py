import flet as ft
import data_handler.current_working_data as data

def click(e=None, button=None) -> None:
    if e != None:
        is_answer_correct = e.control.content.value == data.answer
    else:
        is_answer_correct = button.content.value == data.answer
    data.update_question(is_answer_correct)
    update_GUI(is_answer_correct)

def on_keyboard(e: ft.KeyboardEvent):
    if e.key == "Arrow Left":	click(button=btn1)
    elif e.key == "Arrow Right":	click(button=btn2)

button_style = ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=10), elevation = 5)

question_text = ft.Text(data.question, text_align = "center", size = 35)
banner = ft.Text("Начинай!", color = "white", size = 30, scale=1.25)
counter = ft.Text(f'ВЕРНО👍        {data.count_correct} : {data.count_wrong}        👎НЕВЕРНО', size = 20)
btn1 = ft.ElevatedButton(style = button_style, content = ft.Text(data.answer, size = 30), on_click = click)
btn2 = ft.ElevatedButton(style = button_style, content = ft.Text(data.wrong_answer, size = 30), on_click = click)
row = ft.Row(wrap = True, alignment = ft.MainAxisAlignment.CENTER, controls = (ft.Text("←", size = 40), btn1, ft.Text("или", scale = 1.2), btn2, ft.Text("→", size = 40)))
progressBar = ft.ProgressBar(height = 8, width = 500, color = "#70b658", bgcolor = "#eb4540")
number_of_question = ft.Text(f"{data.index + 1} / {len(data.file)}", size=18)
back_button = ft.TextButton(content=ft.Row([ft.Icon(name=ft.icons.ARROW_BACK), ft.Text('Вернуться к списку тем')], width=200, alignment=ft.MainAxisAlignment.CENTER), on_click=data.return_to_select)

UI = (banner, question_text, row, counter, progressBar, number_of_question, back_button)

def main(page: ft.Page) -> None:
    global update_GUI
    def update_GUI(is_ans_correct: bool):
        question_text.value = data.question
        counter.value = f'ВЕРНО👍        {data.count_correct} : {data.count_wrong}        👎НЕВЕРНО'
        btn1.content.value, btn2.content.value = data.answer_options
        number_of_question.value = f"{data.index + 1} / {len(data.file)}"
        if is_ans_correct:
            banner.value, banner.bgcolor = "ВЕРНО", "green"
        elif not is_ans_correct:
            banner.value, banner.bgcolor = "НЕВЕРНО", "red"
        progressBar.value = data.count_correct / (data.count_correct + data.count_wrong)
        page.update()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.spacing = 40
    page.title = "QuickTest"
    page.window_height = 580
    page.window_width = 850
    page.on_keyboard_event = on_keyboard
    page.add(*UI)

def start_test() -> None:
    ft.app(target=main)