import curses
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOGO_TXT = BASE_DIR / "data/logo.txt"

class Logo():
    def __init__(self, main_app):
        self.main_app = main_app
        h, w = self.main_app.stdscr.getmaxyx()
        self.logo_window = curses.newwin(10, w, 0, 0)

        try:
            with open(LOGO_TXT, encoding="utf-8") as f:
                lignes = f.readlines()
                height, width = self.logo_window.getmaxyx()
                y = 0  # Initialiser y ici
                param_logo = self.main_app.param_manager.get_data("ui", "logo")# work
                for ligne in lignes:
                    if y >= height:
                        break  # don't write out in the screen
                    if  param_logo == "center": 
                        x = max((w - len(ligne)) // 2, 0)
                    else :
                        x = 0
                    
                    self.logo_window.addstr(y, x, ligne[:width-1])
                    y += 1  # pass to next ligne

        except FileNotFoundError:
            from utils.translate import translate
            error_msg = {
                "en":"logo not found",
                "fr":"logo introuvable"
            }
            self.logo_window.addstr(0, 0, translate(error_msg, "en"))

        h, w = self.logo_window.getmaxyx()
        self.logo_window.addstr(h-1, 0, f"{'-' * (w - 1)}")

    def display_logo(self):
        self.logo_window.refresh()


