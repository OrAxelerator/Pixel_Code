import curses

def get_key(stdscr):
    k = stdscr.getch()

    return {
        ord('q'): "q",
        ord('p'): "p",
        curses.KEY_UP: "UP",
        curses.KEY_DOWN: "DOWN",
    }.get(k)
