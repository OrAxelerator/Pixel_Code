import curses
import shutil
from pathlib import Path
import json
import subprocess
from pixel_code.screens.input_curses import Input
from pixel_code.screens.detail_panel_screen import DetailPanel
import os
from pixel_code.utils.translate import translate


BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_JSON = BASE_DIR / "data/projects.json"
PARAMETRES_JSON   = BASE_DIR  / "data/parametres.json"

class MainScreen:
    def __init__(self, main_app):
        self.main_app = main_app
        self.param = main_app.param
        self.stdscr = main_app.stdscr
        h, w = main_app.stdscr.getmaxyx()

        self.win = curses.newwin(h-10, w, 10, 0)

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
            
                for i in range(len(self.projets)): #recup tout les prjet en tant que class dans projetArray
                    self.projectsArray.append(Project(self, str(i), self.projets))
        except FileNotFoundError:
            #"Fichier projets.json introuvable.
            # self.projet = {} so..
            pass


    def display_main(self):
        self.win.clear()
        
        for i, item in enumerate(self.projectsArray):
            #self.win.addstr(i+1, 2, f'{item}')
            
            space = 0
            
            if i == self._selection and self.show_details:
                #item.display_project_compacte(selected_index=self._selection, my_index=i, space=space)
                item.display_project_full("lol", i) # side panel to exept for projet[0]
                #item.detail_panel.win.clear()
                #item.display_side(item.__str__())
            else:

                space = 4  if self.show_details else space
                if self.show_details and self._selection > i:
                    item.display_project_compacte(selected_index=self._selection, my_index=i, space=+1)
                else:                        
                    item.display_project_compacte(selected_index=self._selection, my_index=i, space=space+1)
        self.win.refresh()
        


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
                "pwd" : "  - Directory of the project",
                "repo" : "  - Url of the github repo"
            },
            "fr" : {
                "name" : "  - Nom du projet",
                "description" : "  - Description du projet",
                "langage" : "  - Langages (séparés par des virgules)",
                "pwd" : "  - Chemin du projet",
                "repo" : "  - Url du dépot github"
            }
        }
        try:
            txt = translate(txt_create_project, self.main_app.param.language)
            name = self.input.display_input(f"{txt['name']} : ")
            description = self.input.display_input(f"{txt['description']} : ")
            languages = self.input.display_input(f"{txt['langage']} : ").split(',')
            pwd = self.input.display_input(f"{txt['pwd']} : ")
            repo = self.input.display_input(f'{txt["repo"]} : ')
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
                "en": f"Do you want to delete {self.projectsArray[self._selection]} : [y/N]",
                "fr": f"Voulez vous supprimer {self.projectsArray[self._selection]} : [y/N]"
            }
            txt_error = {
                "en": "Invalid project number.",
                "fr": "Numéro de projet invalide."
            }
            txt_success = {
                "en": "Project deleted successfully!",
                "fr": "Projet supprimé avec succès !"
            }
            
            project_number = str(self._selection)
            
            res = self.input.display_input(translate(txt_confirm, self.param.get_language()))
            if res == "n" or res == "":
                h, w = self.win.getmaxyx()
                self.win.addstr(h-1, 0, "no delete")
                self.win.refresh()
                
                return False
            elif res == "y":
            
                with open(PROJECTS_JSON, encoding="utf-8") as f:
                    projets = json.load(f)
                if project_number not in projets:
                    h, w = self.win.getmaxyx()
                    self.win.addstr(h-1, 0, translate(txt_error, self.param.get_language()))
                    self.win.refresh()
                    return

                del projets[project_number]

                projets = {str(i): v for i, v in enumerate(projets.values())}
                with open(PROJECTS_JSON, 'w', encoding="utf-8") as f:
                    json.dump(projets, f, indent=4, ensure_ascii=False)
                h, w = self.win.getmaxyx()
                self.win.addstr(h-1, 0, translate(txt_success, self.param.get_language()))
                self.win.refresh()
                self.projectsArray = [Project(self, str(i), projets) for i in range(len(projets))]
        except FileNotFoundError:
            print("Fichier projects.json introuvable.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")


class Project:
    def __init__(self, main_app, number, projets):
        self.main_app = main_app
        self.number = number

        data = projets[self.number]

        self.name = data["name"]
        self.description = data["description"]
        self.editor = data["editor"]
        self.languages = " ".join(data.get("programming_languages", []))
        self.pwd = data["pwd"]
        self.repo = data["repo"]

        self.dataAnsiStr = [self.name, self.description, self.languages, self.pwd]

        self.icone_folder = ["󰉋", ""] # Need 2 spaces :  CLOSED | OPEN

        h, w = self.main_app.win.getmaxyx()
        self.detail_panel = DetailPanel(main_app)

    def __str__(self):
        return f'{self.name}'
    

    def display_side(self, item):
        self.detail_panel.win.clear()
        
        self.detail_panel.win.addstr(3,4, f"{item} test")
        self.detail_panel.win.refresh()


    def display_project_compacte(self,selected_index, my_index, space):
        #nf = self.main_app.param.use_nerd_font # True or False ..    
        arrow = "▶" if selected_index == my_index else ""
        #icone = (str(self.icone_folder[0]) + "  ") if nf else ""
        self.main_app.win.addstr(my_index+space, 3, f"{arrow} {self.name}")
        #self.detail_panel.win.addstr(0,0, f"Project side panel {self.__str__()} ")
        
        self.main_app.win.refresh()

    def display_project_full(self, selected_index, my_index):
            self.detail_panel.win.clear()
            self.detail_panel.win.border()
            self.detail_panel.win.addstr(1,1, f"Project side panel { self.__str__()} ")
            self.detail_panel.win.addstr(11,20, f"YOOOOOOO ")
            self.detail_panel.win.refresh()
            carac = ["├─", "└─"]
            lang = 0 if self.main_app.param.get_language() == "en" else 1
            txt = [[ "About", "Languages", "Path"], ["Descrption","Langages", "Chemin" ]] # bofffff
            if not self.main_app.param.use_nerd_font:
                pass

            icone = (str(self.icone_folder[1]) + "  ") if self.main_app.param.use_nerd_font else "" # Some space for the icone
            values = self.dataAnsiStr[1::]
            total = len(values)
            size = os.get_terminal_size()
            columns = size.columns

            for i, values in enumerate(values):
                if i == 0:
                    self.main_app.win.addstr(i+1+my_index, 3, f"▼ {icone}{self.__str__()}")
                is_last_index = 1 if i == total - 1 else 0 # total - 1 cause values[0] = name 
                self.main_app.win.addstr(i+2+my_index, 5, f"  {carac[is_last_index]} {txt[lang][i]} : {values}")
                #self.main_app.win.refresh()
                #if len(values) >= size.columns: # Reduce/shorten path of a project
                #    part = round(columns * 0.34)
                #    
                #    print(f"  {carac[is_last_index]} {txt[lang][i]} : {values[0:part:]}...{values[total - part::]}")
                #else :
                
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