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
from pixel_code.script.data.param_manager import ParamManager
from pixel_code.paths import LOG_FILE, ensure_user_files, APP_VERSION
from pixel_code.utils.update import get_latest_release, is_newer, get_editable_location
from pixel_code.utils.translate import translate
# Start debug mod with python3 pixel_code/__main__.py --debug

ensure_user_files()

DEBUG_TAG = "v999.9.9"
# level = logging.DEBUG if "--debug" in sys.argv else logging.INFO

# logging.debug("Valeur de x ")   # affiché seulement en --debug
# logging.info("APP LAUNCH")   # affiché en --debug ET mode normal
# logging.warning("Problème détecté")    # toujours affiché
class App:
    def __init__(self, stdscr, debug, wifi: bool = False):
        level = logging.DEBUG if debug else logging.INFO
        logging.basicConfig(
            filename=LOG_FILE,
            level=level,
            format="%(asctime)s [%(levelname)s] %(message)s"
        )
        logging.debug("-" * 15 + " init() " + "-" * 15)
        logging.debug(f"debug value : {debug}")
        logging.debug(f"wifi value : {wifi}")
        self.stdscr = stdscr
        self.wifi = wifi
        
        self.param_manager = ParamManager()
        self.update_tag = None # tag of the release to install when Pixel_Code is closed
        
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




    def check_update(self) -> dict | None:
        """
        Return the github release if a new version is available, else None.
        Return None too if user doesn't have connection.
        """
        if not self.param_manager.get_data("app", "check_update_at_launch"):
            logging.debug("Update check disabled in parametres.json")
            return None

        # CAUTION while debuging you can be blocked by github api
        # if you check too many times in a short time, so use --wifi to really check
        if logging.getLogger().getEffectiveLevel() == logging.DEBUG and not self.wifi:
            logging.debug("Debug mode : fake release v999.9.9")
            return {"tag_name": DEBUG_TAG}

        release = get_latest_release(self.param_manager.get_data("app", "allow_prerelease"))
        if release is None:
            return None

        logging.debug(f"actual version : {APP_VERSION}")
        logging.debug(f"last version : {release['tag_name']}")
        if is_newer(release["tag_name"], APP_VERSION):
            logging.debug("New version detected")
            return release

        logging.debug("No new version")
        return None

    def ask_update(self, release: dict):
        """Ask user to update, if yes save the tag in self.update_tag (installed after curses is closed)"""
        lang = self.param_manager.get_data("app", "language")
        tag = release["tag_name"]
        txt = {
            "en" : f"New version available v{APP_VERSION} -> {tag}, update ? [Y/n]",
            "fr" : f"Nouvelle version disponible v{APP_VERSION} -> {tag}, installer ? [Y/n]"
        }
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, translate(txt, lang))
        self.stdscr.refresh()
        res = self.stdscr.getch()
        if res not in (ord("Y"), ord("y"), 10, 13, ord(" ")):
            logging.debug("No updating")
            return

        if tag == DEBUG_TAG:
            logging.debug("DEBUG MODE, no update")
            return

        editable_location = get_editable_location()
        if editable_location is not None:
            # "pip install -e ." : the code is a git repo, pip must not replace it
            txt = {
                "en" : f"Pixel_Code is installed with 'pip install -e', update it with 'git pull' in {editable_location}. Press a key to continue.",
                "fr" : f"Pixel_Code est installé avec 'pip install -e', mettez le à jour avec 'git pull' dans {editable_location}. Appuyez sur une touche pour continuer."
            }
            self.stdscr.addstr(2, 0, translate(txt, lang))
            self.stdscr.refresh()
            self.stdscr.getch()
            return

        self.update_tag = tag

    def run(self):
        release = self.check_update()
        if release is not None:
            self.ask_update(release)
            if self.update_tag is not None:
                return # quit curses, update is done in __main__.py
        self.stdscr.clear()
        self.stdscr.refresh()

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
