import argparse
import os
import sys
import curses
import json

# Import robuste (installé / -m / fichier direct)

try:
    from app import App
except Exception:
    try:
        from .app import App
    except Exception:
        sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
        from app import App

from pixel_code.paths import PROJECTS_JSON, ensure_user_files


def clean_invalid_projects(hard:bool):
    """
    hard = True : delete project from projects.json if the path WITH .pixelcode.json doesn't existe
    hard = False : delete project from projects.json if the path doesn't existe
    """
    ensure_user_files()
    try:
        with open(PROJECTS_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        original_count = len(data.get("projects", []))
        
        

        valid_projects = []
        for p in data["projects"]:
            if os.path.exists(os.path.join(p["path"], ".pixelcode.json") if hard else p["path"]):
                valid_projects.append(p)
        data["projects"] = valid_projects
        
        new_count = len(data["projects"])
        
        with open(PROJECTS_JSON, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print(f"Deleted project : {original_count - new_count}")
        print(f"Number of project remaining : {new_count}")
    except Exception as e:
        print(f"Error : {e}")



def reset_confif():
    from pixel_code.paths import DEFAULT_PARAMETRES, _write_json, PARAMETRES_JSON
    _write_json(PARAMETRES_JSON, DEFAULT_PARAMETRES)

def clear_log():
    from pixel_code.paths import LOG_FILE
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("")


def parse_args():
    parser = argparse.ArgumentParser(description="Pixel Code application launcher")
    parser.add_argument("--clean-projects", action="store_true", help="Delete invalid projects if the path does not exist")
    parser.add_argument("--clean-projects-hard", action="store_true", help="Delete invalid projects if .pixelcode.json is missing")
    parser.add_argument("--reset-config", action="store_true", help="Reset setting of user not all of his projects")
    parser.add_argument("--clear-log", action="store_true", help="Clear debug.log")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    return parser.parse_args()



def run(stdscr, debug: bool = False):
    App(stdscr, debug=debug)
    


def main():
    args = parse_args()

    if args.clean_projects:
        clean_invalid_projects(False)

    if args.clean_projects_hard:
        clean_invalid_projects(True)

    if args.reset_config:
        reset_confif()

    if args.clear_log:
        clear_log()

    if args.clean_projects or args.clean_projects_hard or args.reset_config :
        input("ENTER TO LAUNCH Pixel_Code")
    else:
        sys.exit(0)

    curses.wrapper(lambda stdscr: run(stdscr, debug=args.debug))



if __name__ == "__main__":
    main()
