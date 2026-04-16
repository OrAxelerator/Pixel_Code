from pathlib import Path
import json

from pixel_code.utils.translate import translate
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PROJECTS_JSON = BASE_DIR / "data/projects.json"
PARAMETRES_JSON   = BASE_DIR  / "data/parametres.json"

#print(BASE_DIR)


class ParamManager():
    def __init__(self):
        
        self.data = {} # to load
        self.load_param()
        #print(self.data)
        # self.language = "en" # Default value if error to read parametre.json
        # self.use_nerd_font = False
        # self.version = None
        # self.check_update = True
        # self.allow_prerelease = True

        # # "ui"
        # self.theme = "default"

        # # "projects"
        # self.sort_by_last_opened = True
        # self.sort_by_name = False
        # self.editor = "code"
        
        # self.last_version = None # To load from github
                 
        #self.parametre_array = [self.language, self.use_nerd_font, self.version] #here to get len() on setter

    def load_param(self):
        default_data = {
            "app": {
                "language": "en",
                "use_nerd_font": False,
                "version": None,
                "check_update_at_launch": True,
                "allow_prerelease": True,
            },
            "ui": {
                "theme": "default",
                "logo":"center",
                "display_project":"side"
            },
            "projects": {
                "sort_by_last_opened": False,
                "sort_by_name": True,
                "editor": "code",
            },
        }

        try:
            with open(PARAMETRES_JSON, encoding="utf-8") as f:
                file_data = json.load(f)
        except FileNotFoundError:
            print("no foud")
            file_data = {}

        
        self.data = default_data
        for section in default_data:
            if section in file_data:
                self.data[section].update(file_data[section])
        

    def get_data(self, key_section:str, key:str):
        if key_section in self.data.keys():
            if key in self.data[key_section].keys():
                return self.data[key_section][key]
            else:
                print("key not found")
        else:
            print("key section not found")


    def save_param(self):
        data_to_save = self.data.copy()
        with open(PARAMETRES_JSON, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False)

# a = ParamManager()  
# a.get_data("apeeep", "version")
# print(a.get_data("app", "version"))
