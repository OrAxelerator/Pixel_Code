# Architecture générale du projet

```
pixel_code/
├── __main__.py      # point d'entrée (pixel-code), sous-commandes, lance la mise à jour une fois curses fermé
├── app.py           # classe App : boucle principale, touches, vérification des mises à jour
├── paths.py         # où sont les fichiers utilisateur (platformdirs), paramètres par défaut
├── data/logo.txt    # logo ascii
├── screens/         # fenêtres curses (voir en dessous)
├── script/          # clavier, projets (.pixelcode.json / projects.json), paramètres (ParamManager)
└── utils/           # translate(), système de mise à jour
```

Plus de détails : [App](/docs/fr/App.md), [ParamManager](/docs/fr/param_manager.md), [mise à jour](/docs/fr/update.md).

## Les données

Les fichiers utilisateur ne sont pas stockés dans ``pixel_code/data``. Pixel_Code utilise ``platformdirs`` pour les placer dans les dossiers standards de l'OS (voir [configuration](/docs/fr/config.md)) :

- ``parametres.json`` dans le dossier de configuration utilisateur.
- ``projects.json`` dans le dossier de données utilisateur.
- ``debug.log`` dans le dossier de données utilisateur.

Au lancement, Pixel_Code crée ces fichiers s'ils n'existent pas (``ensure_user_files()`` dans ``paths.py``) et migre les anciens JSON de ``pixel_code/data`` seulement si la nouvelle destination n'existe pas déjà.

### parametres.json

```json
{
    "schema_version": 1,
    "app": {
        "language": "en",                // "en", "fr"
        "use_nerd_font": false,          // icônes
        "version": "0.6.0",              // toujours la version installée (pyproject.toml)
        "check_update_at_launch": true,
        "allow_prerelease": true         // les pre-releases comptent comme mises à jour
    },
    "ui": {
        "theme": "default",              // ne fait rien pour l'instant
        "logo": "center",                // "center", "left"
        "display_project": "side"        // détails d'un projet dans le panneau sur le côté
    },
    "projects": {
        "sort_by_last_opened": false,    // pas utilisé pour l'instant
        "sort_by_name": true,            // pas utilisé pour l'instant
        "editor": "code",                // "code" (VS Code), "vim", "cmd" (terminal)
        "repo": "github"                 // "github", "null" : lien par défaut quand on ajoute un projet
    }
}
```

Les clés manquantes prennent leur valeur par défaut (``DEFAULT_PARAMETRES`` dans ``paths.py``).

### projects.json

Seulement la liste des projets : où ils sont et leur statut.

```json
{
    "schema_version": 1,
    "projects": [
        {
            "id": "72b38123",                 // uuid4[:8]
            "path": "/Users/Axel/Pixel_Code",
            "status": "todo"                  // "todo", "done"
        }
    ]
}
```

### .pixelcode.json

Les données d'un projet, enregistrées **à la racine du projet** (donc elles suivent le projet s'il est copié/cloné).

```json
{
    "name": "Pixel_Code",
    "description": "...",
    "languages": ["python", "json"],
    "path": "/Users/Axel/Pixel_Code",
    "repo": "https://github.com/OrAxelerator/Pixel_Code.git"
}
```

Un projet de ``projects.json`` sans ``.pixelcode.json`` est ignoré au lancement (un warning est écrit dans ``debug.log``), utilisez ``pixel-code --clean-projects-hard`` pour l'enlever.

## Fonctionnement des écrans (`screens`)

Les écrans dans Pixel_Code sont des interfaces utilisateur construites avec la bibliothèque `curses`. Chaque écran est une classe Python conçue pour gérer une partie spécifique de l'application. Chaque écran est initialisé avec une référence à l'application principale (`main_app`) depuis ``app.py`` pour accéder aux ressources partagées comme `stdscr` (la fenêtre du terminal pour curses) et le gestionnaire de paramètres ``ParamManager``. Les écrans utilisent des fenêtres curses (`newwin`) pour s'afficher. L'écran actif est enregistré dans la variable `self.current` de la classe App et peut prendre comme valeur ``"main"`` / ``"param"``.

Voici la liste des écrans de ``/screens`` :

### 1. `Logo`
- **Fichier** : `screens/logo_screen.py`
- **Description** : Affiche le logo ascii en haut de l'écran.
- **Caractéristiques** :
  - Charge ``data/logo.txt``.
  - Centre ou aligne à gauche le logo selon le paramètre utilisateur.

### 2. `MainScreen`
- **Fichier** : `screens/main_screen.py`
- **Description** : Affiche la liste des projets et les gère (recherche, filtre, ajout, édition, suppression, statut). La classe ``Project`` (une par projet, l'ouvre avec l'éditeur) est dans le même fichier.

### 3. `DetailPanel`
- **Fichier** : `screens/detail_panel_screen.py`
- **Description** : Affiche un panneau avec les détails du projet sélectionné dans une fenêtre à droite.
- **Caractéristiques** :
  - Crée une fenêtre avec des bordures.

> [voir plus](/docs/fr/screens/detailPannel.md)

### 4. `ParamScreen`
- **Fichier** : `screens/param_screen.py`
- **Description** : Permet de configurer les paramètres de l'application.
- **Caractéristiques** :
  - Affiche les paramètres modifiables (liste ``settings_config``, types ``cycle``, ``toggle`` et ``readonly``).
  - S'affiche à la place de MainScreen.

### 5. `Input`
- **Fichier** : `screens/input_curses.py`
- **Description** : Gère les entrées utilisateur dans une zone de texte.
- **Caractéristiques** :
  - La zone de saisie peut avoir un titre et du texte pré-rempli.

Représentation des fenêtres dans le terminal :
<img src="/docs/assets/interface.png" style='width:300px; height:220px; margin:0 auto;'>

## Traductions

Chaque texte affiché à l'utilisateur doit exister en anglais et en français, avec ``translate()`` (``utils/translate.py``) :

```python
translate({"en": "Project saved.", "fr": "Projet enregistré."}, self.main_app.param_manager.get_data("app", "language"))
```
