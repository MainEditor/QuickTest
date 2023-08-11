import GUI_handler.select_window
import GUI_handler.statistics_window
import GUI_handler.window
from data_handler.data_writer import write_statistics

def main():
    while True:
        select_window = GUI_handler.select_window.DataSelector()
        if select_window.GO_TO == "STAT":
            statistics = select_window.statistics
            topic = select_window.topic
            stat_window = GUI_handler.statistics_window.StatWindow(statistics, topic)
            if not stat_window.NEED_RETURN:
                return 0
        elif select_window.GO_TO == "TEST":
            data = select_window.data
            main_window = GUI_handler.window.MainWindow(data)
            write_statistics(data[2], main_window.progressBar.value)
            if not main_window.NEED_RETURN:
                return 0
        elif select_window.GO_TO == None:
            return 0

main()