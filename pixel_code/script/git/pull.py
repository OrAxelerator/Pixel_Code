import os

def git_pull(dir):
    """in: dir to where to git pull"""
    os.chdir(dir)
    os.system("git pull")
