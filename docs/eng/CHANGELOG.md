# Changelog

All the important modification are documented here

Format : Y/M/D

---

## [0.1.1] - 2025-12-31

### Added
- Add navigation systeme for keybord
- Add multi-language support
- Add view "bottom"
- Add setting windows (lang, nerdfont, "tuto")
- muti os (just print())

---

## [0.1.2] - 2026-01-16

### Changed
- New architecture with  ``/script`` and ``/data`` and project.json with all the data in it.

---

## [0.2.0]

### Added
- key bind "a" for add a project

---

## [0.3.0] - 2026-01-26

### Added
-  Git feature, key "g" for clone/pull projet

---

## [0.4.0] - 2026-05-16


### Changed
- Interface manage with `curses` (a lot better than print)
- Best support for multi-language with **paramManager**.
- Management of projects : all the data are in .pixelcode.json to the root of the project 
- Debug mod (--debug)
- New setting windows
- Better Global architecture  (/screens /utils)

### Added :
- Documentation fr/eng
- ParamManger [see doc](/docs/eng/param_manager.md)

### Deleted
- Display project mod "bottom" (├─ description : ...)
- Github features


## [0.5.0] - 

### Added :
- 4 new subcommande :
    - --clean-projects :  Delete invalid projects if the path does not exist
    - --clean-projects-hard : Delete invalid projects if .pixelcode.json is missing or the path does not exist
    - --reset-config : reset parametres.json
    - --clear-log : clear the debug.log file
    You can see help with ``pixel-code -h```
- Icon on paramScreen.

### Changed : 
- Pixel_Code uses ``platformdirs`` to place them in the standard OS directories:
    - ``parametres.json`` in the user config directory.
    - ``projects.json`` in the user data directory.
    - ``debug.log`` in the user data directory.
- More debug/warming message in debug.log
- logging.basicConfig is now In App
- How the script get args in __main_.py
- Default parametres get version now with what is write in pyproject.tmol (Attention it return version from the downloaded version in your machine)

- fisrt_use.py work with new platformdirs data.


### Added
- Edit project function with "e" (just a lot of input)

### Added
- Update system (none integreted yet)

### Added
- Search option/marked option to project