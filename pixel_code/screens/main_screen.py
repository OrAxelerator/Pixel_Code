import curses
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECTS_JSON = BASE_DIR / "data/projects.json"
PARAMETRES_JSON   = BASE_DIR  / "data/parametres.json"

class MainScreen:
    def __init__(self, main_app):
        self.main_app = main_app
        h, w = main_app.stdscr.getmaxyx()

        self.win = curses.newwin(h-10, w, 10, 0)
        

        self.array = ["salut", "test", "pixel", "code"]



    def display_main(self):
        self.win.clear()
        self.win.addstr(0,0, "MAIN SCREEN")
        for i, item in enumerate(self.array):
            self.win.addstr(i+1, 2, item)
        self.win.refresh()
        

        def load_projects(self):
            try:
                with open(PROJECTS_JSON, encoding="utf-8") as f:
                    self.projets = json.load(f)
                
                    for i in range(len(self.projets)): #recup tout les prjet en tant que class dans projetArray
                        self.projectsArray.append(Project(self, str(i), self.projets))
            except FileNotFoundError:
                print("Fichier projets.json introuvable.")
                # self.projet = {} so..