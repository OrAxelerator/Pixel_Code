# Changelog

Toutes les modifications importantes de ce projet sont documentées ici.

Format : A-M-J

---

## [0.6.0] - pas encore publiée

### Changé
- Nouveau système de mise à jour, simple et qui marche avec pipx et pip : au lancement Pixel_Code propose la nouvelle version, puis l'installe avec pip directement depuis la release GitHub ([voir doc](/docs/fr/update.md)).
    - S'il n'y a pas de connexion, Pixel_Code attend 3 secondes maximum puis démarre normalement.
    - Les paramètres ``check_update_at_launch`` et ``allow_prerelease`` sont utilisés.
    - Avec ``pip install -e .``, Pixel_Code vous dit d'utiliser ``git pull`` à la place.
- La version dans les paramètres est toujours la version installée.
- Python 3.10+ est nécessaire (le code ne marchait déjà pas avec les versions plus anciennes).
- Tous les messages de l'interface et des sous-commandes sont en anglais et en français.
- La touche ``g`` affiche "pas encore disponible" au lieu de lancer des commandes git pas finies.
- Documentation terminée et identique en anglais et en français.

### Supprimé
- ``update.py`` et le dossier ``update/`` (ancien système de mise à jour, il supprimait et remplaçait les fichiers du clone).

> [!IMPORTANT]
>
> Depuis la v0.5.2 ou plus ancienne : réinstallez une fois à la main (``pipx install --force .`` dans un nouveau clone).

---

## [0.5.2] - 2026-07-31

### Changé
- Correction : la version dans ``pyproject.toml`` n'était pas mise à jour.

---

## [0.5.1] - 2026-07-31

### Rajouté
- Sous-commande ``--wifi`` : vérifie vraiment la dernière version sur GitHub, même en mode debug.

### Changé
- Correction de la récupération de la dernière version sur GitHub, plus de sécurité quand les données de GitHub sont mauvaises.

---

## [0.5.0] - 2026-07-18

### Rajouté
- 4 nouvelles sous-commandes :
    - ``--clean-projects`` : supprime les projets invalides si le chemin n'existe pas/plus
    - ``--clean-projects-hard`` : comme ``--clean-projects`` mais supprime aussi si ``.pixelcode.json`` est introuvable
    - ``--reset-config`` : réinitialise ``parametres.json``
    - ``--clear-log`` : efface le contenu de ``debug.log``

    Utilisez ``pixel-code -h`` pour afficher l'aide
- Icônes sur l'écran des paramètres.
- Message d'avertissement dans ``debug.log`` quand ``.pixelcode.json`` n'est pas trouvé dans le chemin d'un projet.
- Éditer un projet avec "e".
- Système de mise à jour.
- Chercher un projet (``/``), filtrer par statut (``f``), marquer un projet comme fini (``m``).

### Changé
- Pixel_Code utilise ``platformdirs`` pour placer les fichiers utilisateur dans les dossiers standards de l'OS :
    - ``parametres.json`` dans le dossier de configuration utilisateur.
    - ``projects.json`` dans le dossier de données utilisateur.
    - ``debug.log`` dans le dossier de données utilisateur.
- Plus de messages de debug/avertissement dans ``debug.log``.
- ``logging.basicConfig`` est maintenant dans App.
- La façon dont le script récupère les arguments dans ``__main__.py``.
- Les paramètres par défaut prennent la version depuis ``pyproject.toml`` (la version installée sur votre machine).
- ``first_use.py`` marche avec les nouvelles données platformdirs.
- Correction : la version était 0.4.1 et pas 0.5.0.

---

## [0.4.0] - 2026-04-16

### Changé
- Interface gérée avec le module python ``curses`` (beaucoup mieux que print()).
- Meilleur support du multi-langue grâce à **ParamManager**.
- Gestion des projets : toutes les infos sont dans ``.pixelcode.json`` à la racine du projet en question.
- Mode debug (``--debug``).
- Nouvelle interface des paramètres.
- Architecture globale plus propre (``/screens``, ``/utils``).

### Rajouté
- Documentation fr/eng.
- ParamManager [voir doc](/docs/fr/param_manager.md).

### Supprimé
- Affichage mode "bottom" (├─ description : ...).
- Fonctionnalités GitHub.

---

## [0.3.0] - 2026-01-26

### Rajouté
- Fonctionnalité git, touche "g" pour clone/pull un projet.

---

## [0.2.0] - 2026-01-18

### Rajouté
- Raccourci clavier "a" pour rajouter un projet.

---

## [0.1.2] - 2026-01-16

### Changé
- Nouvelle architecture avec ``/script`` et ``/data``, et ``project.json`` avec toutes les données dedans.

---

## [0.1.1] - 2025-12-31

### Rajouté
- Système de navigation au clavier.
- Support multi-langue.
- Vue "bottom".
- Page paramètres (langue, nerdfont, "tuto").
- Multi OS (que des print()).
