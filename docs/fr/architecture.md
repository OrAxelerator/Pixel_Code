# Architecture général du projet


### Les paramètres :

```
{
    "app": {
        "language": "fr", ("fr", "en")
        "use_nerd_font": true, # Icone
        "version": "v0.4.0",
        "check_update_at_launch": true,
        "allow_prerelease": true
    },
    "ui": {
        "theme": "default", # Fait rien pour l'instant
        "logo": "left" # positionnement du logo ("center", "left")
    },
    "projects": {
        "sort_by_last_opened": true,
        "sort_by_name": false,
        "editor": "code" # ("code", "vim")
    }
}
```

### Projects.json : 

```
{
    "projects": [
        {
            "id": "72b38123", #
            "path": "/Users/Axel/Pixel_Code",
            "status": "todo" # ("todo", ...)
        }, ...
    ]
}

```


## Fonctionnement des écrans (`screens`)

Les écrans dans Pixel Code sont des interfaces utilisateur construites avec la bibliothèque `curses`. Chaque écran est encapsulé dans une classe Python et est conçu pour gérer une partie spécifique de l'application. Deplus chaque écran est initialisé avec une référence à l'application principale (`main_app`) depuis ``app.py`` pour accéder aux ressources partagées comme `stdscr` (l'écran principal de `curses`) et les gestionnaires de données. Les écrans utilisent des fenêtres (`newwin`) pour afficher leurs contenus et interagir avec l'utilisateur. L'écran active (main/parametre) est enregistré dans la variable self.current dans la class App et peut prendre comme valeur: "main" et "parametre"

Voici une liste des écrans  de ``/screens``:

### 1. `Logo`
- **Fichier** : `screens/logo_screen.py`
- **Description** : Affiche le logo ascii Pixel_Code en haut de l'écran.
- **Caractéristiques** :
  - Charge ``data/logo.txt`` contenant le logo.
  - Centre ou aligne le logo selon les paramètres utilisateur.
  - Peut etre affiché soit a gauche ("left") ou milieu ("center") selon les réglage de l'utilisateur 

### 2. `MainScreen`
- **Fichier** : `screens/main_screen.py`
- **Description** : Point d'entrée principal pour gérer les interactions utilisateur.
- **Caractéristiques** :
  - Coordonne les différents écrans.

### 3. `DetailPanel` 
- **Fichier** : `screens/detail_panel_screen.py`
- **Description** : Affiche un panneau avec les détails du projet selectionné dans une fenêtre dédiée sur le coté gauche de la fenetre main
- **Caractéristiques** :
  - Crée une fenêtre avec des bordures.

> [voir plus](/docs/fr/screens/detailPannel.md)

### 4. `ParamScreen`
- **Fichier** : `screens/param_screen.py`
- **Description** : Permet de configurer les paramètres de l'application.
- **Caractéristiques** :
  - Affiche une liste de paramètres modifiables.
  - S'affiche a la place de MainScreen
  - Gère la navigation et la sélection des options.
  
### 5. `Input`
- **Fichier** : `screens/input_curses.py`
- **Description** : Gère les entrées utilisateur dans une zone de texte.
- **Caractéristiques** :
  - Affiche une boîte de saisie avec un titre.
  - Permet à l'utilisateur de taper du texte et de le récupérer.

Représenttion des fenètres dans le terminal : 
<img src="/docs/assets/interface.png" style='with:300px; height:220px; margin:0 auto;'>




