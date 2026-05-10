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


def run(stdscr):
    App(stdscr)
    


def main():
    if "--clean-projects" in sys.argv:
        clean_invalid_projects(False)
        sys.exit(0)
    if "--clean-projects-hard" in sys.argv:
        clean_invalid_projects(True)
        sys.exit(0)

    curses.wrapper(run) # lauch normally


if __name__ == "__main__":
    main()
