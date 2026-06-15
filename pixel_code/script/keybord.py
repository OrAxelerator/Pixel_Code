import os
import sys

# Detection of the keybord acording to the OS
if os.name == "nt":# Windows
    import msvcrt
else:
    import termios
    import tty

def get_key() -> str:
    """
    - "UP" for ^
    - "DOWN" for ˅
    - "SPACE" for space
    - "ENTER" for enter
    """
    if os.name == "nt": 
        key = msvcrt.getch()
        if key == b'q':
            return "q"
        elif key == b'p':
            return "p"
        elif key == b' ':
            return "SPACE"
        elif key == b'h':
            return "h"
        elif key == b'r':
            return "r"
        elif key == b'e':
            return "e"
        elif key == b'g':
            return "g"
        elif key == b'm':
            return "m"
        elif key == b'\r':   
            return "ENTER"

        # Special keys (arrows)
        elif key == b'\xe0':
            key = msvcrt.getch()
            if key == b'H':
                return "UP"
            elif key == b'P':
                return "DOWN"

        elif key == b'a':
            return "a"
        elif key == b'd':
            return "d"

        return None
    else:  # Linux / macOS
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch1 = sys.stdin.read(1)

            # Detection ENTER key
            if ch1 in ('\n', '\r'):
                return "ENTER"
            
            if ch1 == 'q':
                return "q"
            if ch1 == 'h':
                return "h"
            if ch1 == 's':
                return "s"
            elif ch1 == 'r':
                return "r"
            elif ch1 == 'e':
                return "e"
            elif ch1 == 'p':
                return "p"
            elif ch1 == 'a':
                return "a"
            elif ch1 == 'd':
                return "d"
            elif ch1 == 'g':
                return "g"
            elif ch1 == 'm':
                return "m"
            elif ch1 == ' ':
                return "SPACE"
            elif ch1 == '\x1b':  # ANSI sequence  for arrows
                ch2 = sys.stdin.read(1)
                ch3 = sys.stdin.read(1)
                if ch3 == 'A':
                    return "UP"
                elif ch3 == 'B':
                    return "DOWN"
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None
