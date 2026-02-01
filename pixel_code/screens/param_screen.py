import curses


class ParamScreen:
    def __init__(self, main_app):
        self.app = main_app
        h, w = main_app.stdscr.getmaxyx()

        self.win = curses.newwin(h-10, w, 10, 0)


        self.array = ["option1", "option2", "option3", "option4"]
        

        self._selection_parametre = 0

        # "app"
        self.language = "en" # Default value if error to read parametre.json
        self.use_nerd_font = False
        self.version = None
        self.check_update = True
        self.allow_prerelease = True

        # "ui"
        self.theme = "default"

        # "projects"
        self.sort_by_last_opened = True
        self.sort_by_name = False
        self.editor = "code"
        
        self.last_version = None # To load from github
                 
        self.load_param()
        self.parametre_array = [self.language, self.use_nerd_font, self.version] #here to get len() on setter



    def get_selection_parametre(self):
        return self._selection_parametre



    def display_param(self):
        self.win.clear()
        self.win.addstr(0,0, "PARAM SCREEN")
        for i, item in enumerate(self.array):
            self.win.addstr(i+1, 2, item)

        self.win.refresh()

