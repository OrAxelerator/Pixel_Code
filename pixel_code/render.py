# render.py
import curses

class Renderer:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.y = 0

    def addstr(self, text, x=0, y=None):
        if y is None:
            y = self.y
            self.y += text.count("\n") + 1
        self.stdscr.addstr(y, x, text)

    def clear(self):
        self.stdscr.clear()
        self.y = 0

    def refresh(self):
        self.stdscr.refresh()

    def getkey(self):
        """Get a key press from the user."""
        return self.stdscr.getkey()

    def getch(self):
        """Get a character input from the user."""
        return self.stdscr.getch()

    def move_cursor(self, y, x):
        """Move the cursor to a specific position."""
        self.stdscr.move(y, x)
