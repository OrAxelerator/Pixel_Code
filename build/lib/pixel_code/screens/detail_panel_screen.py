import curses


class DetailPanel:
    def __init__(self, main_app):
        self.app = main_app
        self.stdscr = main_app.stdscr
        #self.main_screen = self.main_app

        h, w = self.stdscr.getmaxyx()
        self.win = curses.newwin(h-10, w//2, 10, w//2)
        self.win.border()
        self.win.refresh()
        
    def get_middle_x(self, text):
        return (self.win.getmaxyx()[1] // 2) - (len(text) // 2)


