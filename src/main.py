import GUI_handler.window
import GUI_handler.warning_window

import flet as ft

try:
    while True:
        window = GUI_handler.window.MainWindow()
        ft.app(target=window.create_window)
        if not window.NEED_RESTART:
            break
except Exception as e:
    if str(e) == "'CurrentData' object has no attribute 'question'":
        pass
    else:
        GUI_handler.warning_window.create_warning_window("ПРОИЗОШЛА НЕПРЕДВИДЕННАЯ ОШИБКА!", f"Отпаравьте скриншот этого окна автору и опишите ситуацию возникновения ошибки, пожалуйста.\n{str(e)}")