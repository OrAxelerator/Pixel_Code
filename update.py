import os
import shutil
import zipfile
import tempfile
import requests

# ---------------- CONFIG ----------------
REPO = "OrAxelerator/Pixel_Code"
URL = f"https://api.github.com/repos/{REPO}/releases"

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
print("root dir : ", ROOT_DIR)
# ----------------------------------------



import zipfile
from pathlib import Path

def extract_zip(zip_path, extract_dir):
    extract_dir = Path(extract_dir)
    extract_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(extract_dir)

def get_latest_version():
    r = requests.get(URL)
    releases = r.json()

    print(releases[0]["tag_name"])      # la plus récente, même si c'est une prerelease
    print(releases[0]["prerelease"])    # True ou False

    # return {
    #     "prerelease" : releases[0]["prerelease"],
    #     "tag_name" : releases[0]["tag_name"]
    # }

    return releases[0]





def download_last_version() -> str:

    latest = get_latest_version()
    zip_url = latest["zipball_url"]
    response = requests.get(zip_url)
    # print(response.content) #random stuff in hex
    with open("update/latest.zip", "wb") as f:
        f.write(response.content)

    print(type(ROOT_DIR))

    return ROOT_DIR + "/update/latest.zip"


import shutil
import shutil
from pathlib import Path

def delete_everything(path):
    path = Path(path)

    if not path.exists():
        return

    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()


def clean_project():
    for item in os.listdir(ROOT_DIR):
        if item in (".git", "update.py", "update", "pixel_code.egg-info"):
            pass
        else:
        #else
            path = os.path.join(ROOT_DIR, item)
            print("DELETE" , path)
            delete_everything(path)



from pathlib import Path
import shutil


def restore_update(update_folder):
    update_folder = Path(update_folder)
    dst = Path(ROOT_DIR)

    print(f"update folder : {update_folder}")
    print(f"dst : {dst}")

    for item in update_folder.iterdir():
        print(item)
        if any(x in str(item) for x in [".git", "update.py", "update"]):
            pass
        else:
            shutil.move(str(item), str(dst / item.name))



def main():
    from pathlib import Path
    
    zip_path = download_last_version()  # IMPORTANT: doit retourner le path du zip
    

    extract_dir = Path(ROOT_DIR + "/update")
    print(extract_dir)
    
    # attendre / garantir extraction faite AVANT
    extract_zip(zip_path, extract_dir)
    # 
    folders = [p for p in extract_dir.iterdir() if p.is_dir()]

    if not folders:
        raise RuntimeError("Aucun dossier extrait trouvé")

    print(type(folders))  # list

    # prendre le bon dossier (souvent 1 seul dans un zip GitHub)
    root_folder = folders[0]

    print("root folder:", root_folder)

    print("---------")
    clean_project()
    print("---------")


    restore_update(root_folder)


