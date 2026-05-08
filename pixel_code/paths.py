#CODE by: GPT-5.5 with codex

from platformdirs import user_data_dir, user_config_dir
from pathlib import Path
import json
import shutil

APP_NAME = "Pixel_Code"
APP_AUTHOR = "OrAxelerator"

PACKAGE_DIR = Path(__file__).resolve().parent
PACKAGE_DATA_DIR = PACKAGE_DIR / "data"

USER_DATA_DIR = Path(user_data_dir(APP_NAME, APP_AUTHOR))
USER_CONFIG_DIR = Path(user_config_dir(APP_NAME, APP_AUTHOR))

PROJECTS_JSON = USER_DATA_DIR / "projects.json"
PARAMETRES_JSON = USER_CONFIG_DIR / "parametres.json"
LOG_FILE = USER_DATA_DIR / "debug.log"
LOGO_TXT = PACKAGE_DATA_DIR / "logo.txt"

OLD_PROJECTS_JSON = PACKAGE_DATA_DIR / "projects.json"
OLD_PARAMETRES_JSON = PACKAGE_DATA_DIR / "parametres.json"

DEFAULT_PROJECTS = {
    "schema_version": 1,
    "projects": [],
}

DEFAULT_PARAMETRES = {
    "schema_version": 1,
    "app": {
        "language": "en",
        "use_nerd_font": False,
        "version": "v0.5.0",
        "check_update_at_launch": True,
        "allow_prerelease": True,
    },
    "ui": {
        "theme": "default",
        "logo": "center",
        "display_project": "side",
    },
    "projects": {
        "sort_by_last_opened": False,
        "sort_by_name": True,
        "editor": "code",
        "repo": "github",
    },
}


def _write_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def _copy_old_json_if_needed(old_path: Path, new_path: Path):
    if new_path.exists() or not old_path.exists():
        return

    new_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(old_path, new_path)


def _ensure_schema_version(path: Path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return

    if not isinstance(data, dict) or "schema_version" in data:
        return

    data["schema_version"] = 1
    _write_json(path, data)


def ensure_user_files():
    """Create/migrate user data files outside the installed package."""
    USER_DATA_DIR.mkdir(parents=True, exist_ok=True)
    USER_CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    _copy_old_json_if_needed(OLD_PROJECTS_JSON, PROJECTS_JSON)
    _copy_old_json_if_needed(OLD_PARAMETRES_JSON, PARAMETRES_JSON)

    if not PROJECTS_JSON.exists():
        _write_json(PROJECTS_JSON, DEFAULT_PROJECTS)

    if not PARAMETRES_JSON.exists():
        _write_json(PARAMETRES_JSON, DEFAULT_PARAMETRES)

    _ensure_schema_version(PROJECTS_JSON)
    _ensure_schema_version(PARAMETRES_JSON)
