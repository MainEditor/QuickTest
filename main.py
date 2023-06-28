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

# def utf8_error(page: ft.Page):
# 	page.bgcolor = 'RED'
# 	page.vertical_alignment = ft.MainAxisAlignment.CENTER
# 	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
# 	page.spacing = 55
# 	page.title = "QuickTest"
# 	page.window_maximizable = False
# 	page.window_resizable = False
# 	page.window_height = 500
# 	page.window_width = 800
# 	page.add(ft.Text("Ошибка кодировки файла!", size = 50), ft.Text("Убедитесь, что файл 'questionsN.txt' в папке 'Документы' имеет кодировку UTF.", scale = 1.2))

def select(page: ft.Page):
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.spacing = 20
	page.title = "QuickTest"
	page.window_maximizable = False
	page.window_resizable = False
	page.window_height = 800
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
		data[subject] = [x.strip('\n').split('	') for x in cur_file.readlines()]
		buttons += [ft.TextButton(subject, on_click = click, scale = 1.5)]
	
	text = ft.Text("Выберите необходимую тему из списка:", size = 24)
	
	page.add(text, *buttons)

home_dir = str(Path.home()) + "\\Documents\\"
files = [home_dir + f"\{f}" for f in os.listdir(home_dir) if fnmatch(f, "questions*.tsv")]

if len(files) >= 2:
	ft.app(target = select)
elif len(files) == 1:
	file = open(files[0], encoding = 'utf-8')
	subject_final = file.readline().strip()
	file = [x.strip('\n').split('	') for x in file.readlines()]

shuffle(file)

count_correct = 0
count_wrong = 0
index = 0

if 'file' in globals():
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
			btn1.text, btn2.text = answer, wrong_answer
		else:
			btn1.text, btn2.text = wrong_answer, answer

	def update_GUI(is_correct):
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
		is_correct = btn1.text == answer
		if is_correct:
			count_correct += 1
		else:
			count_wrong += 1
		update_data()
		update_GUI(is_correct)

	def click_right(e):
		global count_correct, count_wrong
		is_correct = btn2.text == answer
		if is_correct:
			count_correct += 1
		else:
			count_wrong += 1
		update_data()
		update_GUI(is_correct)

	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.spacing = 45
	page.title = "QuickTest"
	page.window_maximizable = False
	page.window_resizable = False
	page.window_height = 500
	page.window_width = 800

	question_text = ft.Text(question, size = 35)
	banner = ft.Text("НАЧИНАЙ!", color = "white", size = 30, bgcolor = "")
	counter = ft.Text(f'ВЕРНО👍        {count_correct} : {count_wrong}        👎НЕВЕРНО', size = 25)
	btn1 = ft.ElevatedButton(answer, scale = 1.8, on_click = click_left, width = 170, elevation = 10)
	btn2 = ft.ElevatedButton(wrong_answer, scale = 1.8, on_click = click_right, width = 170, elevation = 10)
	row = ft.Row(spacing = 80, alignment = ft.MainAxisAlignment.CENTER, controls = [btn1, ft.Text('или', size = 20), btn2])
	
	pb = ft.ProgressBar(height = 5, width = 500, color = "green", bgcolor = "red")

	page.add(banner, counter, question_text, row, pb, ft.Text(subject_final))


if 'file' in globals():
	ft.app(target = main)
elif len(files) == 0:
	ft.app(target = file_not_found)
else:
	...
