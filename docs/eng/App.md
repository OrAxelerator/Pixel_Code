# App.py

## Initialization


In the init, the class`App` manage to create all these class  :
- `Logo`
- `ParamScreen`
- `MainScreen`
- `DetailPanel`
- `ParamManager`

With  `self` as an argument, So every class have an access to can access to other class.

And full size windows like "main" and "parametre" are save in `sefl.current`, and the main loop lauch with `self.run()`.

---

## self.run()

Do :
- Display logo.
- Display `main` screen  at start.
- Lauch  `while True`.

This loop detect :
- Wich key is pressed.
- What to do according to the screen.

---

## Keys input

>[!WARNING]
>
> `get_key()` function does't return all of the key

To add a specific key yoiu need to add it on 
`pixel_code/script/keybord.py` in the condition os == "nt" (windows) **AND** os == "Darwin" ("macos")  **AND** Linux.
So it works on every OS.

## Update system

``update.py `` download last version from github (can be a release or pre-release) to /update, delete all file/folder from root of project and move all stuff of new versions in /update to ../ (root of project)

In debug mode update checker (execute before launching pixel_code)
do not ping github.com to get last versions but return v999.9.9 (cause by ping github.com every time he block my ip).