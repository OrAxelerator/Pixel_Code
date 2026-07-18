# Required configuration:

* To enable icons:

    To enable icons you need to use **"0xProto Nerd Font"** in your terminal. If you run Pixel_Code inside VS Code, also set **Terminal › Integrated: Font Family** = `"0xProto Nerd Font"`.

    > Link to install the font : https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/0xProto.zip

<br>

* Change settings:

    To change settings, use the settings screen with the ``p`` key. **Some settings may not yet be editable** from this screen.
    Settings are stored in the user config directory managed by ``platformdirs``:
    - macOS: ``~/Library/Application Support/Pixel_Code/parametres.json``
    - Linux: ``~/.config/Pixel_Code/parametres.json`` or according to your XDG variables
    - Windows: ``C:\Users\<user>\AppData\Local\OrAxelerator\Pixel_Code\parametres.json``

>[!NOTE]
>
> Projects are stored separately in the user data directory:
> - macOS: ``~/Library/Application Support/Pixel_Code/projects.json``
> - Linux: ``~/.local/share/Pixel_Code/projects.json``
> - Windows: ``C:\Users\<user>\AppData\Local\OrAxelerator\Pixel_Code\projects.json``
>
> These files are preserved even if Pixel_Code's source code is replaced during an update.


>[!NOTE]
>
> To launch in **debug mode**:
>   From the project root, run: ``python3 pixel_code/__main__.py --debug`` (or py/python according to your OS). Logs are written to ``debug.log`` in the user data directory. (tail -f debug.log)

Sub commande : 
    - --clean-projects :  Delete invalid projects if the path does not exist
    - --clean-projects-hard : Delete invalid projects if .pixelcode.json is missing or the path does not exist
    - --reset-config : reset parametres.json
    - --clear-log : clear the debug.log file
    You can see help with ``pixel-code -h```

