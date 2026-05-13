from pixel_code.script.add_project import create_pixelcode_config
from pixel_code.script.add_project_global import add_project_global
import os
from pathlib import Path
import json
from pixel_code.paths import PROJECTS_JSON, PACKAGE_DIR

PACKAGE_DIR = PACKAGE_DIR.parent # Go to root of projet

print("Thanks for installing Pixel_Code v0.4.0")


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
create_pixelcode_config(blanck_project)
add_project_global(PROJECTS_JSON, str(PACKAGE_DIR))
                   
