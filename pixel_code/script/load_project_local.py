import logging
import json

def get_project_data(PATH :str) -> dict | bool:
    """return False if pc.json is not found else return a dict with all data"""
    try:
        PATH += "/.pixelcode.json"
        with open(PATH, encoding="utf-8") as f:
            DATA = json.load(f)
            return DATA

    except FileNotFoundError:
        logging.warning(f".pixelcode.json not found in {PATH}")        
        return False # ERROR
            #"Fichier projets.json introuvable.
            # self.projet = {} so..