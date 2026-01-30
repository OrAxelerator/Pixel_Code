import os
import shutil
import zipfile
import tempfile
import requests

# ---------------- CONFIG ----------------
REPO = "OrAxelerator/Pixel_Code"
GITHUB_API_RELEASE = f"https://api.github.com/repos/{REPO}/releases/latest"

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

FILES_TO_KEEP = [
    os.path.join("data", "parametres.json"),
    os.path.join("data", "archives.json"),
]
# ----------------------------------------


def download_latest_release():
    response = requests.get(GITHUB_API_RELEASE, timeout=15)
    response.raise_for_status()
    return response.json()["zipball_url"]


def backup_files(temp_dir):
    saved = {}
    for rel_path in FILES_TO_KEEP:
        abs_path = os.path.join(ROOT_DIR, rel_path)
        if os.path.exists(abs_path):
            dest = os.path.join(temp_dir, rel_path)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(abs_path, dest)
            saved[rel_path] = dest
    return saved


def restore_files(saved_files, temp_dir):
    for rel_path, _ in saved_files.items():
        src = os.path.join(temp_dir, rel_path)
        dst = os.path.join(ROOT_DIR, rel_path)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)


def clean_project():
    for item in os.listdir(ROOT_DIR):
        if item in (".git", "update.py"):
            continue
        path = os.path.join(ROOT_DIR, item)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


def extract_release(zip_url, extract_to):
    zip_path = os.path.join(extract_to, "release.zip")
    with requests.get(zip_url, stream=True, timeout=30) as r:
        r.raise_for_status()
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

    # Le zip GitHub contient un dossier racine unique
    extracted_root = os.path.join(
        extract_to,
        os.listdir(extract_to)[0]
    )
    return extracted_root


def copy_new_version(src):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(ROOT_DIR, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)


def main():
    print("Téléchargement de la dernière release...")
    zip_url = download_latest_release()

    with tempfile.TemporaryDirectory() as temp:
        print("Sauvegarde des fichiers utilisateur...")
        saved_files = backup_files(temp)

        print("Extraction de la release...")
        extracted = extract_release(zip_url, temp)

        print("Nettoyage de l'ancien projet...")
        clean_project()

        print("Installation de la nouvelle version...")
        copy_new_version(extracted)

        print("Restauration des paramètres...")
        restore_files(saved_files, temp)

    print("Mise à jour terminée avec succès.")
