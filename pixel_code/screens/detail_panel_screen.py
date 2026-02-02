import curses
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_JSON = BASE_DIR / "data/projects.json"
PARAMETRES_JSON   = BASE_DIR  / "data/parametres.json"


class DetailPanel:
    def __init__(self, main_app):
        self.app = main_app
        self.stdscr = main_app.stdscr
        #self.main_screen = self.main_app

        h, w = self.stdscr.getmaxyx()
        self.win = curses.newwin(h-10, w//2, 10, w//2)
        self.win.border()
        

    #def display_detail(self, projet):
    #    self.win.clear()
    #    self.win.addstr(0,0, f"test{projet.__str__()}")
    #    self.win.refresh()


    # TO DELETE

