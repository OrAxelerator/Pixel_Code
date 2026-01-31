import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle


def prompt_text(stdscr, txt):    
    h, w = stdscr.getmaxyx()

    box_width = w - 10
    start_x = 5
    start_y = 1   

    stdscr.addstr(start_y - 5 + h, start_x, f"{txt} :")

    rectangle(
        stdscr,
        start_y+ h - 4,
        start_x - 1,
        start_y  + h - 2,
        start_x + box_width
    )

    win = curses.newwin(1, box_width, start_y +h - 3, start_x)
    box = Textbox(win)

    stdscr.refresh()

    box.edit()
    text = box.gather().strip()
    win.clear()
    return text


def prompt_text_wrapper(txt):
    return wrapper(lambda stdscr: prompt_text(stdscr, txt))

