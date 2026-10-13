# App.py

## Initialization

``__main__.py`` creates the class `App` inside ``curses.wrapper()``. In the init, `App` creates the ``ParamManager``, checks for updates, then creates all the screens:
- `Logo`
- `ParamScreen`
- `MainScreen`
- `DetailPanel`

With `self` as an argument, so every class has access to the other classes.

The full size window displayed (``"main"`` or ``"param"``) is saved in `self.current`, and the main loop is launched with `self.run()`.

---

## self.run()

Does:
- Check for updates (see [update](/docs/eng/update.md)). If the user accepts, ``run()`` stops here and the update is installed by ``__main__.py``.
- Display the logo.
- Display the `main` screen at start.
- Launch the `while True` loop.

This loop detects:
- Which key is pressed.
- What to do according to the screen (``self.current``).

---

## Keys input

> [!WARNING]
>
> `get_key()` doesn't return all the keys of the keyboard.

To add a key you need to add it in ``pixel_code/script/keybord.py``, in the condition ``os.name == "nt"`` (Windows) **AND** in the ``else`` (macOS / Linux), so it works on every OS. Then add what the key does in the loop of ``App.run()``.
