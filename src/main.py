import GUI_handler.window
import GUI_handler.warning_window

try:
    GUI_handler.window.start_test()
except Exception as e:
    GUI_handler.warning_window.create_warning_window("ПРОИЗОШЛА НЕПРЕДВИДЕННАЯ ОШИБКА!", f"Отпаравьте скриншот этого окна автору и опишите ситуацию возникновения ошибки, пожалуйста.\n{str(e)}")