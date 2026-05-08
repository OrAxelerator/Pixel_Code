import curses
from pixel_code.utils.translate import translate
from pixel_code.paths import LOGO_TXT

class Logo():
    def __init__(self, main_app):
        self.main_app = main_app
        h, w = self.main_app.stdscr.getmaxyx()
        self.logo_window = curses.newwin(10, w, 0, 0)
        self.param_logo = self.main_app.param_manager.get_data("ui", "logo")# work

        try:
            with open(LOGO_TXT, encoding="utf-8") as f:
                lignes = f.readlines()
                height, width = self.logo_window.getmaxyx()
                y = 0  # init herei
                for ligne in lignes:
                    if y >= height:
                        break  # don't write out in the screen
                    if  self.param_logo == "center": 
                        x = max((w - len(ligne)) // 2, 0)
                    else : # logo = "left"
                        x = 0
                    
                    self.logo_window.addstr(y, x, ligne[:width-1])
                    y += 1  # pass to next ligne

        except FileNotFoundError:
            
            error_msg = {
                "en":"logo not found",
                "fr":"logo introuvable"
            }
            self.logo_window.addstr(0, 0, translate(error_msg, "en"))

        h, w = self.logo_window.getmaxyx()
        self.logo_window.addstr(h-1, 0, f"{'-' * (w - 1)}")

    def display_logo(self):
        if self.param_logo != self.main_app.param_manager.get_data("ui", "logo"):# work
             #change logo position in param
             self.param_logo = self.main_app.param_manager.get_data("ui", "logo")
             # need to change val of self.param else nothing append cause redraw like before
             self.redraw_logo()
        else:
            self.logo_window.refresh()

    def redraw_logo(self):
        h, w = self.main_app.stdscr.getmaxyx()        
        self.logo_window.clear() # not duplicate logo
        try:
                    with open(LOGO_TXT, encoding="utf-8") as f:
                        lignes = f.readlines()
                        height, width = self.logo_window.getmaxyx()
                        y = 0  # init here
                        for ligne in lignes:
                            if y >= height:
                                break  # don't write out in the screen
                            if  self.param_logo == "center": 
                                x = max((w - len(ligne)) // 2, 0)
                            else :
                                x = 0
                            
                            self.logo_window.addstr(y, x, ligne[:width-1])
                            y += 1  # pass to next ligne
                    h, w = self.logo_window.getmaxyx()
                    self.logo_window.addstr(h-1, 0, f"{'-' * (w - 1)}")
                    self.logo_window.refresh()
        except FileNotFoundError:
                    
                    error_msg = {
                        "en":"logo not found",
                        "fr":"logo introuvable"
                    }
                    self.logo_window.addstr(0, 0, translate(error_msg, "en"))

                    
