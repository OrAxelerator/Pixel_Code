import os
import sys
import curses

# Import robuste (installé / -m / fichier direct)
try:
    from app import App
except Exception:
    try:
        from .app import App
    except Exception:
        sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
        from app import App


def run(stdscr):
    App(stdscr)
    


def main():
    curses.wrapper(run)


if __name__ == "__main__":
    main()
