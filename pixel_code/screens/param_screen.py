import curses
from pathlib import Path
import json
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_JSON = BASE_DIR / "data/projects.json"
PARAMETRES_JSON   = BASE_DIR  / "data/parametres.json"


class ParamScreen:
    def __init__(self, main_app):
        self.main_app = main_app
        h, w = main_app.stdscr.getmaxyx()

        self.win = curses.newwin(h-10, w, 10, 0)
        self.win.clear()
        self.win.border()
        self.win.refresh()
        self.array = ["option1", "option2", "option3", "option4"]
        self.language = None# load in load_param() 

        self.settings_config = [
            {
                "key": "language",
                "type": "cycle",
                "values": ["en", "fr"],
                "section":"app"
            },
            {
                "key": "use_nerd_font",
                "type": "toggle",
                "section":"app"
            },
            
            {
                "key": "editor",
                "type": "cycle",
                "values": ["code", "vim", "cmd"],
                "section":"projects"
            },
            {
                "key": "repo",
                "type": "cycle",
                "values": ["github", "null"],
                "section":"projects"
            },
            {
                "key": "check_update_at_launch",
                "type": "toggle",
                "section":"app"
            },
            {
                "key": "logo",
                "type": "cycle",
                "values": ["center", "left"],
                "section":"ui"
            },
            {
                "key": "version",
                "type": "readonly",
                "section":"app"
            }
        ]
        # ---------------

        self._selection_parametre = 0

        
        self.data = self.main_app.param_manager.data #data



    def get_selection_parametre(self):
        return self._selection_parametre

    def get_language(self):
        return self.data["app"]["language"]


    def display(self):
        self.win.clear()

        max_y, max_x = self.win.getmaxyx()

        self.parametre_array = [
            self.data["app"]["language"],
            self.data["app"]["use_nerd_font"],
            self.data["projects"]["editor"],
            self.data["projects"]["repo"],
            self.data["app"]["check_update_at_launch"],
            self.data["ui"]["logo"],
            self.data["app"]["version"]
        ]
        # * langage
        # * icone (NF)
        # * affichage (side, bottom)
        # * editor (code, vim, cmd)
        # * check update at lauch
        # * logo (left, center)
        parametre_consigne = {
            "en": ["Language", "Use Nerd Font",  "Editor", "Repo", "Check update at lauch", "Logo", "Actual versions"],
            "fr": ["Langage", "Utiliser Nerd Font", "Editeur", "Depo", "Regarder update au lancement", "Logo", "Version actuelle"]
        }

        caract = ["", "▶"]
        WIDTH = 48
        HEIGHT = len(self.parametre_array) + 4

        lang = "fr" if self.data["app"]["language"] == "fr" else "en"

        self.win.box()

        start_y = (max_y - HEIGHT) // 2
        start_x = (max_x - WIDTH) // 2

        self.win.addstr(start_y + 0, start_x+2, "================== PARAMÈTRES ==================")

        for i in range(len(self.parametre_array)):
            arrow = (i == self._selection_parametre)
            self.win.addstr(
                start_y + i + 1,
                start_x + 2,
                f'{caract[arrow]}  {parametre_consigne[lang][i].ljust(WIDTH - len(str(self.parametre_array[i])) + (0 if arrow else 1) - 3)}{self.parametre_array[i]}'
            )

        self.win.addstr(start_y + len(self.parametre_array) + 1, start_x+2, "-" * WIDTH)
        txt = {
            "en":["Navigation", "Change", "Quit"],
            "fr":["Navigation", "Changer", "Quitter"]
        }
        key = {
            "en":"SPACE BAR",
            "fr":"ESPACE"
        }
        

        self.win.addstr(
            start_y + len(self.parametre_array) + 2,
            start_x,
            f"{txt[lang][0]} : ↑/↓    {txt[lang][1]} : {key[lang]}    {txt[lang][2]} : p"
        )

        self.win.refresh()

    def change_value(self, i):
        setting = self.settings_config[i]
        key = setting["key"]

        if setting["type"] == "toggle":
            self.data[setting["section"]][key] = not self.data[setting["section"]][key]

        elif setting["type"] == "cycle":
            values = setting["values"]
            current = self.data[setting["section"]][key]
            idx = values.index(current)
            self.data[setting["section"]][key] = values[(idx + 1) % len(values)]

        elif setting["type"] == "readonly":
            pass

    
    def move_up(self):
        self._selection_parametre = max(0, self._selection_parametre -1)
    
    def move_down(self):
        self._selection_parametre = min(len(self.parametre_array)-1, self._selection_parametre + 1)



    def load_param(self):
        try:
            with open(PARAMETRES_JSON, encoding="utf-8") as f:
                data = json.load(f)

                if 'app' in data:
                    self.language = data['app'].get('language')
                    self.use_nerd_font = data['app'].get('use_nerd_font', self.use_nerd_font)
                    self.version = data['app'].get('version', self.version) # Cause in v0.1.1 parametres.json there is no argument "version" but "versionS" so since v0.1.2 it's "version"
                    self.check_update_at_launch = data['app'].get('check_update_at_launch', self.check_update_at_launch)
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
        self.main_app.param_manager.save_param()