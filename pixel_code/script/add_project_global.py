import json
import uuid
from pixel_code.paths import PROJECTS_JSON, ensure_user_files

def add_project_global(path_json_projects=PROJECTS_JSON, path=None):
    """add new line on projects.json with pwd of 'path'"""
    ensure_user_files()

    if path is None:
        raise ValueError("path is required")

    # open/load json
    with open(path_json_projects, "r", encoding="utf-8") as f:
        data = json.load(f)
        print(path_json_projects)
        print(data)

    
    if path not in [project.get("path") for project in data.get("projects", [])]:
        ID = uuid.uuid4().hex[:8]
        project = {
            "id":ID,
            "path":path,
            "status":"todo"
        }
        data["projects"].append(project)

    # Save json
    with open(path_json_projects, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
