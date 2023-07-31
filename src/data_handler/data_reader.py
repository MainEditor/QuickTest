import os
from GUI_handler.select_window import DataSelector
from pathlib import Path
from fnmatch import fnmatch

def get_data() -> tuple:
    questions_dir = str(Path.home()) + "\\Documents\\QuickTest\\"
    Path(questions_dir).mkdir(exist_ok=True)
    files_paths = [questions_dir + f"\{file_path}" for file_path in os.listdir(questions_dir) if fnmatch(file_path, "questions*.tsv")]
    return DataSelector().select_topic(files_paths)