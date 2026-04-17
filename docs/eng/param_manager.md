# ParamManager

ParamManger is a class (``/pixel_code/script/data/param_manager.py``) create in app.py in  ``self.param_manager``. this class load user settings  (/data/parametre.json) with self.load_param() and save them with self.save_param(). To get a data of it use get_data(key_section, key).

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