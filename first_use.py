from pixel_code.script.add_project import create_pixelcode_config
from pixel_code.script.add_project_global import add_project_global
from pathlib import Path
from pixel_code.paths import PROJECTS_JSON, PACKAGE_DIR, APP_VERSION
from pixel_code.script.data.param_manager import ParamManager
from pixel_code.utils.translate import translate

PACKAGE_DIR = PACKAGE_DIR.parent # Go to root of projet

lang = ParamManager().get_data("app", "language")
print(translate({"en": f"Thanks for installing Pixel_Code v{APP_VERSION}", "fr": f"Merci d'avoir installé Pixel_Code v{APP_VERSION}"}, lang))


# blanck_project = {
#     "id": "79b38223",
#     "path":ROOT,
#     "status":"todo"
# }

blanck_project = {
    "name": "Pixel_code",
    "description": "Super COOL TUI build by OrAxelerator, you can delete this project by using 'd' on it.",
    "languages": [
        "python", "json"
    ],
    "path": f"{PACKAGE_DIR}",
    "repo": "https://github.com/OrAxelerator/Pixel_Code.git"
}
if not create_pixelcode_config(blanck_project): # .pixelcode.json already exist
    config_file = PACKAGE_DIR / ".pixelcode.json"
    print(translate({"en": f"Error, {config_file} already exists, delete it and run first_use.py again.", "fr": f"Erreur, {config_file} existe déjà, supprimez-le et relancez first_use.py."}, lang))

add_project_global(PROJECTS_JSON, str(PACKAGE_DIR))
                   
