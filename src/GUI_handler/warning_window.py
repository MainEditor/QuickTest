import flet as ft

def warning_window(page: ft.Page) -> None:
    page.bgcolor = 'RED'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing = 55
    page.title = "QuickTest"
    page.window_height = 500
    page.window_width = 800
    page.add(ft.Text(messege, size = 50), ft.Text(instruction, scale = 1.2))

def create_warning_window(main_messege, instruction_messege):
    global messege, instruction
    messege, instruction = main_messege, instruction_messege
    ft.app(target = warning_window)