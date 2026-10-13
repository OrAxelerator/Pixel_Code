# ParamManager

ParamManager is a class (``/pixel_code/script/data/param_manager.py``) created in app.py as ``self.param_manager``. This class loads user settings from ``PARAMETRES_JSON`` defined in ``pixel_code/paths.py`` with ``self.load_param()`` and saves them with ``self.save_param()``. The file is stored in the user config directory through ``platformdirs``, so settings are kept during updates. To get data from it, use ``get_data(key_section, key)``.

Example:
```json
{
    "app": {
        "language": "en",
        ...
    }
}
```

> self.get_data("app", "language") = "en"

When loading, the values of the file are merged over ``DEFAULT_PARAMETRES`` (``paths.py``): a key missing in the file takes its default value. So to add a new setting, add it in ``DEFAULT_PARAMETRES`` (and in ``settings_config`` of ``ParamScreen`` to make it editable from the settings screen). ``app.version`` is always replaced by the installed version.

The idea of this class is that from everywhere, as long as you have access to it (through main), you can get the settings without reading the .json again.

However from the class ``Project``, getting data looks like: ``self.main_app.main_app.param_manager.get_data("projects", "editor")``
This can surely be reduced.
