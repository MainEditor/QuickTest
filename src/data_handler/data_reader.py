import os
from pathlib import Path
from fnmatch import fnmatch

def get_pathes():
    questions_dir = str(Path.home()) + "\\Documents\\QuickTest\\"
    Path(questions_dir).mkdir(exist_ok=True)
    files_paths = [questions_dir + f"\{file_path}" for file_path in os.listdir(questions_dir) if fnmatch(file_path, "questions*.tsv")]
    for path in files_paths:
        file = open(path, 'r').readlines()
        if "STAT" not in file[-1]:
            file += [f"\nSTAT	"]
            open(path, 'w').writelines(file)
    return files_paths