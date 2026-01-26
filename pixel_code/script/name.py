import os
from pathlib import Path


def is_dir_empty(dir: str) -> bool:
    """return True if dir is in current directorie"""
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    dir_path = BASE_DIR
    files_dir = [
        f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))
    ]
    return True if dir in files_dir else False

#print(is_dir_empty("trophee-nsi-ant"))

#print(files)
# ['file2.txt', 'dir2', 'file3.jpg', 'file1', 'dir1']

#for el in files:
  #  print(el)
 #   print(files)