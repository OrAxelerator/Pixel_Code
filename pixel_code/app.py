import locale
locale.setlocale(locale.LC_ALL, "")

import os
import json
import subprocess
import colorama
import sys
colorama.init()

from pixel_code.script.keybord import get_key
from pixel_code.script.get_update import get_update
from pixel_code.script.is_update_available import is_update_available
from pixel_code.script.translate import translate
from pixel_code.script.terminal.clear_terminal import clear_terminal
from pixel_code.script.terminal.clear_from_line import clear_from_line
from pixel_code.script.git.clone import clone_repo

from pixel_code.script.input_curses import prompt_text_wrapper
from pixel_code.script.input_curses import prompt_text
import curses
from render import Renderer

import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


LOGO_TXT   = BASE_DIR / "data/logo.txt"
PROJECTS_JSON = BASE_DIR / "data/projects.json"
PARAMETRES_JSON   = BASE_DIR  / "data/parametres.json"



# todo :
#   - sys of pip => installer.py
#   - Check if user have wifi
#   - make option to add pixelcode.json so when install new code VIA pixel_code pop to add project on fork on pixel code
#   -  make something cool with nerd font for icon
#   -  think about integration in pixel_nav => pixelcode.json ? ..
#   -  clearFormLine(line=12) hard-coded => bad, calcule height of logo ?
#   - programme de mise a jour automatique
#   - Do something cleaner at change_value() in Param
#   - projet.json : icone = ["":iconed de base, "favortite : icone + cœur, "]
#   - Use quit() func in main  instead of break in code
#   - # Make error message if pwd is False in open_code (Project)
#   - Use import color
#   - Choose IDE 

# coeur : 󱃪
# side project : 󰉌
# add folder : 

# icone (NF) : https://www.nerdfonts.com/cheat-sheet

# Call the code : "pixel-code"

# on macOs : pip install -e .
# on Ubuntu use pipx and write : pipx install . 
# on Windows 11 ... go see the README




