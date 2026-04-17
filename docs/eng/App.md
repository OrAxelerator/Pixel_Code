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

## Gestion des touches

>[!WARNING]
>
> `get_key()` function does't return all of the key

To add a specific key yoiu need to add it on 
`pixel_code/script/keybord.py` in the condition os == "nt" (windows) **AND** os == "Darwin" ("macos")  **AND** Linux.
So it works on every OS.