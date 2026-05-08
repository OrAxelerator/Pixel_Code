# ParamManager

ParamManger is a class (``/pixel_code/script/data/param_manager.py``) created in app.py as ``self.param_manager``. This class loads user settings from ``PARAMETRES_JSON`` defined in ``pixel_code/paths.py`` with self.load_param() and saves them with self.save_param(). The file is stored in the user config directory through ``platformdirs``, so settings are preserved during updates. To get data from it, use get_data(key_section, key).

exemple : 
```json
{
    "app": {
        "language": "en",
        ...
    }
}
```

> self.get_data("app", "language") = "en"

The idea of this class is from everywhere, [tantque] you have access to it (by main) you can get access to it without read again .json.

However from class Project to get data look : ``self.main_app.main_app.param_manager.get_data("projects", "editor")``
This can surely be reduced.
