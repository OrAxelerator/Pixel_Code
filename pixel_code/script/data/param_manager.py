import json

from pixel_code.paths import DEFAULT_PARAMETRES, PARAMETRES_JSON, ensure_user_files


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
        ensure_user_files()
        try:
            with open(PARAMETRES_JSON, encoding="utf-8") as f:
                file_data = json.load(f)
        except FileNotFoundError:
            file_data = {}

        self.data = {
            section: values.copy() if isinstance(values, dict) else values
            for section, values in DEFAULT_PARAMETRES.items()
        }

        if "schema_version" in file_data:
            self.data["schema_version"] = file_data["schema_version"]

        for section in DEFAULT_PARAMETRES:
            if section in file_data:
                if isinstance(self.data[section], dict) and isinstance(file_data[section], dict):
                    self.data[section].update(file_data[section])
                else:
                    self.data[section] = file_data[section]
        

    def get_data(self, key_section:str, key:str):
        if key_section in self.data.keys():
            if key in self.data[key_section].keys():
                return self.data[key_section][key]
            else:
                print("key not found")
        else:
            print("key section not found")


    def save_param(self):
        ensure_user_files()
        data_to_save = self.data.copy()
        with open(PARAMETRES_JSON, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False)

# a = ParamManager()  
# a.get_data("apeeep", "version")
# print(a.get_data("app", "version"))
