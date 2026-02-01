import curses

from pixel_code.script.keybord import get_key
from pixel_code.screens.logo_screen import Logo
from pixel_code.screens.main_screen import MainScreen
from pixel_code.screens.param_screen import ParamScreen
from pixel_code.screens.input_curses import Input

class App:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.stdscr.keypad(True)
        curses.curs_set(0)

        h, w = stdscr.getmaxyx()

        self.logo = Logo(self)
        self.param = ParamScreen(self)
        self.main = MainScreen(self)
        #self.input = Input(self)
 

        self.current = "main"
        self.run()





    def run(self):
        self.logo.display_logo()
        self.main.display_main()
        while True:
            key = get_key()

            if key == "q" or key == "ENTER":
                break

            if "main"== self.current :
                if key == "p":
                    self.current = "param"
                    self.param._selection_parametre = 0
                    self.param.display()
                elif key == "a":
                    self.main.add_project()
                    self.main.display_projects() # or display main ?? seem lagy
                elif key == "d":
                    self.main.delete_project()
                    self.main.display_projects()
                elif key == "UP":
                    self.main.move_up()
                    self.main.display_main()
                elif key == "DOWN":
                    self.main.move_down()
                    self.main.display_main()
                
            elif "param" == self.current :
                if key == "p":
                    self.param.save_param()
                    self.current = "main"
                    self.main.display_main()
                elif key == "SPACE":
                    self.param.change_value(self.param.get_selection_parametre())
                    self.param.display()
                elif key == "UP":
                    self.param.move_up()
                    self.param.display()
                elif key == "DOWN":
                    self.param.move_down()
                    self.param.display()

                #self.stdscr.addstr(5, 0, f"Vous avez saisi: {text}")
                #self.stdscr.refresh()

                #res = prompt_text(self.stdscr, "Entrez du texte")
                #self.stdscr.addstr(16,0, f"Vous avez entré: {res}")
                #self.stdscr.refresh()