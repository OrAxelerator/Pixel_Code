import subprocess
import os

def exec_sh(script_name: str):
    """
    Exécute un script .sh situé dans pixel_code/script/sh
    :param script_name: nom du script sans .sh
    """
    
    base_dir = os.path.dirname(__file__)  # dossier actuel (script)
    sh_dir = os.path.join(base_dir, "sh")
    
    script_path = os.path.join(sh_dir, f"{script_name}.sh")
    
    if not os.path.isfile(script_path):
        print(f"[ERREUR] Script introuvable: {script_name}.sh")
        return
    
    try:
        result = subprocess.run(
            ["bash", script_path],
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        
        if result.stderr:
            print("[ERREUR SCRIPT]")
            print(result.stderr)
    
    except Exception as e:
        print(f"[ERREUR EXECUTION] {e}")