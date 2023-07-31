import flet as ft
import data_handler.current_working_data as DT

class MainWindow():
    def __init__(self):
        self.data = DT.CurrentData()
        self.NEED_RESTART = False
        button_style = ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=10), elevation = 5)
        self.question_text = ft.Text(self.data.question, text_align = "center", size = 35)
        self.banner = ft.Text("Начинай!", color = "white", size = 30, scale=1.25)
        self.counter = ft.Text(f'ВЕРНО👍        {self.data.count_correct} : {self.data.count_wrong}        👎НЕВЕРНО', size = 20)
        self.btn1 = ft.ElevatedButton(style = button_style, content = ft.Text(self.data.answer, size = 28), on_click = self.click)
        self.btn2 = ft.ElevatedButton(style = button_style, content = ft.Text(self.data.wrong_answer, size = 28), on_click = self.click)
        self.row = ft.Row(wrap = True, alignment = ft.MainAxisAlignment.CENTER, controls = (ft.Text("←", size = 40), self.btn1, ft.Text("или", scale = 1.2), self.btn2, ft.Text("→", size = 40)))
        self.progressBar = ft.ProgressBar(height = 8, width = 500, color = "green", bgcolor = "red")
        self.number_of_question = ft.Text(f"{self.data.index + 1} / {len(self.data.file)}", size=18)
        self.back_button = ft.TextButton(content=ft.Row([ft.Icon(name=ft.icons.ARROW_BACK), ft.Text('Вернуться к списку тем')], width=200, alignment=ft.MainAxisAlignment.CENTER), on_click=self.go_back)
        self.UI = (self.banner, self.question_text, self.row, self.counter, self.progressBar, self.number_of_question, ft.Text(self.data.topic), self.back_button)
    
    def update_GUI(self, is_ans_correct: bool):
        self.question_text.value = self.data.question
        self.counter.value = f'ВЕРНО👍        {self.data.count_correct} : {self.data.count_wrong}        👎НЕВЕРНО'
        self.btn1.content.value, self.btn2.content.value = self.data.answer_options
        self.number_of_question.value = f"{self.data.index + 1} / {len(self.data.file)}"
        if is_ans_correct:
            self.banner.value, self.banner.bgcolor = "ВЕРНО", "green"
        elif not is_ans_correct:
            self.banner.value, self.banner.bgcolor = "НЕВЕРНО", "red"
        self.progressBar.value = self.data.count_correct / (self.data.count_correct + self.data.count_wrong)
        self.update()
    
    def click(self, e=None, button=None) -> None:
        if e != None:
            is_answer_correct = e.control.content.value == self.data.answer
        else:
            is_answer_correct = button.content.value == self.data.answer
        self.data.update_question(is_answer_correct)
        self.update_GUI(is_answer_correct)
    
    def on_keyboard(self, e: ft.KeyboardEvent):
        if e.key == "Arrow Left":	self.click(button=self.btn1)
        elif e.key == "Arrow Right":	self.click(button=self.btn2)
    
    def go_back(self, e):
        self.NEED_RESTART = True
        self.close()
    
    def create_window(self, page: ft.Page):
        page.window_center()
        self.update = lambda: page.update()
        self.close = lambda: page.window_close()

        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.window_height = page.window_min_height = 610
        page.window_width = page.window_min_width = 860
        page.scroll = ft.ScrollMode.AUTO
        page.spacing = 40
        page.title = "QuickTest"

        page.on_keyboard_event = self.on_keyboard
        page.add(*self.UI)