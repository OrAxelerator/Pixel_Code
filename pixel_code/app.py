import curses

from pixel_code.script.keybord import get_key
from pixel_code.screens.logo_screen import Logo
from pixel_code.screens.main_screen import MainScreen
from pixel_code.screens.param_screen import ParamScreen
from pixel_code.screens.detail_panel_screen import DetailPanel
from pixel_code.screens.input_curses import Input
from pixel_code.script.data.param_manager import ParamManager



import logging
import sys
# Start debug mod with python3 pixel_code/__main__.py --debug

level = logging.DEBUG if "--debug" in sys.argv else logging.INFO

logging.basicConfig(
    filename="debug.log",
    level=level,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# logging.debug("Valeur de x ")   # affiché seulement en --debug
# logging.info("APP LAUNCH")   # affiché en --debug ET mode normal
# logging.warning("Problème détecté")    # toujours affiché
class App:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.stdscr.keypad(True)
        curses.curs_set(0)

        self.h, self.w = stdscr.getmaxyx()
        self.param_manager = ParamManager()
        self.logo = Logo(self)
        self.param = ParamScreen(self)
        self.main = MainScreen(self)
        self.detail_panel = DetailPanel(self)
        
        # self.win_input = curses.newwin(3, w, h - 3, 0)
        # self.input = Input(self,)
 

        self.current = "main" #("main", "parametre")
        self.run()





    def run(self):
        self.logo.display_logo()
        self.main.display_main()
        logging.info("main loop launched")
        while True:
            key = get_key()

            if key == "q":
                logging.info("user quit pixel_code")
                break

            if "main"== self.current :
                if key == "p":
                    logging.info("user open parametre windows")
                    self.current = "param"
                    self.param._selection_parametre = 0
                    self.param.display()
                elif key == "a":
                    self.main.add_project()
                    self.main.display_main() # or display main ?? seem lagy display_proj
                elif key == "d":
                    self.main.delete_project()
                    self.main.display_main()
                    # self.main.popup("jsspppp")
                elif key == "g":
                    self.main.pull_project()
                    pass #gt clone, git pull, git reset
                    #electon input like main with arrow
                elif key == "UP":
                    self.main.move_up()
                    self.main.display_main()
                elif key == "DOWN":
                    self.main.move_down()
                    self.main.display_main()
                elif key == "SPACE":
                    self.main.show_details = not self.main.show_details
                    self.main.display_main()
                elif key == "ENTER":
                    self.main.projectsArray[self.main._selection].open_project()
                
            elif "param" == self.current :
                if key == "p":
                    logging.info("user open main windows")
                    self.param.save_param()
                    self.current = "main"
                    self.main.display_main()
                    self.logo.display_logo() # if in param change ""ui" : "logo"
                    # self.main.popup(f"logo :{self.logo.param_logo}")
                elif key == "SPACE":
                    self.param.change_value(self.param.get_selection_parametre())
                    self.param.display()
                elif key == "UP":
                    self.param.move_up()
                    self.param.display()
                elif key == "DOWN":
                    self.param.move_down()
                    self.param.display()