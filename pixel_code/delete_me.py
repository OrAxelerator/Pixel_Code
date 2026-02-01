# todo :
#   - sys of pip => installer.py
#   - Check if user have wifi
#   - make option to add pixelcode.json so when install new code VIA pixel_code pop to add project on fork on pixel code
#   -  make something cool with nerd font for icon
#   -  think about integration in pixel_nav => pixelcode.json ? ..
#   -  clearFormLine(line=12) hard-coded => bad, calcule height of logo ?
#   - programme de mise a jour automatique
#   - Do something cleaner at change_value() in Param
#   - projet.json : icone = ["":iconed de base, "favortite : icone + cœur, "]
#   - Use quit() func in main  instead of break in code
#   - # Make error message if pwd is False in open_code (Project)
#   - Use import color
#   - Choose IDE 

# coeur : 󱃪
# side project : 󰉌
# add folder : 

# icone (NF) : https://www.nerdfonts.com/cheat-sheet

# Call the code : "pixel-code"

# on macOs : pip install -e .
# on Ubuntu use pipx and write : pipx install . 
# on Windows 11 ... go see the README

import os
import json
import subprocess
import sys
import colorama
colorama.init()

from pixel_code.script.keybord import get_key
from pixel_code.script.get_update import get_update
from pixel_code.script.is_update_available import is_update_available
from pixel_code.script.translate import translate
from pixel_code.script.terminal.clear_terminal import clear_terminal
from pixel_code.script.terminal.clear_from_line import clear_from_line
from pixel_code.script.git.clone import clone_repo

import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


LOGO_TXT   = BASE_DIR / "data/logo.txt"
HEIGHT_LOGO = 12
PROJECTS_JSON = BASE_DIR / "data/projects.json"
PARAMETRES_JSON   = BASE_DIR  / "data/parametres.json"




from pixel_code.script.main_screen import Main
from pixel_code.script.param_screen import Param
from pixel_code.script.project import Project

import curses
from curses import textpad

size = os.get_terminal_size()
columns = size.columns
lines = size.lines

import curses
from app import App




def run(stdscr):
    app = App(stdscr)
    app.loop()

if __name__ == "__main__":
    curses.wrapper(run)
