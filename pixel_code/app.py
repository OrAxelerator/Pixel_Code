import os
import sys
import json
import subprocess
import requests # Not standar library : in project.toml

# Détection of the keybord acording to the OS
if os.name == "nt":# Windows ..
    import msvcrt
else:
    import termios
    import tty

import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

LOGO_TXT   = BASE_DIR / "logo.txt"
PROJECTS_JSON = BASE_DIR / "projects.json"
PARAMETRES_JSON   = BASE_DIR / "parametres.json"



# todo :
#   - sys of pip => installer.py
#   - make option to add pixelcode.json so when install new code VIA pixel_code pop to add project on fork on pixel code
#   -  make something cool with nerd font for icon
#   -  think about integration in pixel_nav => pixelcode.json ? ..
#   -  clearFormLine(line=12) hard-coded => bad, calcule height of logo ?
#   -  getKey need to be centraliser
#   - do function shortentext for pwd or descripttion too long
#   - programme de mise a jour automatique
#   - Do something cleaner at change_value() in Param
#   - Improve translate systeme ... 
#   - projet.json : icone = ["":iconed de base, "favortite : icone + cœur, "]
#   - Use quit() func in main  instead of break in code

# coeur : 󱃪
# side project : 󰉌
# add folder : 

# icone (NF) : https://www.nerdfonts.com/cheat-sheet

# Call the code : "pixel-code"

# on macOs : pip install -e .
# on Ubuntu use pipx and write : pipx install . 
# on Windows 11 ... go see the README

# CONST
# Styles ANSI #Do ANSI.py for later ??
BOLD = "\033[1m"
BLUE = "\033[34m"
GRAY = "\033[90m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


#put this in main ?
def get_key():
    """
    - "UP" for ^
    - "DOWN" for ˅
    - "q" for quit
    - None for others ...
    """
    if os.name == "nt":  # Windowsn WORK ?
        key = msvcrt.getch()
    # touches simples
        if key == b'q':
            return "q"
        elif key == b'p':
            return "p"
        elif key == b' ':
            return "SPACE"
        elif key == b'h':
            return "h"
        elif key == b'r':
            return "r"
        elif key == b'e':
            return "e"
        elif key == b'\r':   # ENTRÉE
            return "ENTER"

        # touches spéciales (flèches)
        elif key == b'\xe0':
            key = msvcrt.getch()
            if key == b'H':
                return "UP"
            elif key == b'P':
                return "DOWN"

        return None
    else:  # Linux / macOS
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch1 = sys.stdin.read(1)

            # Détection touche Entrée
            if ch1 in ('\n', '\r'):
                return "ENTER"
            
            if ch1 == 'q':
                return "q"
            if ch1 == 'h':
                return "h"
            if ch1 == 's':
                return "s"
            elif ch1 == 'r':
                return "r"
            elif ch1 == 'e':
                return "e"
            elif ch1 == 'p':
                return "p"
            elif ch1 == ' ':
                return "SPACE"
            elif ch1 == '\x1b':  # séquence ANSI pour flèches
                ch2 = sys.stdin.read(1)
                ch3 = sys.stdin.read(1)
                if ch3 == 'A':
                    return "UP"
                elif ch3 == 'B':
                    return "DOWN"
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None




