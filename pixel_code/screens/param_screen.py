import curses
from pathlib import Path
import json
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_JSON = BASE_DIR / "data/projects.json"
PARAMETRES_JSON   = BASE_DIR  / "data/parametres.json"


class ParamScreen:
    def __init__(self, main_app):
        self.app = main_app
        h, w = main_app.stdscr.getmaxyx()

        self.win = curses.newwin(h-10, w, 10, 0)


        self.array = ["option1", "option2", "option3", "option4"]
        

        # ---------------

        self._selection_parametre = 0

        # "app"
        self.language = "en" # Default value if error to read parametre.json
        self.use_nerd_font = False
        self.version = None
        self.check_update = True
        self.allow_prerelease = True

        # "ui"
        self.theme = "default"

        # "projects"
        self.sort_by_last_opened = True
        self.sort_by_name = False
        self.editor = "code"
        
        self.last_version = None # To load from github
                 
        self.load_param()
        self.parametre_array = [self.language, self.use_nerd_font, self.version] #here to get len() on setter



    def get_selection_parametre(self):
        return self._selection_parametre

    def get_language(self):
        return self.language

    def display_param(self): # to delete
        self.win.clear()
        self.win.addstr(0,0, "PARAM SCREEN")
        for i in range(len(self.parametre_array)):
            self.win.addstr(i+1, 2, f'{self.parametre_array[i]}')

        self.win.refresh()


    def display(self):
        self.win.clear()

        self.parametre_array = [self.language, self.use_nerd_font, self.version ] # DONT DELETE => recacule data after load_param()
        parametre_consigne = [["Language", "Use Nerd Font", "Current version"], ["Langage", "Utiliser Nerd Font", "Version actuelle"]]
        #self.selection_parametre = 0 # Alwyas have selection at the start even after quit,open
        caract = ["", "▶"] # False : "" | True :  "▶"
        WIDTH = 48
        lang = 1 if self.language == "fr" else 0 # Do func ?
        
        self.win.addstr(0, 0, f"================== PARAMÈTRES ==================")
        for i in range(len(self.parametre_array)):
            arrow = False
            if i == self._selection_parametre:
                arrow = True
            self.win.addstr(i+1, 2, f'{caract[arrow]}  {parametre_consigne[lang][i].ljust(WIDTH - len(str(self.parametre_array[i])) + (0 if i == self._selection_parametre else 1) - 3)}{self.parametre_array[i]}')
        self.win.addstr(len(self.parametre_array)+1, 0, f"-" * WIDTH)
        
        txt = [["Navigation", "Change", "Quit"], ["Navigation", "Changer", "Quitter"]]
        key = ["SPACE BAR", "ESPACE"]
        self.win.addstr(len(self.parametre_array)+2, 0, f"{txt[lang][0]} : ↑/↓    {txt[lang][1]} : {key[lang]}    {txt[lang][2]} : p")

        self.win.refresh()


    def change_value(self, i):
        if i == 0:
            self.language = "fr" if self.language == "en" else "en"
        elif i == 1:
            self.use_nerd_font = not self.use_nerd_font
        elif i == 2:
            pass
    
    def move_up(self):
        if len(self.parametre_array) == 0:
            pass
        elif self._selection_parametre - 1 < 0:
            pass
        else:
            self._selection_parametre -= 1
    
    def move_down(self):
        if len(self.parametre_array) == 0:
            pass
        elif self._selection_parametre + 1 >= len(self.parametre_array):
            pass
        else:
            self._selection_parametre += 1



    def load_param(self):
        try:
            with open(PARAMETRES_JSON, encoding="utf-8") as f:
                data = json.load(f)

                if 'app' in data:
                    self.language = data['app'].get('language')
                    self.use_nerd_font = data['app'].get('use_nerd_font', self.use_nerd_font)
                    self.version = data['app'].get('version', self.version) # Cause in v0.1.1 parametres.json there is no argument "version" but "versionS" so since v0.1.2 it's "version"
                    self.check_update = data['app'].get('check_update', self.check_update),
                    self.allow_prerelease = data['app'].get('allow_prerelease', self.allow_prerelease)

                if 'ui' in data:
                    self.theme = data['ui'].get('theme', self.theme)
         

                if 'projects' in data:
                    self.sort_by_last_opened = data['projects'].get('sort_by_last_opened', self.sort_by_last_opened) 
                    self.sort_by_name = data['projects'].get('sort_by_name', self.sort_by_name) 
                    self.editor = data['projects'].get('editor', self.editor)

        except FileNotFoundError:
            print("Fichier de paramètres introuvable.")

    def save_param(self):
        data = {
            'app': {
                'language': self.language,
                'use_nerd_font': self.use_nerd_font,
                'version': self.version,
                'check_update': self.check_update,
                'allow_prerelease': self.allow_prerelease
            },
            'ui': {
                'theme': self.theme,
            },
            'projects': {
                'sort_by_last_opened': self.sort_by_last_opened,
                'sort_by_name': self.sort_by_name,
                'editor': self.editor
            }
        }
        with open(PARAMETRES_JSON, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4)
