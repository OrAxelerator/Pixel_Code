# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Pixel_Code is a curses-based TUI (Python ≥3.8) for organizing local projects and opening them in an editor (VS Code, vim, or a terminal). Entry point: `pixel-code` → `pixel_code.__main__:main`.

## Commands

```bash
pip install -e .                       # dev install (pipx install . on Linux)
pixel-code                             # run
python3 pixel_code/__main__.py --debug # debug mode; logs go to debug.log in the user data dir (tail -f it)
pixel-code -h                          # list subcommands
```

Subcommands: `--clean-projects`, `--clean-projects-hard`, `--reset-config`, `--clear-log`, `--debug`, `--wifi`.

There is no test suite, linter, or formatter configured.

## Architecture

**Flow:** `__main__.py` parses args, runs any maintenance subcommand, then `curses.wrapper` → `App` (`app.py`). `App.__init__` sets up logging, builds a `ParamManager`, checks GitHub for updates, then builds all screens and runs the main key loop. `App.current` (`"main"` / `"param"`) decides which screen handles each key.

**Screens** (`pixel_code/screens/`) are classes built with a reference to the `App` (`main_app`), which gives them `stdscr` and `param_manager`. Each draws into its own `curses.newwin`. `MainScreen` (`main_screen.py`) holds most of the app logic (list, search, filter, add/edit/delete, status toggle) plus the `Project` class, whose `open_project()` launches the configured editor via `subprocess`.

**Key input does not use curses' `getch`.** `script/keybord.py:get_key()` reads raw stdin (termios on POSIX, msvcrt on Windows) and returns names like `"UP"`, `"ENTER"`, `"SPACE"`, or the character. A new shortcut needs three changes: the **Windows branch** and the **POSIX branch** of `get_key()`, and the dispatch in `App.run()`.

**Two-level project storage:**
- `projects.json` (user data dir) is only a registry of `{id, path, status}`.
- Each project's metadata (name, description, languages, repo, …) is in `<project>/.pixelcode.json`. It is written by `script/add_project.py` and read by `script/load_project_local.py`. Registry entries without that file are skipped when loading.

**Settings and paths:** `paths.py` is the single source for file locations (via `platformdirs`), `DEFAULT_PARAMETRES`, and `ensure_user_files()`. That function creates files when missing and migrates old `pixel_code/data/*.json` files. `ParamManager` merges `parametres.json` over the defaults, so a new setting key must go in `DEFAULT_PARAMETRES`. To make it editable in the UI, also add an entry to `ParamScreen.settings_config` (types: `cycle`, `toggle`, `readonly`).

**Versioning/updates:** `APP_VERSION` comes from `importlib.metadata.version("pixel-code")`, so after bumping `version` in `pyproject.toml` you must reinstall before the change shows up. `ParamManager` always overrides `app.version` with it. At launch, `App.check_update()` asks the GitHub releases API (`utils/update.py`, 3 s timeout, so no connection means it just starts). If the user accepts, `App.update_tag` is set and `App.run()` returns before building the screens. After `curses.wrapper` returns, `__main__.py` runs `sys.executable -m pip install --upgrade <tag zip url>` in the plain terminal, so it works the same for pipx and pip. Editable installs are detected via `direct_url.json` and only get a "use git pull" message. In `--debug` without `--wifi`, it fakes `v999.9.9` (and skips the real update) so GitHub's API rate limit isn't hit. A release tag must be `v` + the exact `pyproject.toml` version, otherwise users get the prompt at every launch. Full details: `docs/eng/update.md`.

## Conventions (from CONTRIBUTING.md)

- Every user-facing string must work in English and French: `translate({"en": ..., "fr": ...}, param_manager.get_data("app", "language"))` from `utils/translate.py`.
- No `print()`/`input()` in TUI code (they break curses). Use `logging` for diagnostics. CLI subcommands that run before curses starts are the exception.
- Code comments in English. Must work on Linux, macOS, and Windows (`windows-curses` is a Windows-only dependency).
- Keep changes small and in line with the existing structure. AI use is allowed only for small, limited sections, not architecture design, and AI-written code must be reviewed by a human.
- Documentation exists in both `docs/eng/` and `docs/fr/` with the same content. Update both when behavior changes (e.g. key bindings, config keys, changelog). `README.md` is English, `docs/fr/README_FR.md` is its French twin.
