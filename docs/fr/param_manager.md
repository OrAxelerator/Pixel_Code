# ParamManager


ParamManger est une classe (``/pixel_code/script/data/param_manager.py``) créée dans app.py dans la variable ``self.param_manager``. Cette classe charge les paramètres utilisateur depuis le fichier ``PARAMETRES_JSON`` défini dans ``pixel_code/paths.py`` avec self.load_param() et enregistre les données avec self.save_param(). Le fichier est placé dans le dossier de configuration utilisateur via ``platformdirs``, ce qui permet de garder les paramètres pendant les mises à jour. Pour obtenir une donnée il suffit d'accéder à la classe et utiliser get_data(key_section, key).

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

L'idée de cette classe est que depuis n'importe où, tant qu'il y a un accès à la classe main on puisse acceder aux données du json sans devoir relire le json.

Cepandant dans la classe project par ex l'accès aux données ressemble à ça : ``self.main_app.main_app.param_manager.get_data("projects", "editor")``
Ce qui peut surement être réduit. 