class Main:
    def __init__(self):
        self._selection = 0
        self.projets = {}
        self.projectsArray = []
        self.show_details = False 

        self.current_screen = "main" # > ["main", "parametre"]

        self.parametre = Param(self)
        self.parametre.load_param()
        self.language = None # Param 
        self.run()

    def run(self):
        # Lauch app

        # INIT ---------
        
        self.clear_terminal() # Voir si peut faire autrement ..
        self.load_projects()
        self.display_logo()
        self.display_projects()
        self.get_update() # 

        while True:
            key = get_key()
            if key == "q": # Always
                if self.parametre.language == "en":
                    print("End of programme")
                else :
                    print("Fermeture du programme...")
                break
                
            elif self.current_screen == "main" : # Interface of Main
                
                if key == "UP" :
                    #main.show_details = not main.show_details if main.show_details else main.show_details
                    self.move_up()
                    self.clear_from_line()
                    self.display_projects()
                elif key == "DOWN":
                    self.move_down()
                    self.clear_from_line()
                    self.display_projects()
                elif key == "ENTER": 
                    self.projectsArray[self.selection].open_project()
                elif key == "h":
                    self.help()
                elif key == "e":
                    self.projectsArray[self.selection].edit_project()
                elif key == "p": # Parametre off app
                    self.clear_from_line()
                    self.current_screen = "parametre"
                    self.parametre.selection_parametre = 0 # Alwyas start slection at 0
                    self.parametre.display_parametre()
                elif key == "SPACE":
                    self.toggle_view()
                    self.clear_from_line() # To opti bcs 2 time projectS
                    self.display_projects()
                elif key == "r": # Reload all
                    self.clear_terminal() # Clear all to reload logo too
                    self.__init__()
                    self.load_projects()
                    self.display_logo()
                    self.display_projects()
            elif self.current_screen == "parametre" : # Interface of Parametre
                if key == "DOWN" :
                    self.move_down()
                    self.clear_from_line()
                    self.parametre.display_parametre()
                elif key == "UP" :
                    self.move_up()
                    self.clear_from_line()
                    self.parametre.display_parametre()
                elif key == "SPACE": # Change value
                    self.parametre.change_value(self.parametre.selection_parametre)
                    self.clear_from_line()
                    self.parametre.display_parametre()   
                elif key == "p":
                    self.parametre.save_param()
                    self.current_screen = "main"            
                    self.clear_from_line()
                    self.display_projects()
                    
            else:
                print("key ignored")





















        

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, value):
        if len(self.projectsArray) == 0:  # Évite les erreurs si la liste est vide
            self._selection = 0
        elif value < 0:
            self._selection = 0
        elif value >= len(self.projectsArray):
            self._selection = len(self.projectsArray) - 1
        else:
            self._selection = value


    def tr(self): # Translate function
        return 0 if self.language == "fr" else 1

    def help(self):
        help_message = ["""
Keybinds :
    q : Quit
    ↑/↓ : Navigation
    p : Open parametre
    r : refresh display (only work for screen main)
    e : edit project inside Pixel_Code (doesnt work for the moment)
   ESPACE : Change a parametre
""",
"""
Raccourci clavier :
    q : Quitter
    ↑/↓ : Navigation
    p : ouvrir les parametres
    r : rafraichir l'affichage (marche seulement sur main)
    e : chager les info sur un projet (marche pas pour le moment)
   ESPACE : Changer un parametre
"""
]
        help_message[0] if self.parametre.language == "en" else help_message[1]
        print(help_message[0] if self.parametre.language == "en" else help_message[1])

    def display_logo(self): # Static
            try:
                with open(LOGO_TXT, encoding="utf-8") as l:
                    logo = l.read()
                    print()
                    print(logo)
                    print("_____________________________________________________________________________________")
                    print()
            except FileNotFoundError:
                print("Logo introuvable.")
                

    def clear_terminal(self):
        if os.name == "nt": # work ??
            os.system("cls")
        else:
            os.system("clear")

    def clear_from_line(self, line=12): 
        """line = 12 (height of static render : logo.txt)"""
        print(f"\033[H\033[{line}B\033[J", end="")

    def move_up(self):
        if self.current_screen == "main":
            self.selection = self._selection - 1  # Utilisation du setter
        elif self.current_screen == "parametre":
            self.parametre.selection_parametre = max(0, self.parametre.selection_parametre - 1)

    def move_down(self):
        if self.current_screen == "main":
            
            self.selection = self._selection + 1  # Utilisation du setter
            
        elif self.current_screen == "parametre":
            self.parametre.selection_parametre =  min(self.parametre.selection_parametre +1, 2)


    def enter(self): # supr ?
        pass

    def quit(self):
        pass

    def edit(self):# supr ?
        pass

    def load_projects(self):
        try:
            with open(PROJECTS_JSON, encoding="utf-8") as f:
                self.projets = json.load(f)
                
                for i in range(len(self.projets)): #recup tout les prjet en tant que class dans projetArray
                    self.projectsArray.append(Project(self, str(i), self.projets))
        except FileNotFoundError:
            print("Fichier projets.json introuvable.")
            # self.projet = {} so..


    def display_projects(self): # Not static
        for i, project in enumerate(self.projectsArray):
            if self.selection == i and self.show_details: # Works
                project.display_project_full(selected_index=self.selection, my_index=i)
            else :
                project.display_project_compacte(selected_index=self.selection, my_index=i)

    def toggle_view(self):
        """Reverse the value of self.show_details"""
        self.show_details = not self.show_details 

    def display_tutorial(self):
        pass # need langague before

    def get_update(self):
        url = "https://api.github.com/repos/OrAxelerator/Pixel_Code/releases"
        releases = requests.get(url).json()
        for r in releases:
            if r["prerelease"]:
                v = r["tag_name"]
                return v



