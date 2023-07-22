import flet as ft
import os
from pathlib import Path
from random import choice, shuffle, randint
from fnmatch import fnmatch

def file_not_found(page: ft.Page):
	page.bgcolor = 'RED'
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.spacing = 55
	page.title = "QuickTest"
	page.window_maximizable = False
	page.window_resizable = False
	page.window_height = 500
	page.window_width = 800
	page.add(ft.Text("Файл c вопросами не найден!", size = 50), ft.Text("Убедитесь, что существует файл 'questionsN.txt' в папке 'Документы'.", scale = 1.2))

def select(page: ft.Page):
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.spacing = 20
	page.title = "QuickTest"
	page.window_maximizable = False
	page.window_resizable = False
	page.window_width = 500
	page.scroll = ft.ScrollMode.HIDDEN 

	buttons = []
	data = dict()

	def click(e):
		subject_selected = e.control.text
		global file, subject_final
		file = data[subject_selected]
		subject_final = subject_selected
		page.window_close()

	for path in files:
		cur_file = open(path, encoding = 'utf-8')
		subject = cur_file.readline().strip()
		data[subject] = [x.strip('\n').strip('	').split('	') for x in cur_file.readlines()]
		buttons += [ft.OutlinedButton(subject, on_click = click, scale = 1.5)]
	
	text = ft.Text("Выберите необходимую тему из списка:", size = 24)
	
	page.add(text, *buttons)

home_dir = str(Path.home()) + "\\Documents\\"
files = [home_dir + f"\{f}" for f in os.listdir(home_dir) if fnmatch(f, "questions*.tsv")]

if len(files) >= 2:
	ft.app(target = select)
elif len(files) == 1:
	file = open(files[0], encoding = 'utf-8')
	subject_final = file.readline().strip()
	file = [x.strip('\n').strip('	').split('	') for x in file.readlines()]
	print(file)

count_correct = 0
count_wrong = 0
index = 0

if 'file' in globals():
	shuffle(file)
	question = file[index][0]
	answer = file[index][1]
	wrong_answer = choice(file[index][2:])

def update_data():
	global index, question, answer, wrong_answer
	if index < len(file) - 1:
		index += 1
	else:
		shuffle(file)
		index = 0
	question = file[index][0]
	answer = file[index][1]
	wrong_answer = choice(file[index][2:])

def main(page: ft.Page):
	def choose_button_randomly():
		if randint(0, 1):
			btn1.content.value, btn2.content.value = answer, wrong_answer
		else:
			btn1.content.value, btn2.content.value = wrong_answer, answer

	def update_GUI(is_correct: bool):
		question_text.value = question
		choose_button_randomly()
		pb.value = count_correct / (count_wrong + count_correct)
		counter.value = f'ВЕРНО👍        {count_correct} : {count_wrong}        👎НЕВЕРНО'
		if is_correct:
			banner.value, banner.bgcolor = "ВЕРНО", "green"
		elif not is_correct:
			banner.value, banner.bgcolor = "НЕВЕРНО", "red"
		page.update()

	def click_left(e):
		global count_correct, count_wrong
		is_correct = btn1.content.value == answer
		count_correct += is_correct
		count_wrong += not is_correct
		update_data()
		update_GUI(is_correct)

	def click_right(e):
		global count_correct, count_wrong
		is_correct = btn2.content.value == answer
		count_correct += is_correct
		count_wrong += not is_correct
		update_data()
		update_GUI(is_correct)

	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.scroll = ft.ScrollMode.ADAPTIVE 
	page.spacing = 40
	page.padding = 20
	page.title = "QuickTest"
	# page.window_maximizable = False
	# page.window_resizable = False
	page.window_height = 525
	page.window_width = 825

	button_style = ft.ButtonStyle(shape = ft.RoundedRectangleBorder(radius=10), elevation = 5)

	question_text = ft.Text(question, text_align = "center", size = 35)
	banner = ft.Text("НАЧИНАЙ!", color = "white", size = 30)
	counter = ft.Text(f'ВЕРНО👍        {count_correct} : {count_wrong}        👎НЕВЕРНО', size = 20)
	btn1 = ft.ElevatedButton(style = button_style, content = ft.Text(answer, size = 23), on_click = click_left)
	btn2 = ft.ElevatedButton(style = button_style, content = ft.Text(wrong_answer, size = 23), on_click = click_right)
	row = ft.Row(wrap = True, alignment = ft.MainAxisAlignment.CENTER, controls = (ft.Text("←", size = 40), btn1, ft.Text("или", scale = 1.2), btn2, ft.Text("→", size = 40)))
	
	pb = ft.ProgressBar(height = 5, width = 500, color = "#70b658", bgcolor = "#eb4540")

	def on_keyboard(e: ft.KeyboardEvent):
		if e.key == "Arrow Left":	click_left(None)
		elif e.key == "Arrow Right":	click_right(None)

	page.on_keyboard_event = on_keyboard

	page.add(banner, counter, question_text, row, pb, ft.Text(subject_final))

if 'file' in globals():
	ft.app(target = main)
elif len(files) == 0:
	ft.app(target = file_not_found)
else:
	...
