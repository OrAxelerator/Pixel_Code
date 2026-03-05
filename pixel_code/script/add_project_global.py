import json
import uuid

def add_project_global(path_json, path):
    """add new line on projects.json with pwd of 'path'"""

    # open/load json
    with open(path_json, "r") as f:
        data = json.load(f)
    
    if path not in data.get("projects", []):
        ID = uuid.uuid4().hex[:8]
        project = {
            "id":ID,
            "path":path,
            "status":"todo"
        }
        data["projects"].append(project)

    # Save json
    with open(path_json, "w") as f:
        json.dump(data, f, indent=4)