class Project:
    def __init__(self, main, number, projets):
        self.main = main
        self.number = number
        data = projets[self.number]

        # Infos projet
        self.name = data["name"]
        self.description = data["description"]
        self.languages = " ".join(data.get("programming_languages", []))
        self.pwd = data["pwd"]
        

        # Styles ANSI
        self.Tname = f"{BOLD}{BLUE}{self.name}{RESET}"
        self.Tdescription = f"{GREEN}{self.description}{RESET}"
        self.Tlanguages = f"{YELLOW}{self.languages}{RESET}"
        self.Tpath = f"{GRAY}{self.pwd}{RESET}"

        # Stocke les textes formatés pour affichage
        self.dataAnsiStr = [self.name, self.description, self.languages, self.pwd]
        self.dataAnsi = [self.Tname, self.Tdescription, self.Tlanguages, self.Tpath]

        # NF
        self.icone_folder = ["󰉋", ""] # Need 2 spaces :  CLOSED | OPEN






    def display_project_compacte(self, selected_index, my_index):
        """
        Display the name project
        selected_index : index of the selectioned project
        my_index : index of this project
        """
        nf = self.main.parametre.use_nerd_font # True or False ..    
        arrow = "▶" if selected_index == my_index else ""
        icone = (str(self.icone_folder[0]) + "  ") if nf else ""
        print(arrow + " "+ icone + self.Tname )


    def display_project_full(self, selected_index, my_index):
        carac = ["├─", "└─"]
        lang = 0 if self.main.parametre.language == "fr" else 1
        txt = [["","Descrption : ","Langages  :", "Chemin : " ], ["", "About : ", "Languages : ", "Path : "]] # bofffff
        if not self.main.parametre.use_nerd_font:
            pass
        icone = (str(self.icone_folder[1]) + "  ") if self.main.parametre.use_nerd_font else ""
        print("▼" + " "+icone + self.Tname)
        for  text in self.dataAnsiStr[1::]:
            is_last_index = 1 if self.dataAnsiStr.index(text) == len(self.dataAnsiStr[1::]) else 0
            print("  " + carac[is_last_index] + " "+ txt[lang][self.dataAnsiStr.index(text)] + text)
        
        print()

    def edit_project(self): # change info about prject like the name ...
        print("edit")


    def open_project(self):

        project_path = Path(self.pwd).expanduser().resolve()

        # Chercher la commande "code"
        code_cmd = shutil.which("code")

        if code_cmd:
            subprocess.run([code_cmd, "-n", str(project_path)])
            return

        # Fallback macOS
        if os.name == "posix" and shutil.which("open"):
            subprocess.run(["open", "-a", "Visual Studio Code", str(project_path)])
            return

        raise RuntimeError("VS Code n'est pas trouvé sur ce système")

    def archive(self):
        pass




