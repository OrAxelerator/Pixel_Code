import json
from pathlib import Path
import logging

def create_pixelcode_config(data_projects: dict):
    """
    Create .pixelcode.json file in the folder of the project.
    Crée un fichier .pixelcode.json dans le dossier du projet.
    """

    project_path = Path(data_projects["path"]).expanduser().resolve()
    # with open(project_path/"test.json", "w", encoding="utf-8") as f:
    #     json.dump(data_projects, f, indent=4, ensure_ascii=False)
        
    config_file = project_path / ".pixelcode.json"

    if not project_path.exists():
        logging.debug(f"Dossier projet introuvable : {project_path}")
        return False

    if config_file.exists():
        logging.debug(f"\n{"-"*10}\nCONFIG FILE ALREADY EXISTE (.pixelcode.json) \nDelete it with : rm {config_file}\n{"-"*10}")
        return False
        

    # default config
    config_data = { 
        "name": data_projects["name"],
        "description": data_projects["description"],
        "path": data_projects["path"],
        "version": "0.1.0",
        "languages": data_projects["languages"],
        "repo": data_projects.get("repo", ""),
        "tags": [],
        "last_opened": None
    }

    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(data_projects, f, indent=4, ensure_ascii=False)
