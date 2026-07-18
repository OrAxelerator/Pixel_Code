import curses
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))



from pixel_code.script.keybord import get_key
from pixel_code.screens.logo_screen import Logo
from pixel_code.screens.main_screen import MainScreen
from pixel_code.screens.param_screen import ParamScreen
from pixel_code.screens.detail_panel_screen import DetailPanel
from pixel_code.screens.input_curses import Input
from pixel_code.script.data.param_manager import ParamManager
from pixel_code.paths import LOG_FILE, ensure_user_files
from pixel_code.utils.update import get_latest_version
from pixel_code.utils.translate import translate
# Start debug mod with python3 pixel_code/__main__.py --debug

ensure_user_files()
# level = logging.DEBUG if "--debug" in sys.argv else logging.INFO

# logging.debug("Valeur de x ")   # affiché seulement en --debug
# logging.info("APP LAUNCH")   # affiché en --debug ET mode normal
# logging.warning("Problème détecté")    # toujours affiché
class App:
    def __init__(self, stdscr, debug):
        level = logging.DEBUG if debug else logging.INFO
        logging.basicConfig(
            filename=LOG_FILE,
            level=level,
            format="%(asctime)s [%(levelname)s] %(message)s"
        )
        logging.debug("-" * 15 + " init() " + "-" * 15)
        logging.debug(f"debug value : {debug}")
        self.stdscr = stdscr
        
        self.param_manager = ParamManager()
        
        # self.win_input = curses.newwin(3, w, h - 3, 0)
        # self.input = Input(self,)
 

        self.current = "main" #("main", "parametre")
        self.run()

    def launch_curses(self):
        self.stdscr.keypad(True)
        curses.curs_set(0)

        self.h, self.w = self.stdscr.getmaxyx()
        self.logo = Logo(self)
        self.param = ParamScreen(self)
        self.main = MainScreen(self)
        self.detail_panel = DetailPanel(self)




    def check_update(self) -> tuple[bool, list, list]:
        """
        True : A new versions (pre-realse) is available
        False : Version install is the lastest
        """
        current = self.param_manager.get_data("app", "version")
        
        
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG:
            lastest = ["999", "9", "9"] # debug
        else:
            last = get_latest_version()
            logging.debug("last")
            logging.debug(last)
            lastest = last["tag_name"][1::] # in github there "v"X.X.X
            
            lastest = lastest.split(".")

        current = current.split(".")
        logging.debug(f"actual version : {current}")
        logging.debug(f"last version : {lastest}")


        for i in range(3):
            if int(current[i]) == int(lastest[i]):
                continue
            elif int(current[i]) < int(lastest[i]):
                logging.debug("New versions detected")
                return True, current, lastest
            else:
                logging.debug("No new version")
                return False, current, lastest
            
        logging.debug("No new version")

        return False, current, lastest # if same version

    def run(self):
        
        # CAUTION while debuging you can be blocked by github api 
        # if you check too many times in a short time
        # has_update, current, latest = True, self.param_manager.get_data("app", "version").split("."), [9,9,9] #use this for debuging

        has_update, current, latest = self.check_update()

        if has_update:
            txt = {
                "en" : f"New versions avaible v{current[0]}.{current[1]}.{current[2]} -> v{latest[0]}.{latest[1]}.{latest[2]}, update ? [Y/n]",
                "fr" : f"Nouvelle version disponible v{current[0]}.{current[1]}.{current[2]} -> v{latest[0]}.{latest[1]}.{latest[2]}, installez ? [Y/n]"
            }
            self.stdscr.addstr(0,0, translate(txt, self.param_manager.get_data("app", "language")))
            self.stdscr.refresh()
            res = self.stdscr.getch()
            logging.debug(res)
            res = chr(res)
            # logging.debug(res == chr(10)) # chr = ENTER
            if res in ("Y", "y", chr(10), " ", None):
                logging.debug("UPDATING")
                if latest == ["999", "9", "9"]:
                    logging.debug("DEBUG MODE, no update")
                else:
                    # fc is on the path /update.py
                    from update import main
                    main() # call main from update.py
                    logging.debug("UPDATE DONE")
                    self.stdscr.addstr(1,0, "Update done, please restart the app")
                    self.stdscr.refresh()
                    self.stdscr.getch()
                    exit(0)
                #call main from update.py
            else:
                logging.debug("No updating")



        self.launch_curses()

        logging.info("-" * 10 + " START Application, run() " + "-" * 10)
        self.logo.display_logo()
        self.main.display_main()
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
                elif key == "e":
                    self.main.edit_project()
                    self.main.display_main()
                elif key == "g":
                    self.main.pull_project()
                    pass #gt clone, git pull, git reset
                    #electon input like main with arrow
                elif key == "m":
                    self.main.toggle_project_status()
                    self.main.display_main()
                elif key == "/":
                    self.main.search_project()
                    self.main.display_main()
                elif key == "c":
                    self.main.clear_search()
                    self.main.display_main()
                elif key == "f":
                    self.main.cycle_status_filter()
                    self.main.display_main()
                elif key == "UP":
                    self.main.move_up()
                    self.main.display_main()
                elif key == "DOWN":
                    self.main.move_down()
                    self.main.display_main()
                elif key == "SPACE":
                    if self.main.get_selected_project() is None:
                        self.main.reset_project_view()
                    else:
                        self.main.show_details = not self.main.show_details
                    self.main.display_main()
                elif key == "ENTER":
                    project = self.main.get_selected_project()
                    if project is not None:
                        project.open_project()
                
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
