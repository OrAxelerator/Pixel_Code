import curses

from pixel_code.script.keybord import get_key
from pixel_code.screens.logo_screen import Logo
from pixel_code.screens.main_screen import MainScreen
from pixel_code.screens.param_screen import ParamScreen
from pixel_code.script.input import get_key

class App:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.stdscr.keypad(True)
        curses.curs_set(0)

        h, w = stdscr.getmaxyx()

        self.logo = Logo(self)
        self.main = MainScreen(self)
        self.param = ParamScreen(self)
        self.input = Input(self)
 

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
                    self.param.display_param()
                elif key == "a":
                    text = self.input.display_input("Entrez votre texte")
                    self.main.array.append(text)
                    self.main.display_main()
                
            elif "param" == self.current :
                if key == "p":
                    self.current = "main"
                    self.main.display_main()

                #self.stdscr.addstr(5, 0, f"Vous avez saisi: {text}")
                #self.stdscr.refresh()

                #res = prompt_text(self.stdscr, "Entrez du texte")
                #self.stdscr.addstr(16,0, f"Vous avez entré: {res}")
                #self.stdscr.refresh()