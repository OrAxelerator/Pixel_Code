import os
import sys
from subprocess import run


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from script.name import is_dir_empty
from script.git.repo_name import get_name_repo
from script.delete import delete_dir
        
def clone_repo(url : str):
    name = get_name_repo(url)
    if is_dir_empty(name):
        if not delete_dir(name):
            return False 
            
    run(["git", "clone", url], check=True)
    return True


#url = "https://github.com/OrAxelerator/trophee-nsi-ant.git" # start to pass / {name} = 19
#clone_repo(url)