# Update system

## For users

At launch, Pixel_Code checks GitHub for a newer version. If it finds one, it asks:

```
New version available v0.6.0 -> v0.6.1, update ? [Y/n]
```

* **Y / ENTER / SPACE**: Pixel_Code closes, installs the new version (you can see pip's output in the terminal), then asks you to relaunch with `pixel-code`.
* **any other key**: Pixel_Code starts normally.

Your projects and settings are **never touched** by an update: they are stored outside the code (see [config](/docs/eng/config.md)).

> [!NOTE]
>
> * **No connection?** Pixel_Code waits at most 3 seconds for GitHub, then starts normally without asking anything.
> * To disable the check: set ``check_update_at_launch`` to ``false`` in the settings (``p`` key) or in ``parametres.json``.
> * ``allow_prerelease`` (in ``parametres.json``) chooses whether pre-releases count as updates. For now every Pixel_Code release is a pre-release, so leave it to ``true``.

### Installed with `pip install -e .`?

In that case the code comes from your git clone, so Pixel_Code doesn't install anything: it tells you to update with ``git pull`` in the folder of the clone.

### Update by hand

If the automatic update fails, reinstall from a fresh clone:

```bash
git clone https://github.com/OrAxelerator/Pixel_Code.git
cd Pixel_Code
pipx install --force .   # or : pip install --upgrade .
```

> [!IMPORTANT]
>
> Versions **0.5.2 and older** use the old update system, which doesn't work with pipx. Reinstall them by hand **once** (commands above). After that, updates are automatic.

---

## For developers

Code: ``pixel_code/utils/update.py``, called from ``App.run()`` (``app.py``) and ``__main__.py``.

1. ``App.check_update()`` asks the GitHub API (``/repos/OrAxelerator/Pixel_Code/releases``, timeout 3s) for the most recent release. Any error (no connection, rate limit, 404...) returns ``None`` and Pixel_Code just starts.
2. The release tag (``vX.Y.Z``) is compared with the installed version (``importlib.metadata.version("pixel-code")``, i.e. ``version`` in ``pyproject.toml``).
3. If the user accepts, the tag is saved in ``App.update_tag`` and the ``App`` stops **before** launching the interface.
4. Once curses is closed, ``__main__.py`` runs:
    ```bash
    <python of Pixel_Code> -m pip install --upgrade https://github.com/OrAxelerator/Pixel_Code/archive/refs/tags/vX.Y.Z.zip
    ```
    Using the python that runs Pixel_Code (``sys.executable``) means it works the same way with pipx and with pip.

### Publishing a new version

1. Change ``version`` in ``pyproject.toml`` (e.g. ``0.6.1``).
2. Merge in ``main``, then create a GitHub release with the tag **``v`` + the same version** (``v0.6.1``).

> [!WARNING]
>
> If the tag and ``pyproject.toml`` don't match, users get the update prompt at every launch (this happened with v0.5.0).

### Debug

In ``--debug`` mode, Pixel_Code does **not** contact GitHub (too many requests get you blocked for a while) and shows a fake ``v999.9.9`` update, which does nothing when accepted. Add ``--wifi`` to really check GitHub in debug mode:

```bash
python3 pixel_code/__main__.py --debug --wifi
```
