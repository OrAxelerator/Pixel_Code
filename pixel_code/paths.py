# TO USE FOR v4.1.x or v0.5.0 cause it's better
from platformdirs import user_data_dir, user_config_dir
from pathlib import Path

APP_NAME = "Pixel_Code"
APP_AUTHOR = "OrAxelerator"  # ou ton nom

DATA_DIR = Path(user_data_dir(APP_NAME, APP_AUTHOR))
CONFIG_DIR = Path(user_config_dir(APP_NAME, APP_AUTHOR))

DATA_DIR.mkdir(parents=True, exist_ok=True)
CONFIG_DIR.mkdir(parents=True, exist_ok=True)

PROJECTS_JSON = DATA_DIR / "projects.json"
PARAMETRES_JSON = CONFIG_DIR / "parametres.json"