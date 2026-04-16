import subprocess
import os

def git_pull_reset_hard(url, local_dir=None):
    """
    Cloner si le dépôt local n'existe pas, sinon pull + reset --hard.
    """
    if local_dir is None:
        local_dir = os.path.basename(url.rstrip("/").replace(".git",""))

    if not os.path.exists(local_dir):
        subprocess.run(["git", "clone", url, local_dir], check=True)
        print(f"Dépôt cloné dans {local_dir}")
    else:
        subprocess.run(["git", "-C", local_dir, "pull"], check=True)
        subprocess.run(["git", "-C", local_dir, "reset", "--hard"], check=True)
        print(f"Dépôt '{local_dir}' mis à jour avec reset --hard")