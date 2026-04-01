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


import curses
import shutil
from pathlib import Path
import json
import subprocess
from pixel_code.screens.input_curses import Input
from pixel_code.screens.detail_panel_screen import DetailPanel
import os
from pixel_code.utils.translate import translate
from pixel_code.script.load_project_local import get_project_data
from pixel_code.script.add_project import create_pixelcode_config
from pixel_code.script.add_project_global import add_project_global
import logging


BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_JSON = BASE_DIR / "data/projects.json"
PARAMETRES_JSON   = BASE_DIR  / "data/parametres.json"
path_txt   = BASE_DIR  / "data/debug.txt"
def append_line(path_txt, line):
    """Ajoute une ligne à la fin du fichier, avec saut de ligne automatique."""
    with open(path_txt, "a", encoding="utf-8") as f:
        f.write(line + "\n")


class MainScreen:
    def __init__(self, main_app):
        self.main_app = main_app
        self.param = main_app.param
        self.stdscr = main_app.stdscr
        h, w = main_app.stdscr.getmaxyx()

        self.win = curses.newwin(h-10, w, 10, 0)
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

        self.input = Input(main_app)

        
        


        self._selection = 0
        self.projets = {}
        self.projectsArray = []
        self.show_details = False 
        self.show_git = False # clone, git pull

        self.load_projects()


    def load_projects(self):
        try:
            
            with open(PROJECTS_JSON, encoding="utf-8") as f:
                self.projets = json.load(f)
                #for path in self.projets:
            
                for i, project in enumerate(self.projets["projects"]): #recup tout les prjet en tant que class dans projetArray
                    DATA = get_project_data(project["path"])
                    self.projectsArray.append(Project(self, project["id"], DATA))
        except FileNotFoundError:
            #"Fichier projets.json introuvable.
            # self.projet = {} so..
            pass


    def display_main(self):
        h, w = self.win.getmaxyx()
        append_line(path_txt, f"Display main called. Window dimensions: h={h}, w={w}")  # Log dimensions
        self.win.clear()
        append_line(path_txt, "Main window cleared.")  # Log clear

        for i, item in enumerate(self.projectsArray):
            space = 0
            if i == self._selection and self.show_details:
                item.display_project_full("lol", i)
            else:
                space = 4 if self.show_details else space
                if self.show_details and self._selection > i:
                    item.display_project_compacte(selected_index=self._selection, my_index=i, space=+1)
                else:
                    item.display_project_compacte(selected_index=self._selection, my_index=i, space=space+1)

        self.win.refresh()
        append_line(path_txt, "Main window refreshed.")  # Log refresh

        


    def move_up(self):
        if len(self.projectsArray) == 0:
            pass
        elif self._selection - 1 < 0:
            pass
        else:
            self._selection -= 1
    
    def move_down(self):
        if len(self.projectsArray) == 0:
            pass
        elif self._selection + 1 >= len(self.projectsArray):
            pass
        else:
            self._selection += 1


    



    def add_project(self):
        txt_create_project = {
            "en" : {
                "name" : "  - Name of the project",
                "description" : "  - Description of the project",
                "langage" : "  - Langages (separated by commas)",
                "path" : "  - Directory of the project",
                "repo" : "  - Url of the github repo"
            },
            "fr" : {
                "name" : "  - Nom du projet",
                "description" : "  - Description du projet",
                "langage" : "  - Langages (séparés par des virgules)",
                "path" : "  - Chemin du projet",
                "repo" : "  - Url du dépot github"
            }
        }
        try:
            
            txt = translate(txt_create_project, self.main_app.param_manager.get_data("app", "language")) #chasj le prog ?
            
            name = self.input.display_input(f"{txt['name']} : ")
            description = self.input.display_input(f"{txt['description']} : ")
            languages = self.input.display_input(f"{txt['langage']} : ").split(',')
            pwd = self.input.display_input(f"{txt['path']} : ")
            repo = self.input.display_input(f'{txt["repo"]} : ')
            if pwd == "":
                pwd = os.getcwd()
            
            new_project = {
                "name": name,
                "description": description,
                "languages": [lang.strip() for lang in languages],
                "path": pwd,
                "repo" : repo
            }
            create_pixelcode_config(new_project)

            add_project_global(PROJECTS_JSON,pwd) # add to projects.json

            self.projectsArray.append(Project(self, str(4), new_project))
        except FileNotFoundError:
            print("Fichier projects.json introuvable.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")


    def delete_project(self):
        try:
            txt_confirm = {
                "en": f"Do you want to delete {self.projectsArray[self._selection]} : [y/N]",
                "fr": f"Voulez-vous supprimer {self.projectsArray[self._selection]} : [y/N]"
            }

            confirmation_message = translate(txt_confirm, self.main_app.param_manager.get_data("app", "language"))
            res = self.input.display_input(confirmation_message)
            self.win.addstr(0,0,"QWERTY")
            self.win.refresh()#do nothing
            if res.lower() not in ("y", "yes"):
                self.popup("Action annulée. Projet non supprimé.")
                return

            with open(PROJECTS_JSON, encoding="utf-8") as f:
                projets = json.load(f)

            target_path = self.projectsArray[self._selection].pwd
            projets["projects"] = [
                p for p in projets["projects"] if p["path"] != target_path
            ]

            with open(PROJECTS_JSON, "w", encoding="utf-8") as f:
                json.dump(projets, f, indent=4, ensure_ascii=False)

            self.projectsArray.pop(self._selection)
            self._selection = max(0, self._selection - 1)
            self.popup("Projet supprimé avec succès !")

        except FileNotFoundError:
            self.popup("Fichier projects.json introuvable.")
        except Exception as e:
            self.popup(f"Erreur : {e}")



    def pull_project(self):
        from pixel_code.script.git import git_pull_reset_hard
        res = self.input.display_input("sur ? [y/N]")
        if res == "y":
            git_pull_reset_hard(self.projectsArray[self._selection].repo)


    def popup(self, msg: str):#debug fonction to delete
            h, w = self.win.getmaxyx()
            self.win.addstr(h - 2, 2, f"{msg}")
            self.win.refresh()

