from pixel_code.script.add_project import create_pixelcode_config
from pixel_code.script.add_project_global import add_project_global
from pathlib import Path
from pixel_code.paths import PROJECTS_JSON, PACKAGE_DIR

PACKAGE_DIR = PACKAGE_DIR.parent # Go to root of projet

print("Thanks for installing Pixel_Code v0.5.0")


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
    print("error, .pixelcode.json file should not be there, delete it")
    print(f'Do : rm ~/{PACKAGE_DIR} on macos/linux')
    print("windows : ")

add_project_global(PROJECTS_JSON, str(PACKAGE_DIR))
                   