class Param:
    def __init__(self, main):
        self.main = main
        self._selection_parametre = 0
        self.language = None
        self.use_nerd_font = False
        self.sort_by_name = False
        self.theme = "default"
        self.display_tutorial = False
        self.version = None
        self.details_mode_default = False
        self.truncate_text = True
        self.path_truncate_mode = "middle"
        self.clear_mode = "partial"
        self.auto_reload = False
        self.parametre_array = [self.language, self.use_nerd_font, self.display_tutorial] #here to get len() on setter
        
        # Tableau des paramètres modifiables depuis l'interface
        


    def get_selection_parametre(self):
        return self._selection_parametre
    

    
    def display_parametre(self):
        self.parametre_array = [self.language, self.use_nerd_font, self.display_tutorial] # DONT DELETE => recacule data after load_param()
        parametre_consigne = ["Language", "Use Nerd Font", "Display tutorial at launch", "Sort By Name" ]
        #self.selection_parametre = 0 # Alwyas have selection at the start even after quit,open
        caract = ["", "▶"] # False : "" | True :  "▶"
        WIDTH = 48
        print(self.version)
        print( self.main.get_update())
        if self.version != self.main.get_update():
            print("Nouvelle verions disponilbe")
        else :
            print("Pixel-Code est a jour")
        print()
        print(f"================== PARAMÈTRES ==================")
        for i in range(len(self.parametre_array)):
            arrow = False
            if i == self.selection_parametre:
                arrow = True
            print(f'{caract[arrow]}  {parametre_consigne[i].ljust(WIDTH - len(str(self.parametre_array[i])) + (0 if i == self.selection_parametre else 1) - 3)}{self.parametre_array[i]}')
        print(f"-" * WIDTH)
        txt = [["Navigation", "Change", "Quit"], ["Navigation", "Changer", "Quitter"]]
        lang = 1 if self.language == "fr" else 0 # Do func ?
        print(f"{txt[lang][0]} : ↑/↓    {txt[lang][1]} : SPACE    {txt[lang][2]} : p")
        


    def load_param(self):
        try:
            with open(PARAMETRES_JSON, encoding="utf-8") as f:
                data = json.load(f)

                # Parcours des sections et assignation des valeurs aux variables correspondantes
                if 'app' in data:
                    self.language = data['app'].get('language')
                    self.use_nerd_font = data['app'].get('use_nerd_font', self.use_nerd_font)
                    self.display_tutorial = data['app'].get('display_tutorial', self.display_tutorial)
                    self.theme = data['app'].get('theme', self.theme)
                    self.version = data['app'].get('version') # Cause in v0.1.1 parametres.json there is no argument "version" but "versionS" so since v0.1.2 it's "version"

                if 'ui' in data:
                    self.details_mode_default = data['ui'].get('details_mode_default', self.details_mode_default)
                    self.truncate_text = data['ui'].get('truncate_text', self.truncate_text)
                    self.path_truncate_mode = data['ui'].get('path_truncate_mode', self.path_truncate_mode)
                    self.clear_mode = data['ui'].get('clear_mode', self.clear_mode)

                if 'projects' in data:
                    self.auto_reload = data['projects'].get('auto_reload', self.auto_reload)
                    self.sort_by_name = data['projects'].get('sort_by_name', self.sort_by_name)

        except FileNotFoundError:
            print("Fichier de paramètres introuvable.")

    def change_value(self, i):
        
        
        if i == 0:
            self.language = "fr" if self.language == "en" else "en"
        elif i == 1:
            self.use_nerd_font = not self.use_nerd_font
        elif i == 2:
            self.display_tutorial = not self.display_tutorial 



    def save_param(self):
        data = {
            'app': {
                'language': self.language,
                'use_nerd_font': self.use_nerd_font,
                'display_tutorial': self.display_tutorial,
                'theme': self.theme
            },
            'ui': {
                'details_mode_default': self.details_mode_default,
                'truncate_text': self.truncate_text,
                'path_truncate_mode': self.path_truncate_mode,
                'clear_mode': self.clear_mode
            },
            'projects': {
                'auto_reload': self.auto_reload,
                'sort_by_name': self.sort_by_name
            }
        }
        with open(PARAMETRES_JSON, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4)
