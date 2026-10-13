# Changelog

All the important modifications are documented here.

Format: Y-M-D

---

## [0.6.0] - not released yet

### Changed
- New update system, simple and working with pipx and pip: at launch Pixel_Code proposes the new version, then installs it with pip directly from the GitHub release ([see doc](/docs/eng/update.md)).
    - If there is no connection, Pixel_Code waits at most 3 seconds then starts normally.
    - The settings ``check_update_at_launch`` and ``allow_prerelease`` are used.
    - With ``pip install -e .``, Pixel_Code tells you to use ``git pull`` instead.
- The version in the settings is always the installed version.
- Python 3.10+ is required (the code didn't work with older versions anyway).
- Every message of the interface and of the subcommands is in English and French.
- Key ``g`` shows "not available yet" instead of running unfinished git commands.
- Documentation finished and identical in English and French.

### Deleted
- ``update.py`` and the ``update/`` folder (old update system, it deleted and replaced the files of the clone).

> [!IMPORTANT]
>
> Coming from v0.5.2 or older: reinstall once by hand (``pipx install --force .`` in a fresh clone).

---

## [0.5.2] - 2026-07-31

### Changed
- Fix: version in ``pyproject.toml`` was not updated.

---

## [0.5.1] - 2026-07-31

### Added
- ``--wifi`` subcommand: really check the last version on GitHub, even in debug mode.

### Changed
- Fix the fetch of the last version on GitHub, more security when the GitHub data is wrong.

---

## [0.5.0] - 2026-07-18

### Added
- 4 new subcommands:
    - ``--clean-projects``: delete invalid projects if the path does not exist
    - ``--clean-projects-hard``: delete invalid projects if ``.pixelcode.json`` is missing or the path does not exist
    - ``--reset-config``: reset ``parametres.json``
    - ``--clear-log``: clear the ``debug.log`` file

    You can see help with ``pixel-code -h``
- Icons on the settings screen.
- Warning in ``debug.log`` when ``.pixelcode.json`` is not found in the path of a project.
- Edit a project with "e".
- Update system.
- Search a project (``/``), filter by status (``f``), mark a project done (``m``).

### Changed
- Pixel_Code uses ``platformdirs`` to place user files in the standard OS directories:
    - ``parametres.json`` in the user config directory.
    - ``projects.json`` in the user data directory.
    - ``debug.log`` in the user data directory.
- More debug/warning messages in ``debug.log``.
- ``logging.basicConfig`` is now in App.
- How the script gets args in ``__main__.py``.
- Default settings get the version from ``pyproject.toml`` (the version installed on your machine).
- ``first_use.py`` works with the new platformdirs data.
- Fix: version was 0.4.1 and not 0.5.0.

---

## [0.4.0] - 2026-04-16

### Changed
- Interface managed with `curses` (a lot better than print).
- Better support for multi-language with **ParamManager**.
- Management of projects: all the data is in ``.pixelcode.json`` at the root of the project.
- Debug mode (``--debug``).
- New settings window.
- Better global architecture (``/screens``, ``/utils``).

### Added
- Documentation fr/eng.
- ParamManager [see doc](/docs/eng/param_manager.md).

### Deleted
- Display project mode "bottom" (├─ description : ...).
- Github features.

---

## [0.3.0] - 2026-01-26

### Added
- Git feature, key "g" to clone/pull a project.

---

## [0.2.0] - 2026-01-18

### Added
- Key "a" to add a project.

---

## [0.1.2] - 2026-01-16

### Changed
- New architecture with ``/script`` and ``/data``, and ``project.json`` with all the data in it.

---

## [0.1.1] - 2025-12-31

### Added
- Keyboard navigation system.
- Multi-language support.
- View "bottom".
- Settings window (language, nerd font, "tuto").
- Multi OS (just print()).
