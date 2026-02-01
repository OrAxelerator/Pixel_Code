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

                for ligne in lignes:
                    if y >= height:
                        break  # ne pas dépasser la hauteur de l'écran
                    # On affiche la ligne en entier, ou tronquée si trop longue
                    self.logo_window.addstr(y, 0, ligne[:width-1])
                    y += 1  # passer à la ligne suivante à l'écran

        except FileNotFoundError:
            self.logo_window.addstr(0, 0, "Logo introuvable.")

        h, w = self.logo_window.getmaxyx()
        self.logo_window.addstr(h-1, 0, f"{'-' * (w - 1)}")

    def display_logo(self):
        self.logo_window.refresh()


