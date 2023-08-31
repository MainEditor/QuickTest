import os
from pathlib import Path
from fnmatch import fnmatch
from string import ascii_lowercase

def get_pathes():
    questions_dir = str(Path.home()) + "\\Documents\\QuickTest\\"
    Path(questions_dir).mkdir(exist_ok=True)
    files_paths = [questions_dir + f"\{file_path}" for file_path in os.listdir(questions_dir) if fnmatch(file_path, "questions*.tsv")]
    for path in files_paths:
        file = [s for s in open(path, 'r').readlines() if s not in ("", "\n", " ", " \n", "	", "	\n")]
        if "STAT" not in file[-1]:
            if file[-1][-1] == '\n':
                file += [f"STAT	"]
            else:
                file += [f"\nSTAT	"]
        open(path, 'w').writelines(file)
    return files_paths