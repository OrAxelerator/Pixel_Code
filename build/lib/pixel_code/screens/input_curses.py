import curses
from curses.textpad import Textbox

class Input:
    def __init__(self, main_app):
        self.app = main_app
        self.stdscr = main_app.stdscr

        h, w = self.stdscr.getmaxyx()

        self.height = 3 
        self.width = w
        self.y = h - self.height
        self.x = 0
        # self.win = main_app
        # Fenêtre principale de l’input
        self.win = curses.newwin(self.height, self.width, self.y, self.x)
        self.win.keypad(True)

    def display_input(self, title="Input", prefill=""):

        curses.curs_set(1)
        self.win.clear()
        self.win.border()
        self.win.addstr(0, 2, f" {title} ")

        box_width = self.width - 6
        box_x = 3
        box_y = 2

        # Fenêtre de saisie (sansd
        #  bordure)
        edit_win = self.win.derwin(1, box_width, box_y-1, box_x)
        edit_win.clear()

        edit_win.addstr(prefill)
        # edit_win.clear()
        self.win.refresh()
        edit_win.refresh()

        box = Textbox(edit_win)
        text = box.edit().strip()

        if text.endswith(chr(27)):  # Si Échap a été pressé (peu probable avec Textbox)
            text = None
            self.win.clear()
            self.win.refresh()    
            self.main_app.stdscr.refresh()
        else:
            self.win.clear()
            self.win.refresh()
            curses.curs_set(0)

            return text