class Project:
    def __init__(self, main_app, number, projets):
        self.main_app = main_app

        self.data = projets

        self.name = self.data["name"]
        self.description = self.data["description"]

        self.languages = " ".join(self.data.get("languages", []))
        self.pwd = self.data["path"]
        self.repo = self.data["repo"]

        self.dataAnsiStr = [self.name, self.description, self.languages, self.pwd]

        self.icone_folder = ["󰉋", ""] # Need 2 spaces :  CLOSED | OPEN

        h, w = self.main_app.win.getmaxyx()
        self.detail_panel = DetailPanel(main_app)

    def __str__(self):
        return f'{self.name}'



    def display_project_compacte(self,selected_index, my_index, space):
        #nf = self.main_app.param.use_nerd_font # True or False ..    
        arrow = "▶" if selected_index == my_index else ""
        icone_folder = ["󰉋", ""]
        icone = (str(icone_folder[0]) + "  ") if self.main_app.main_app.param_manager.get_data("app", "use_nerd_font") else ""
        if selected_index == my_index:
            self.main_app.win.addstr(my_index+space, 3, f"{arrow} {icone}{self.name}", curses.color_pair(2))
        else:
            self.main_app.win.addstr(my_index+space, 3, f"{arrow} {icone}{self.name}", curses.color_pair(1))
        #self.detail_panel.win.addstr(0,0, f"Project side panel {self.__str__()} ")
        
        self.main_app.win.refresh()
        

    def display_project_full(self, selected_index, my_index):
            txt = [[ "About", "Languages", "Path"], ["Descrption","Langages", "Chemin" ]] # bofffff
            txt = {
                "en": ["About", "Languages", "Path"],
                "fr":["Description", "Langages", "Chemin"]
            }
            lang = self.main_app.param.get_language() 
            icone = (str(self.icone_folder[1]) + "  ") if self.main_app.main_app.param_manager.get_data("app", "use_nerd_font") else "" # Some space for the icone
            values = self.dataAnsiStr[1::]
            total = len(values)
            size = os.get_terminal_size()
            columns = size.columns
            carac = ["├─", "└─"] # Each string is actually 2 charactere
            display = self.main_app.main_app.param_manager.get_data("ui", "display_project")

            if display == "bottom":
                for i, values in enumerate(values):
                    if i == 0:
                        self.main_app.win.addstr(i+1+my_index, 3, f"▼ {icone}{self.__str__()}", curses.color_pair(2))
                    is_last_index = 1 if i == total - 1 else 0 # total - 1 cause values[0] = name 
                    self.main_app.win.addstr(i+2+my_index, 5, f"  {carac[is_last_index]} {txt[lang][i]} : {values}")
            elif display == "side":
                self.detail_panel.win.clear() # clear at "init"
                h, w = self.detail_panel.win.getmaxyx()
                # self.detail_panel.win.refresh()
                self.detail_panel.win.addstr(11,w//5, f"{w,  h} ") #debug, to delete

                middle_x_name = self.detail_panel.get_middle_x(self.data['name'])
                self.detail_panel.win.addstr(2,middle_x_name, f"{self.data['name']} ", curses.A_BOLD) # Name in BOLD
                logging.debug("--------- SIDE MODE ----------")
                space = 0
                description_str = self.data['description']
                ligne = len(self.data['description']) // (w - 4) + 1
                div = ligne+1
                description_cut = []
                for i in range(1, div): #div=2, outpout 1, 2
                    logging.debug(f"valeur de i :{i} ")
                    logging.debug(f"valeur de description cut :{description_str[(w-3)*(i-1):(w-3)*i]} ")
                    description_cut.append(description_str[(w-3)*(i-1):(w-3)*i])
                # description_cut.append(description_str[ligne::])#rest of the description # CAUSE BUg ?
                
                logging.debug("debut écriture")
                for i, sentence in enumerate(description_cut):
                    logging.debug(repr(sentence))
                    if len(sentence) >= w:
                        logging.debug("PUPPSSIIII")
                    self.detail_panel.win.addstr(4 + i, 2, f"{sentence}")
                    # description_cut.append(description_str[0 + i*(w-2):w-2])
                
                
                # self.main_app.popup(ligne)
                if ligne == 0:
                    space = -3
                # for i in range(ligne):

                #     self.detail_panel.win.addstr(4 + i, 2, f"{self.data['description']}") # after 1line not 2 space right
                if  len(self.data['languages']) == 0:
                    space -= 2
                    pass
                else:
                    self.detail_panel.win.addstr(4 + ligne + 2 + space, 2, f"languages : {', '.join(self.data['languages'])}")

                self.detail_panel.win.addstr(4 + ligne + 4 + space, 2, f"Path : {self.data['path']}")                
                self.detail_panel.win.addstr(4 + ligne + 6 + space, 2, f"[Repo] : [{self.data['repo']}]")                


                self.detail_panel.win.border()
                self.main_app.popup(len(description_cut))
                self.detail_panel.win.refresh()
            
            if not self.main_app.main_app.param_manager.get_data("app", "use_nerd_font"):
                pass



                
    def open_project(self):
            # Make error message if pwd is False
            #self.main_app.param_manager.get_data
            editor = self.main_app.main_app.param_manager.get_data("projects", "editor")
            project_path = Path(self.pwd)
            
            if editor == "vim":
                subprocess.run(["vim",str(project_path)])
                return
            elif editor == "code":
                subprocess.run(["code", "-n", str(project_path)])
                return
            error_msg = {
                "en":"error while lauching projects in your IDE, check value of 'editor' in parametes.json",
                "fr":"erreur pedant lancement du projets dans votre IDE, regardez la valeur de 'editor' dans parametres.json"
            }
