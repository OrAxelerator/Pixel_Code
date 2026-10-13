# General project architecture

```
pixel_code/
├── __main__.py      # entry point (pixel-code), subcommands, runs the update after curses is closed
├── app.py           # class App : main loop, keys, update check
├── paths.py         # where user files are (platformdirs), default settings
├── data/logo.txt    # ascii logo
├── screens/         # curses windows (see below)
├── script/          # keyboard, projects (.pixelcode.json / projects.json), settings (ParamManager)
└── utils/           # translate(), update system
```

More details: [App](/docs/eng/App.md), [ParamManager](/docs/eng/param_manager.md), [update](/docs/eng/update.md).

## Data

User files are not stored in ``pixel_code/data``. Pixel_Code uses ``platformdirs`` to place them in the standard OS directories (see [config](/docs/eng/config.md)):

- ``parametres.json`` in the user config directory.
- ``projects.json`` in the user data directory.
- ``debug.log`` in the user data directory.

On launch, Pixel_Code creates these files if they do not exist (``ensure_user_files()`` in ``paths.py``) and migrates the old JSON files from ``pixel_code/data`` only if the new destination does not already exist.

### parametres.json

```json
{
    "schema_version": 1,
    "app": {
        "language": "en",                // "en", "fr"
        "use_nerd_font": false,          // icons
        "version": "0.6.0",              // always the installed version (pyproject.toml)
        "check_update_at_launch": true,
        "allow_prerelease": true         // pre-releases count as updates
    },
    "ui": {
        "theme": "default",              // does nothing for now
        "logo": "center",                // "center", "left"
        "display_project": "side"        // details of a project in the side panel
    },
    "projects": {
        "sort_by_last_opened": false,    // not used for now
        "sort_by_name": true,            // not used for now
        "editor": "code",                // "code" (VS Code), "vim", "cmd" (terminal)
        "repo": "github"                 // "github", "null" : default link when adding a project
    }
}
```

Missing keys take their default value (``DEFAULT_PARAMETRES`` in ``paths.py``).

### projects.json

Only the list of projects: where they are and their status.

```json
{
    "schema_version": 1,
    "projects": [
        {
            "id": "72b38123",                 // uuid4[:8]
            "path": "/Users/Axel/Pixel_Code",
            "status": "todo"                  // "todo", "done"
        }
    ]
}
```

### .pixelcode.json

The data of a project, saved **at the root of the project** (so it follows the project if it is copied/cloned).

```json
{
    "name": "Pixel_Code",
    "description": "...",
    "languages": ["python", "json"],
    "path": "/Users/Axel/Pixel_Code",
    "repo": "https://github.com/OrAxelerator/Pixel_Code.git"
}
```

A project of ``projects.json`` without ``.pixelcode.json`` is ignored at launch (a warning is written in ``debug.log``), use ``pixel-code --clean-projects-hard`` to remove it.

## How screens work (`screens`)

Screens in Pixel_Code are user interfaces built with the library `curses`. Each screen is a python class made to manage a specific part of the app. Each screen is initialized with a reference to the main app (`main_app`) from ``app.py`` to access shared resources like `stdscr` (the terminal window for curses) and the settings manager ``ParamManager``. Screens use curses windows (`newwin`) to display themselves. The active screen is saved in the variable `self.current` of the App class and can take ``"main"`` / ``"param"`` as value.

Here is the list of screens in ``/screens``:

### 1. `Logo`
- **File**: `screens/logo_screen.py`
- **Description**: Displays the ascii logo at the top of the screen.
- **Characteristics**:
  - Loads ``data/logo.txt``.
  - Displays the logo centered or on the left according to the user setting.

### 2. `MainScreen`
- **File**: `screens/main_screen.py`
- **Description**: Displays the list of projects and manages them (search, filter, add, edit, delete, status). The ``Project`` class (one per project, opens it with the editor) is in the same file.

### 3. `DetailPanel`
- **File**: `screens/detail_panel_screen.py`
- **Description**: Displays a panel with the details of the selected project in a window on the right.
- **Characteristics**:
  - Creates a window with borders.

> [see more](/docs/eng/screens/detailPannel.md)

### 4. `ParamScreen`
- **File**: `screens/param_screen.py`
- **Description**: Gives access to the settings of the app.
- **Characteristics**:
  - Displays the editable settings (list ``settings_config``, types ``cycle``, ``toggle`` and ``readonly``).
  - Displayed instead of MainScreen.

### 5. `Input`
- **File**: `screens/input_curses.py`
- **Description**: Manages user input in a text box.
- **Characteristics**:
  - The input box can have a title and pre-filled text.

Preview of all the windows in the terminal:
<img src="/docs/assets/interface.png" style='width:300px; height:220px; margin:0 auto;'>

## Translations

Every text displayed to the user must exist in English and French, with ``translate()`` (``utils/translate.py``):

```python
translate({"en": "Project saved.", "fr": "Projet enregistré."}, self.main_app.param_manager.get_data("app", "language"))
```
