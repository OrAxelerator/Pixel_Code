# ParamManager

ParamManager est une classe (``/pixel_code/script/data/param_manager.py``) créée dans app.py dans la variable ``self.param_manager``. Cette classe charge les paramètres utilisateur depuis le fichier ``PARAMETRES_JSON`` défini dans ``pixel_code/paths.py`` avec ``self.load_param()`` et enregistre les données avec ``self.save_param()``. Le fichier est placé dans le dossier de configuration utilisateur via ``platformdirs``, ce qui permet de garder les paramètres pendant les mises à jour. Pour obtenir une donnée il suffit d'accéder à la classe et d'utiliser ``get_data(key_section, key)``.

Exemple :
```json
{
    "app": {
        "language": "en",
        ...
    }
}
```

> self.get_data("app", "language") = "en"

Au chargement, les valeurs du fichier sont fusionnées par-dessus ``DEFAULT_PARAMETRES`` (``paths.py``) : une clé absente du fichier prend sa valeur par défaut. Donc pour rajouter un paramètre, ajoutez-le dans ``DEFAULT_PARAMETRES`` (et dans ``settings_config`` de ``ParamScreen`` pour pouvoir le modifier depuis l'écran des paramètres). ``app.version`` est toujours remplacé par la version installée.

L'idée de cette classe est que depuis n'importe où, tant qu'il y a un accès à la classe main, on puisse accéder aux données du json sans devoir relire le json.

Cependant dans la classe ``Project`` par exemple, l'accès aux données ressemble à ça : ``self.main_app.main_app.param_manager.get_data("projects", "editor")``
Ce qui peut sûrement être réduit.
