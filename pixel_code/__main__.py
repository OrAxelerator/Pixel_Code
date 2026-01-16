import os
import sys

# Try absolute import (works when package is installed or run with -m),
# otherwise try relative import (works when executed as package),
# otherwise add parent dir to sys.path as a last resort (works when running file directly).
try:
    from app import Main
except Exception:
    try:
        from .app import Main
    except Exception:
        sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
        from app import Main


def main(): 
    Main()


if __name__ == "__main__":
    main()
