# todo :
#   - sys of pip => installer.py
#   - Check if user have wifi
#   - make option to add pixelcode.json so when install new code VIA pixel_code pop to add project on fork on pixel code
#   -  make something cool with nerd font for icon
#   -  think about integration in pixel_nav => pixelcode.json ? ..
#   - programme de mise a jour automatique
#   - projet.json : icone = ["":iconed de base, "favortite : icone + cœur, "]
#   - Use quit() func in main  instead of break in code
#   - # Make error message if pwd is False in open_code (Project)

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
from pixel_code.paths import PROJECTS_JSON, ensure_user_files
from pixel_code.utils.translate import translate
from pixel_code.script.load_project_local import get_project_data
from pixel_code.script.add_project import create_pixelcode_config
from pixel_code.script.add_project_global import add_project_global
import logging
import math


class MainScreen:
    def __init__(self, main_app):
        self.main_app = main_app
        self.param = main_app.param
        self.stdscr = main_app.stdscr
        h, w = main_app.stdscr.getmaxyx()

        self.win = curses.newwin(h-10, w, 10, 0)
        blue = curses.init_color(1, 300, 270, 1000)
        curses.init_pair(1, 1, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

        self.input = Input(main_app)

        
        


        self._selection = 0
        self.projets = {}
        self.projectsArray = []
        self.search_query = ""
        self.status_filter = "all"
        self.show_details = False 
        self.show_git = False # clone, git pull

        self.load_projects()

    def get_display_projects(self):
        query = self.search_query.strip().lower()
        display_projects = self.projectsArray

        if query != "":
            display_projects = [
                project for project in display_projects
                if query in project.name.lower()
            ]

        if self.status_filter == "done":
            display_projects = [
                project for project in display_projects
                if project.status == "done"
            ]
        elif self.status_filter == "todo":
            display_projects = [
                project for project in display_projects
                if project.status != "done"
            ]

        return display_projects

    def get_status_filter_label(self):
        labels = {
            "en": {
                "all": "All",
                "done": "Done",
                "todo": "To finish"
            },
            "fr": {
                "all": "Tous",
                "done": "Fini",
                "todo": "À finir"
            }
        }
        lang = self.main_app.param_manager.get_data("app", "language")
        return labels.get(lang, labels["en"]).get(self.status_filter, labels["en"]["all"])

    def get_selected_project(self):
        display_projects = self.get_display_projects()
        if len(display_projects) == 0:
            return None

        self._selection = min(self._selection, len(display_projects) - 1)
        return display_projects[self._selection]


    def load_projects(self):
        logging.debug("load_project in MainScreen")
        ensure_user_files()
        try:
            if PROJECTS_JSON.exists():
                with open(PROJECTS_JSON, encoding="utf-8") as f:
                    self.projets = json.load(f)
                    #for path in self.projets:
                    
                    for i, project in enumerate(self.projets["projects"]): #recup tout les prjet en tant que class dans projetArray
                        project_path = project.get("path")
                        DATA = get_project_data(project_path)
                        if DATA is False:
                            msg = f"Project ignored: .pixelcode.json not found for {project_path}"
                            logging.warning(f"{msg} (id={project.get('id')})")
                            continue

                        status = project.get("status", "todo")
                        self.projectsArray.append(Project(self, project["id"], DATA, status))
        except FileNotFoundError:
            logging.warning(f"FILE {PROJECTS_JSON} NOT FOUND")
            #"Fichier projets.json introuvable.
            # self.projet = {} so..
            pass


    def display_main(self):
        h, w = self.win.getmaxyx()
        self.main_app.h
        self.win.clear()
        display_projects = self.get_display_projects()
        header_offset = 1 if self.search_query or self.status_filter != "all" else 0

        if header_offset:
            header_parts = []
            if self.search_query:
                label_search = translate({"en": "Search", "fr": "Recherche"}, self.main_app.param_manager.get_data("app", "language"))
                header_parts.append(f"{label_search}: {self.search_query}")
            if self.status_filter != "all":
                label_filter = translate({"en": "Filter", "fr": "Filtre"}, self.main_app.param_manager.get_data("app", "language"))
                header_parts.append(f"{label_filter}: {self.get_status_filter_label()}")

            header_text = " | ".join(header_parts)
            self.win.addstr(0, 3, header_text[:max(0, w - 6)], curses.color_pair(1))

        if len(display_projects) == 0:
            self._selection = 0
            no_project_text = translate({"en": "No projects found", "fr": "Aucun projet trouvé"}, self.main_app.param_manager.get_data("app", "language"))
            self.win.addstr(header_offset, 3, no_project_text)
            self.win.refresh()
            return

        self._selection = min(self._selection, len(display_projects) - 1)
#self.porjetArray[difCurseurExt::] #jusqu'a condition bloue le reste
        available_h = h - header_offset
        gap_curror_over = self._selection - available_h + 1
        if gap_curror_over > 0: # if positive
            logging.debug(f"CUSOR OVERFLOW, : {gap_curror_over}")
        else :
            gap_curror_over = 0
            # logging.debug(f"CUSOR IN, : {gap_curror_over}")

        gap = 0
        # logging.debug(f"h of main : {h}")
        dif = available_h - len(display_projects)
        # logging.debug(f' dif = {h} - {len(self.projectsArray)} = {h - len(self.projectsArray)}')
        if dif >= 0:
            gap = len(display_projects) 
            # logging.debug(f"gap :{gap} | dif <= 0")
        elif dif < 0 :
            gap = available_h + gap_curror_over
            # logging.debug(f"{gap} - dif > 0 (else)")
        else:
            logging.debug(f"WTF gap = {gap}")

        # logging.debug(f"GAP /, , {gap}")
        # display_proj = self.projectsArray[gap_curror_over:gap:]
        # logging.debug("======START FOR ========")
        for i, project in enumerate(display_projects[gap_curror_over:gap:]): # j'ai 0 a 4 donc 3 mais afficbe 4 truc ... WHY
            
            space = 4 if self.show_details else 0
            # logging.debug(f"selectin_index:{self._selection}, myindex:{i}, gap:{gap_curror_over}")
            project.display_project_compacte(selected_index=self._selection, my_index=i, space=space, gap=gap_curror_over, row_offset=header_offset)
            if self._selection == i + gap_curror_over and self.show_details:
                project.display_project_full("to_delete", i + header_offset)
        
        
        self.win.refresh()

        # for i, item in enumerate(self.projectsArray[gap_curror_over::]):
        #     # i par rapport début lsite et pa par rapoort premier el affiché
        #     logging.debug("-------")
        #     if 10 + i < self.main_app.h:
        #         # logging.debug("condition pass")
        #         space = 0
        #         if i == self._selection and self.show_details:
        #             item.display_project_compacte(selected_index=self._selection, my_index=i, space=space+1) # why reverse display_compacte and full don't display the first project on side mod
        #             item.display_project_full("lol", i)
        #         else:
        #             space = 4 if self.show_details else space
        #             if self.show_details and self._selection > i:
        #                 item.display_project_compacte(selected_index=self._selection, my_index=i+gap_curror_over, space=+1)
        #             else:
        #                 item.display_project_compacte(selected_index=self._selection, my_index=i+gap_curror_over, space=space+1) # put gap here ?

        

        


    def move_up(self):
        self._selection = max(0, self._selection -1)

    def move_down(self):
        # self._selection = max(1, min(self._selection+1, len(self.projectsArray)))
        display_projects = self.get_display_projects()
        if len(display_projects) == 0:
            self._selection = 0
            return

        self._selection = min(len(display_projects)-1, self._selection + 1)

    def search_project(self):
        search_text = {
            "en": "Search by name",
            "fr": "Chercher par nom"
        }
        title = translate(search_text, self.main_app.param_manager.get_data("app", "language"))
        query = self.input.display_input(f"{title} : ", prefill=self.search_query)
        if query is None:
            return

        self.search_query = query.strip()
        self._selection = 0

    def clear_search(self):
        self.search_query = ""
        self._selection = 0

    def reset_project_view(self):
        self.search_query = ""
        self.status_filter = "all"
        self._selection = 0

    def cycle_status_filter(self):
        filters = ["all", "done", "todo"]
        index = filters.index(self.status_filter)
        self.status_filter = filters[(index + 1) % len(filters)]
        self._selection = 0

    def toggle_project_status(self):
        project = self.get_selected_project()
        if project is None:
            return

        project.status = "todo" if project.status == "done" else "done"
        project.data["status"] = project.status

        ensure_user_files()
        try:
            with open(PROJECTS_JSON, encoding="utf-8") as f:
                projets = json.load(f)

            for saved_project in projets.get("projects", []):
                if saved_project.get("id") == project.id or saved_project.get("path") == project.pwd:
                    saved_project["status"] = project.status
                    break

            with open(PROJECTS_JSON, "w", encoding="utf-8") as f:
                json.dump(projets, f, indent=4, ensure_ascii=False)

            logging.info(f"Project status changed: {project.name} -> {project.status}")
        except FileNotFoundError:
            logging.warning("File projects.json not found.")
        except Exception as e:
            logging.warning(f"Error while saving project status: {e}")

    
    def edit_project(self):
        """Edit project fields and save changes to .pixelcode.json."""
        project = self.get_selected_project()
        if project is None:
            return

        lang = self.main_app.param_manager.get_data("app", "language")
        labels = {
            "en": {
                "name": "Name",
                "description": "Description",
                "languages": "Languages (comma separated)",
                "pwd": "Path",
                "repo": "Repo URL"
            },
            "fr": {
                "name": "Nom",
                "description": "Description",
                "languages": "Langages (séparés par des virgules)",
                "pwd": "Chemin",
                "repo": "URL du dépôt"
            }
        }

        fields = ["name", "description", "languages", "pwd", "repo"]
        old_path = project.pwd
        updated_path = None
        for field in fields:
            current_value = project.data.get(field, "")
            if field == "languages":
                current_value = ", ".join(current_value or [])

            prompt = translate({"en": labels["en"][field], "fr": labels["fr"][field]}, lang)
            new_value = self.input.display_input(f"{prompt} : ", prefill=current_value)
            if new_value is None:
                continue

            new_value = new_value.strip()
            if field == "languages":
                project.data["languages"] = [lang_item.strip() for lang_item in new_value.split(",") if lang_item.strip()]
                project.languages = " ".join(project.data["languages"])
            elif field == "pwd":
                if new_value == "":
                    continue
                new_path = os.path.expanduser(new_value)
                if not Path(new_path).exists():
                    no_path_text = translate({"en": "Path not found", "fr": "Chemin introuvable"}, lang)
                    self.popup(f"{no_path_text}: {new_path}")
                    continue
                project.pwd = new_path
                project.data["path"] = new_path
                updated_path = new_path
            else:
                project.data[field] = new_value
                setattr(project, field, new_value)

        project.dataAnsiStr = [project.name, project.description, project.languages, project.pwd]
        self._save_project_config(project, old_path=old_path, updated_path=updated_path)

    def _save_project_config(self, project, old_path=None, updated_path=None):
        ensure_user_files()
        config_file = Path(project.pwd) / ".pixelcode.json"
        try:
            with open(config_file, "w", encoding="utf-8") as f:
                json.dump(project.data, f, indent=4, ensure_ascii=False)

            if updated_path is not None:
                with open(PROJECTS_JSON, encoding="utf-8") as f:
                    projets = json.load(f)

                for saved_project in projets.get("projects", []):
                    if saved_project.get("id") == project.id or saved_project.get("path") == old_path:
                        saved_project["path"] = updated_path
                        break

                with open(PROJECTS_JSON, "w", encoding="utf-8") as f:
                    json.dump(projets, f, indent=4, ensure_ascii=False)

            save_text = translate({"en": "Project saved.", "fr": "Projet enregistré."}, self.main_app.param_manager.get_data("app", "language"))
            self.popup(save_text)
        except Exception as e:
            logging.warning(f"Error saving project config: {e}")
            save_error_text = translate({"en": "Error saving project.", "fr": "Erreur lors de l'enregistrement du projet."}, self.main_app.param_manager.get_data("app", "language"))
            self.popup(save_error_text)


    def add_project(self):
        txt_create_project = {
            "en" : {
                "name" : "  - Name of the project",
                "description" : "  - Description of the project",
                "langage" : "  - Langages (separated by commas)",
                "path" : "  - Directory of the project",
                "repo" : "  - Url of the github repo"
            },
            "fr" : {
                "name" : "  - Nom du projet",
                "description" : "  - Description du projet",
                "langage" : "  - Langages (séparés par des virgules)",
                "path" : "  - Chemin du projet",
                "repo" : "  - Url du dépot github"
            }
        }
        try:
            
            txt = translate(txt_create_project, self.main_app.param_manager.get_data("app", "language")) #chasj le prog ?
            
            name = self.input.display_input(f"{txt['name']} : ")
            description = self.input.display_input(f"{txt['description']} : ")
            languages = self.input.display_input(f"{txt['langage']} : ").split(',')
            pwd = self.input.display_input(f"{txt['path']} : ")
            if pwd == "":
                pwd = os.getcwd() # get pwd path

            if self.main_app.param_manager.get_data("projects", "repo") == "github":
                link = "https://github.com/"
            else:
                link= "https://"
            repo = self.input.display_input(f'{txt["repo"]} : ', prefill=link)

            
            
            
            new_project = {
                "name": name,
                "description": description,
                "languages": [lang.strip() for lang in languages],
                "path": pwd,
                "repo" : repo
            }
            if not create_pixelcode_config(new_project): # .pixelcode.json already exist
                self.popup("TSTE")
                logging.error("File .pixelcode.json aleray exist, your input will be ignored")
                return False


            add_project_global(PROJECTS_JSON,pwd) # add to projects.json

            self.projectsArray.append(Project(self, str(4), new_project, "todo"))
        except FileNotFoundError:
            logging.warning("File projects.json not found.")
        except Exception as e:
            logging.warning(f"Error append : {e}")


    def delete_project(self):
        try:
            ensure_user_files()
            project_to_delete = self.get_selected_project()
            if project_to_delete is None:
                return

            txt_confirm = {
                "en": f"Do you want to delete {project_to_delete} : [y/N]",
                "fr": f"Voulez-vous supprimer {project_to_delete} : [y/N]"
            }

            confirmation_message = translate(txt_confirm, self.main_app.param_manager.get_data("app", "language"))
            res = self.input.display_input(confirmation_message)
            self.win.refresh()#do nothing?
            if res.lower() not in ("y", "yes"):
                self.popup("Action cancelled. Project not delete.")
                return

            with open(PROJECTS_JSON, encoding="utf-8") as f:
                projets = json.load(f)

            target_path = project_to_delete.pwd
            projets["projects"] = [
                p for p in projets["projects"] if p["path"] != target_path
            ]

            with open(PROJECTS_JSON, "w", encoding="utf-8") as f:
                json.dump(projets, f, indent=4, ensure_ascii=False)

            self.projectsArray = [
                project for project in self.projectsArray
                if project.pwd != target_path
            ]
            self._selection = max(0, min(self._selection, len(self.get_display_projects()) - 1))
            self.popup("Projet supprimé avec succès !")
            logging.info("Project deleted")

        except FileNotFoundError:
            logging.warning("File projects.json not found.")
        except Exception as e:
            logging.warning(f"Error append : {e}")



    def pull_project(self):
        from pixel_code.script.git import git_pull_reset_hard
        project = self.get_selected_project()
        if project is None:
            return

        res = self.input.display_input("sur ? [y/N]")
        if res == "y":
            git_pull_reset_hard(project.repo)


    def popup(self, msg: str):#debug fonction to delete
            h, w = self.win.getmaxyx()
            self.win.addstr(h - 2, 2, f"{msg}")
            self.win.refresh()






class Project:
    def __init__(self, main_app, number, projets, status="todo"):
        self.main_app = main_app
        self.id = number

        self.data = projets
        self.status = status or "todo"
        self.data["status"] = self.status

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

    def get_status_badge(self):
        use_nerd_font = self.main_app.main_app.param_manager.get_data("app", "use_nerd_font")
        if self.status == "done":
            return "" if use_nerd_font else "[x]"
        return "" if use_nerd_font else "[ ]"

    def get_status_text(self):
        txt = {
            "en": {
                "done": "Done",
                "todo": "To finish"
            },
            "fr": {
                "done": "Fini",
                "todo": "À finir"
            }
        }
        lang = self.main_app.main_app.param_manager.get_data("app", "language")
        return txt.get(lang, txt["en"]).get(self.status, txt.get(lang, txt["en"])["todo"])



    def display_project_compacte(self,selected_index, my_index, space, gap=0, row_offset=0):
        if self.main_app.main_app.param_manager.get_data("ui", "display_project") == "side":
            space = 0

        # logging.debug(f"select : {selected_index}   my{my_index}")
        # if selected_index == my_index:
            # logging.debug(f"CHECK ARE EQUALS")
        if selected_index == my_index + gap:
            logging.debug(f"CONDITION CHECK de {self.name}")

        arrow = "▶" if selected_index == my_index + gap else " "
        icone_folder = ["󰉋", ""]
        icone = (str(icone_folder[0]) + "  ") if self.main_app.main_app.param_manager.get_data("app", "use_nerd_font") else ""
        status_badge = self.get_status_badge()
        y = my_index + space + row_offset
        if selected_index == my_index + gap:
            # self.main_app.popup("la")
            self.main_app.win.addstr(y, 3, f"{arrow} {status_badge} {icone}{self.name}", curses.color_pair(2))
        else:
            self.main_app.win.addstr(y, 3, f"{arrow} {status_badge} {icone}{self.name}", curses.color_pair(1))
        #self.detail_panel.win.addstr(0,0, f"Project side panel {self.__str__()} ")
        
        self.main_app.win.refresh()
        

    def display_project_full(self, selected_index, my_index):
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
                for i, val in enumerate(values):
                    len_text_and_display = len(str(values[0])) + 11
                    self.main_app.popup(f"len:{len_text_and_display} col: {columns} truc:{len(str(val))} val : {values[0]}")
                    if i == 0:
                        self.main_app.win.addstr(i+1+my_index, 3, f"▼ {icone}{self.__str__()}", curses.color_pair(2))
                    is_last_index = 1 if i == total - 1 else 0 # total - 1 cause values[0] = name 
                    if len_text_and_display > columns:#w pas déclaré
                        self.main_app.popup("TOO LOONG")
                        self.main_app.win.addstr(i+2+my_index, 3, f"  {carac[is_last_index]} {txt[lang][i]} : {values[i][0:columns:]}")  
                    self.main_app.win.addstr(i+3+my_index, 3, f"  {carac[is_last_index]} {values[i]}")

            elif display == "side":
                self.detail_panel.win.clear() # clear at "init"
                h, w = self.detail_panel.win.getmaxyx()

                center_name_x = self.detail_panel.get_middle_x(self.data['name'])
                self.detail_panel.win.addstr(2,center_name_x, f"{self.data['name']} ", curses.A_BOLD) # Name in BOLD
                space = 0
                description_str = self.data['description']
                overfloww:int = math.ceil(len(description_str) / (w - 3)) #calc number of line over w
                description_cut = [] # cut description in multiple str (sentence)
                #math seuil : 41.1 = 42
                # Calc sentence
                max_width = w - 3 #2 ch border + 1space left
                for i in range(0, len(description_str), max_width):
                    description_cut.append(description_str[i:i + max_width])

                # Display
                for i, sentence in enumerate(description_cut):
                    self.detail_panel.win.addstr(4 + i, 2, sentence)

                text = {
                    "en": ["Status", "Languages", "Path", "Repo"],
                    "fr":["Statut", "Langages", "Chemin", "Depo"]
                }
                text_description = translate(text, self.main_app.main_app.param_manager.get_data("app", "language"))
                detail_y = 4 + max(len(description_cut), 1) + 1
                self.detail_panel.win.addstr(detail_y, 2, f"{text_description[0]} : {self.get_status_text()}")
                detail_y += 2

                if len(self.data['languages']) > 0:
                    self.detail_panel.win.addstr(detail_y, 2, f"{text_description[1]} : {', '.join(self.data['languages'])}")
                    detail_y += 2

                self.detail_panel.win.addstr(detail_y, 2, f"{text_description[2]} : {self.data['path']}")
                self.detail_panel.win.addstr(detail_y + 2, 2, f"{text_description[3]} : [{self.data['repo']}]")

                self.detail_panel.win.border()
                self.detail_panel.win.refresh()



                
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
            elif editor == "cmd":
                if os.path.exists(project_path) and os.path.isdir(project_path):
                #cd into directory?
                    self.main_app.popup("path existe")
                    import platform
                    import sys
                    system = platform.system()
                    try:
                        if system == "Linux":
                            # try several terminal
                            terminals = [
                                ["gnome-terminal", "--working-directory", project_path],
                                ["konsole", "--workdir", project_path],
                                ["xfce4-terminal", "--working-directory", project_path],
                                ["x-terminal-emulator", "--working-directory", project_path],
                                ["xterm", "-e", f'cd "{project_path}" && bash']
                            ]

                            for cmd in terminals:
                                try:
                                    subprocess.Popen(cmd)
                                    break
                                except FileNotFoundError:
                                    continue

                        elif system == "Darwin":  # macOS
                            subprocess.Popen([
                                "open", "-a", "Terminal", project_path
                            ])

                        elif system == "Windows":
                            subprocess.Popen([
                                "cmd.exe", "/K", f'cd /d "{project_path}"'
                            ])

                        else:
                            logging.warning(f"OS not  supported: {system}") # user on temple os ?
                            self.main_app.popup(f"OS not  supported: {system}")

                    except Exception as e:
                        logging.warning(f"Error opening terminal : {e}")
                        self.main_app.popup(f"Error opening terminal : {e}")

                    sys.exit() # quit Pixel_Code