class Main:
    def __init__(self):
        import curses
        from render import Renderer
        curses.wrapper(self._start)

    def _start(self, stdscr):
        self.renderer = Renderer(stdscr)

        self._selection = 0
        self.projets = {}
        self.projectsArray = []
        self.show_details = False 
        self.show_git = False

        self.current_screen = "main"

        self.parametre = Param(self)
        self.parametre.load_param()

        self.run()

    #def _start(self, stdscr):
        



    def run(self):
        # Launch app
        self.renderer.clear()  # Clear the screen before starting
        self.renderer.refresh()  # Refresh the screen to show changes

        last_version = get_update()  # Check if user has Wi-Fi
        self.parametre.last_version = last_version

        if is_update_available(self.parametre.version, last_version):
            txt_update = {
                "en": f"[Pixel-Code] A new version is here ({last_version})",
                "fr": f"[Pixel-Code] Une nouvelle mise à jour est disponible ({last_version})"
            }
            txt_pass = {
                "en": "[Enter to pass]",
                "fr": "[Tapez entrer pour passer]"
            }

            self.renderer.addstr(translate(txt_update, self.parametre.language))
            self.renderer.addstr(translate(txt_pass, self.parametre.language))
            self.renderer.refresh()
            self.renderer.getch()
            self.renderer.clear()
            #input(translate(txt_pass, self.parametre.language))

        #clear_terminal()  # Clear terminal after update check
        self.renderer.clear()

        self.load_projects()
        self.display_logo()
        self.display_projects()
        
        

        while True:
            key = get_key()
            if key == "q": # Always check
                clear_terminal()
                last_txt = {
                    "en" : "End of program",
                    "fr" : "Fin du programme"
                }
                print(translate(last_txt, self.parametre.language))
                break
                
            elif self.current_screen == "main" : # Interface of Main
                
                if key == "UP" :
                    #main.show_details = not main.show_details if main.show_details else main.show_details
                    self.move_up()
                    clear_from_line()
                    self.display_projects()
                elif key == "DOWN":
                    self.move_down()
                    clear_from_line()
                    self.display_projects()
                elif key == "ENTER": 
                    self.projectsArray[self.selection].open_project()
                elif key == "h":
                    self.help()
                elif key == "e":
                    self.projectsArray[self.selection].edit_project()
                    print("edit")
                elif key == "p": # Parametre off app
                    clear_from_line()
                    self.current_screen = "parametre"
                    self.parametre.selection_parametre = 0 # Alwyas start slection at 0
                    self.parametre.display_parametre()
                elif key == "SPACE":
                    self.toggle_view()
                    self.show_git = False # toggle
                    clear_from_line() # To opti bcs 2 time projectS
                    self.display_projects()
                elif key == "r": # Reload all
                    clear_terminal() # Clear all to reload logo too
                    self.__init__()
                    self.load_projects()
                    self.display_logo()
                    self.display_projects()
                elif key == "a":
                    self.add_project()
                    clear_from_line()
                    self.display_projects()
                elif key == "d":
                    self.delete_project()
                    clear_from_line()
                    self.move_down() # selection not display
                    self.display_projects()
                elif key == "g":
                    self.show_details = False
                    self.show_git = not self.show_git 
                    clear_from_line()
                    self.display_projects()
                    txt = {"en" : "c : clone \np : git pull\nothers : notihng ",
                           "fr" : "c : clone \np : git pull\autre : rien "
                    }
                    if self.show_git:
                        res = prompt_text_wrapper(translate(txt, self.parametre.language))
                        if res == "c":
                            
                            url = self.projectsArray[self.selection].get_depo_url()
                            if url == None:
                                txt_error = {"en" : "No url found",
                                             "fr": "Aucune url trouvé"}
                            else :
                                clone_repo(url)
                        elif res == "p":
                            from pixel_code.script.git.pull import git_pull
                            dir = self.projectsArray[self.selection].pwd
                            git_pull(dir)
                        else:
                            clear_from_line()
                            self.show_git = False
                            self.display_projects()
            elif self.current_screen == "parametre" : # Interface of Parametre
                if key == "DOWN" :
                    self.move_down()
                    clear_from_line()
                    self.parametre.display_parametre()
                elif key == "UP" :
                    self.move_up()
                    clear_from_line()
                    self.parametre.display_parametre()
                elif key == "SPACE": # Change value
                    self.parametre.change_value(self.parametre.selection_parametre)
                    clear_from_line()
                    self.parametre.display_parametre()   
                elif key == "p":
                    self.parametre.save_param()
                    self.current_screen = "main"            
                    clear_from_line()
                    self.display_projects()
                elif key == "r":
                    self.parametre.__init__(self)
                    clear_terminal()
                    self.display_logo()
                    self.parametre.display_parametre()
                    
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


    def print_bottom_txt(self, txt):
        size = os.get_terminal_size()
        columns = size.columns
        # use curses



    def help(self):
        help_message = ["""
Keybinds :
    q : Quit
    ↑/↓ : Navigation
    p : Open parametre
    r : refresh display (only work for screen main)
    e : edit project inside Pixel_Code (doesnt work for the moment)
    a : add a new project
    d : delete a project
   ESPACE : Change a parametre
""",
"""
Raccourci clavier :
    q : Quitter
    ↑/↓ : Navigation
    p : ouvrir les parametres
    r : rafraichir l'affichage (marche seulement sur main)
    e : chager les info sur un projet (marche pas pour le moment)
    a : ajoutez un projet
    d : suprimmer un projet
   ESPACE : Changer un parametre
"""
]
        print(translate(help_message, self.parametre.language))

    def display_logo(self): # Static
            try:
                with open(LOGO_TXT, encoding="utf-8") as l:
                    logo = l.read()
                    #self.renderer.clear()  # Clear the screen before displaying the logo
                    self.renderer.addstr(logo+"\n")
                    self.renderer.addstr("\n" + "-" * 80 + "\n")  # Add a separator line
                    self.renderer.refresh()  # Refresh to show the logo
            except FileNotFoundError:
                self.renderer.addstr("Logo introuvable.\n")
                self.renderer.refresh()
                





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
        size = os.get_terminal_size()
        height = size.lines
        #print(height)
        for i, project in enumerate(self.projectsArray):
            if i != self.selection:
                project.display_project_compacte(selected_index=self.selection, my_index=i)
            elif  self.selection == i and not self.show_details and not self.show_git:
                project.display_project_compacte(selected_index=self.selection, my_index=i)
            elif self.show_details and i == self.selection:
                project.display_project_full(selected_index=self.selection, my_index=i)
            elif self.show_git and i == self.selection:
                project.display_git()

    def toggle_view(self):
        """Reverse the value of self.show_details"""
        self.show_details = not self.show_details 



    def add_project(self):
        #from input_curses import prompt_text_wrapper
        txt_create_project = {
            "en" : {
                "name" : "Name of the project",
                "description" : "Description of the project",
                "langage" : "Langages (separated by commas)",
                "pwd" : "Directory of the project",
                "repo" : "Url of the github repo"
            },
            "fr" : {
                "name" : "Nom du projet",
                "description" : "Description du projet",
                "langage" : "Langages (séparés par des virgules)",
                "pwd" : "Chemin du projet",
                "repo" : "Url du dépot github"
            }
        }
        try:
            #user_input = prompt_text_wrapper("")
            txt = translate(txt_create_project, self.parametre.language)
            name = prompt_text(self.renderer.stdscr, f"{txt['name']} : ")
            description = prompt_text(self.renderer.stdscr, f"{txt['description']} : ")
            languages = prompt_text(self.renderer.stdscr, f"{txt['langage']} : ").split(',')
            pwd = prompt_text(self.renderer.stdscr, f"{txt['pwd']} : ")
            repo = prompt_text(self.renderer.stdscr, f'{txt["repo"]} : ')
            
           # self.renderer.stdscr.clear()
            
            if pwd == "":
                pwd = os.getcwd()

            with open(PROJECTS_JSON, encoding="utf-8") as f:
                projets = json.load(f)

            new_project = {
                "name": name,
                "description": description,
                "programming_languages": [lang.strip() for lang in languages],
                "pwd": pwd,
                "editor": "code",
                "repo" : repo
            }
            projets[str(len(projets))] = new_project

            with open(PROJECTS_JSON, 'w', encoding="utf-8") as f:
                json.dump(projets, f, indent=4, ensure_ascii=False)


            self.projectsArray.append(Project(self, str(len(projets) - 1), projets))
        except FileNotFoundError:
            print("Fichier projects.json introuvable.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

    def delete_project(self):
        try:
            txt_confirm = {
                "en": f"Do you want to delete {self.projectsArray[self.selection]} : [y/N]",
                "fr": f"Voulez vous supprimer {self.projectsArray[self.selection]} : [y/N]"
            }
            txt_error = {
                "en": "Invalid project number.",
                "fr": "Numéro de projet invalide."
            }
            txt_success = {
                "en": "Project deleted successfully!",
                "fr": "Projet supprimé avec succès !"
            }

            
            project_number = str(self.selection)
            
            res = prompt_text_wrapper(translate(txt_confirm, self.parametre.language))
            if res == "n" or res == "":
                print("no")
                return False
            elif res == "y":
                

                with open(PROJECTS_JSON, encoding="utf-8") as f:
                    projets = json.load(f)

                if project_number not in projets:
                    print(translate(txt_error, self.parametre.language))
                    return

                del projets[project_number]

                projets = {str(i): v for i, v in enumerate(projets.values())}

                with open(PROJECTS_JSON, 'w', encoding="utf-8") as f:
                    json.dump(projets, f, indent=4, ensure_ascii=False)

                print(translate(txt_success, self.parametre.language))

                self.projectsArray = [Project(self, str(i), projets) for i in range(len(projets))]
        except FileNotFoundError:
            print("Fichier projects.json introuvable.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

    def archive(self):
        pass




class Project:
    def __init__(self, main, number, projets):
        self.main = main
        self.number = number

        data = projets[self.number]
        
        self.name = data["name"]
        self.description = data["description"]
        self.editor = data["editor"]
        self.languages = " ".join(data.get("programming_languages", []))
        self.pwd = data["pwd"]
        self.repo = data["repo"]
        

        # Styles ANSI
        self.Tname = f"{colorama.Style.BRIGHT}{colorama.Fore.BLUE}{self.name}{colorama.Style.RESET_ALL}" # mArhce mais galere

        

        self.dataAnsiStr = [self.name, self.description, self.languages, self.pwd]

        # NF
        self.icone_folder = ["󰉋", ""] # Need 2 spaces :  CLOSED | OPEN



    def __str__(self):
        return f"{self.name}"





    def display_project_compacte(self, selected_index, my_index):
        """
        Display the name of the project in a compact format.
        selected_index : index of the selected project
        my_index : index of this project
        """
        nf = self.main.parametre.use_nerd_font  # True or False
        arrow = "▶" if selected_index == my_index else ""
        icone = (str(self.icone_folder[0]) + "  ") if nf else ""
        #self.main.renderer.addstr(f"{arrow}", 0, 11)
        self.main.renderer.addstr(f"     {self.name}", 0, 13+my_index)
        self.main.renderer.addstr(f"  {icone}", 0, 13+my_index)
        self.main.renderer.addstr(f"{arrow}", 0, 13+my_index)
        self.main.renderer.refresh()


    def display_project_full(self, selected_index, my_index):
        carac = ["├─", "└─"]
        lang = 0 if self.main.parametre.language == "en" else 1
        txt = [[ "About", "Languages", "Path"], ["Descrption","Langages", "Chemin" ]] # bofffff
        if not self.main.parametre.use_nerd_font:
            pass

        icone = (str(self.icone_folder[1]) + "  ") if self.main.parametre.use_nerd_font else "" # Some space for the icone
        values = self.dataAnsiStr[1::]
        total = len(values)
        size = os.get_terminal_size()
        columns = size.columns

        for i, values in enumerate(values):
            if i == 0:
                print(f"▼ {icone}{self.Tname}")

            is_last_index = 1 if i == total - 1 else 0 # total - 1 cause values[0] = name 
            if len(values) >= size.columns: # Reduce/shorten path of a project
                part = round(columns * 0.34)
                
                print(f"  {carac[is_last_index]} {txt[lang][i]} : {values[0:part:]}...{values[total - part::]}")
            else :
                print(f"  {carac[is_last_index]} {txt[lang][i]} : {values}")
        
        
        print()

    def display_git(self):
        carac = ["├─", "└─"]
        lang = 0 if self.main.parametre.language == "en" else 1
        values = ["","c", "g"]
        total = len(values)
        icone = (str(self.icone_folder[1]) + "  ") if self.main.parametre.use_nerd_font else "" # Some space for the icone
        txt = [[ "clone", "pull"], ["clone","pull" ]] # bofffff
        for i, values in enumerate(values):
            if i == 0:
                print(f"▼ {icone}{self.Tname}")
                is_last_index = 1 if i == total - 1 else 0 # total - 1 cause values[0] = name                 
            else :
                print(f"  {carac[is_last_index]} {txt[lang][i-1]} : {values}")
        

    def edit_project(self): # change info about prject like the name ...
        print(self.description)
        project = BASE_DIR  /"data/projects.json"
        line = 10
        subprocess.run(["nano", f"+{line}", project])
        #subprocess.call(['nano', project])

    def open_project(self):
        # Make error message if pwd is False
        # Mabye make popup (os) to open a folder like app if it's possible

        project_path = Path(self.pwd).expanduser().resolve()

        code_cmd = shutil.which(self.editor)

        if code_cmd:
            subprocess.run([code_cmd, "-n", str(project_path)])
            return

        # Fallback macOS
        if os.name == "posix" and shutil.which("open"):
            subprocess.run(["open", "-a", "Visual Studio Code", str(project_path)])
            return

        raise RuntimeError("VS Code n'est pas trouvé sur ce système")

    def get_depo_url(self) -> str | None:
        if self.repo == "":
            return None
        else :
            return self.repo

    def archive(self):
        pass




class Param:
    def __init__(self, main):
        self.main = main
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
        
        # Tableau des paramètres modifiables depuis l'interface param
        


    def get_selection_parametre(self):
        return self._selection_parametre
    

    
    def display_parametre(self):
        
        self.parametre_array = [self.language, self.use_nerd_font, self.version ] # DONT DELETE => recacule data after load_param()
        parametre_consigne = [["Language", "Use Nerd Font", "Current version"], ["Langage", "Utiliser Nerd Font", "Version actuelle"]]
        #self.selection_parametre = 0 # Alwyas have selection at the start even after quit,open
        caract = ["", "▶"] # False : "" | True :  "▶"
        WIDTH = 48
        lang = 1 if self.language == "fr" else 0 # Do func ?
        
        print()
        print(f"================== PARAMÈTRES ==================")
        for i in range(len(self.parametre_array)):
            arrow = False
            if i == self.selection_parametre:
                arrow = True
            print(f'{caract[arrow]}  {parametre_consigne[lang][i].ljust(WIDTH - len(str(self.parametre_array[i])) + (0 if i == self.selection_parametre else 1) - 3)}{self.parametre_array[i]}')
        print(f"-" * WIDTH)
        
        print()

        txt = [["Navigation", "Change", "Quit"], ["Navigation", "Changer", "Quitter"]]
        key = ["SPACE BAR", "ESPACE"]
        print(f"{txt[lang][0]} : ↑/↓    {txt[lang][1]} : {key[lang]}    {txt[lang][2]} : p")

        


    def load_param(self):
        try:
            with open(PARAMETRES_JSON, encoding="utf-8") as f:
                data = json.load(f)

                if 'app' in data:
                    self.language = data['app'].get('language')
                    self.use_nerd_font = data['app'].get('use_nerd_font', self.use_nerd_font)
                    self.version = data['app'].get('version') # Cause in v0.1.1 parametres.json there is no argument "version" but "versionS" so since v0.1.2 it's "version"
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

    def change_value(self, i):
        if i == 0:
            self.language = "fr" if self.language == "en" else "en"
        elif i == 1:
            self.use_nerd_font = not self.use_nerd_font
        elif i == 2:
            pass



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
