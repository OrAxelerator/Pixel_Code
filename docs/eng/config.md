# Configuration

### Enable icons

To enable icons, use the **"0xProto Nerd Font"** font in your terminal, then turn on ``Use nerd font`` in the settings (``p`` key). If you run Pixel_Code inside VS Code, also set **Terminal › Integrated: Font Family** = `"0xProto Nerd Font"`.

> [!NOTE]
>
> Maybe your terminal doesn't support Nerd Fonts, then find an alternative.

> Link to install the font: https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/0xProto.zip

### Change settings

Use the settings screen with the ``p`` key. **Some settings are not editable** from this screen yet, change them directly in ``parametres.json`` (see [architecture](/docs/eng/architecture.md) for every key).

Settings available on the screen: language (``en``/``fr``), nerd font, editor (``code``/``vim``/``cmd``), repo (default link when adding a project), check update at launch, logo position, version (read only).

### Where are my files?

Pixel_Code uses ``platformdirs`` to store your files outside the code, so they are **kept during updates**:

| | ``parametres.json`` (settings) | ``projects.json`` and ``debug.log`` |
| --- | --- | --- |
| macOS | ``~/Library/Application Support/Pixel_Code/`` | ``~/Library/Application Support/Pixel_Code/`` |
| Linux | ``~/.config/Pixel_Code/`` (or according to your XDG variables) | ``~/.local/share/Pixel_Code/`` |
| Windows | ``C:\Users\<user>\AppData\Local\OrAxelerator\Pixel_Code\`` | ``C:\Users\<user>\AppData\Local\OrAxelerator\Pixel_Code\`` |

Each project also has a ``.pixelcode.json`` file at its root with its name, description, languages and repo.

### Debug mode

From the root of the clone, run: ``python3 pixel_code/__main__.py --debug`` (or ``py``/``python`` according to your OS). Logs are written in ``debug.log`` (see the table above), follow them with ``tail -f debug.log``.

In debug mode the update check is fake (see [update](/docs/eng/update.md#debug)), add ``--wifi`` to really check GitHub.

### Subcommands

| Command | Action |
| --- | --- |
| ``pixel-code --clean-projects`` | delete invalid projects if their path does not exist |
| ``pixel-code --clean-projects-hard`` | delete invalid projects if their path or their ``.pixelcode.json`` does not exist |
| ``pixel-code --reset-config`` | reset ``parametres.json`` (your projects are kept) |
| ``pixel-code --clear-log`` | clear ``debug.log`` |
| ``pixel-code --debug`` | enable debug logs |
| ``pixel-code --wifi`` | really check GitHub for updates, even in debug mode |
| ``pixel-code -h`` | show the help |
