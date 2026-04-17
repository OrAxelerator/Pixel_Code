# Architecture général du projet


### Les paramètres :

```
{
    "app": {
        "language": "en", ("fr", "en")
        "use_nerd_font": true, # Icone
        "version": "v0.4.0",
        "check_update_at_launch": true,
        "allow_prerelease": true
    },
    "ui": {
        "theme": "default", # Do nothing for now
        "logo": "left" # positoin of the logo ("center", "left")
    },
    "projects": {
        "sort_by_last_opened": true,
        "sort_by_name": false,
        "editor": "code" # ("code", "vim", "cmd")
    }
}
```

### Projects.json : 

```
{
    "projects": [
        {
            "id": "72b38123", #
            "path": "/Users/Axel/Pixel_Code",
            "status": "todo" # ("todo", ...)
        }, ...
    ]
}

```
## How screen works (`screens`) ?

Screens on Pixel_Code are user interface build with the librarie `curses`. Each screen is built on a python class and is made to manage a specific part of the app. Also each screen is init with a reference to the main app (`maain_app`) from ``app.py`` for access to share ressource like `stdscr` (windows of the terminal for curses) and the setting manager ``ParamManger``. Screens use curses windows  (`newwin`) to display themselve. The active screen is save on the variable `self.current` in the App class and can take "main" / "parametre" for value

Here a list of screens ``/screens``:

### 1. `Logo`
- **File** : `screens/logo_screen.py`
- **Description** : Display the ascii Logo on the top of the screen.
- **Characteristics** :
  - Load ``data/logo.txt``.
  - Can display the logo in center or left according to user setting.


### 2. `MainScreen`
- **File** : `screens/main_screen.py`
- **Description** : Display the list of procjects.


### 3. `DetailPanel`
- **File** : `screens/detail_panel_screen.py`
- **Description** : Display a pannel with details of the selected project in a new windows on the right.
- **Characteristics** :
  - Create a windows with border.

### 4. `ParamScreen`
- **File** : `screens/param_screen.py`
- **Description** : Give acess to manage setting of the app.
- **Characteristics** :
  - Display the modifiable setting.
  - Display on top of MainScreen.
  
### 5. `Input`
- **File** : `screens/input_curses.py`
- **Description** : Manage user input in a text box.
- **Characteristics** :.
  - Input box can have a title and have pre-fill text in it.

Preview of all the windows in the terminal :
<img src="/docs/assets/interface.png" style='with:300px; height:220px; margin:0 auto;'>

---

