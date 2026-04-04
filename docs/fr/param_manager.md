# ParamManager


ParamManger est une classe (``/pixel_code/script/data/param_manager.py``) créer dans  app.py dans la variable ``self.param_manager``. Cette classe charge les parametres utilisateur (/data/parametre.json) avec self.load_param() et enregistre les données avec self.save_param(). Pour obtenir une donnés il suffit d'accceder a la classe et utilisier get_data(key_section, key)

ex : 
```json
{
    "app": {
        "language": "en",
        ...
    }
}
```

> self.get_data("app", "language") = "en"

L'idée de cette classe et que depuis n'importe ou, tant qu'il y a un accès a la classe main on puisse acceder au donnés du json sans devoir relire le json

Cepadant dans la classe projet par ex l'accès au donnés ressemble a ça : ``self.main_app.main_app.param_manager.get_data("projects", "editor")``
Ce qui peut surement etre réduis 