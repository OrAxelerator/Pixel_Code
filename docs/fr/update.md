# Système de mise à jour

## Pour les utilisateurs

Au lancement, Pixel_Code regarde sur GitHub si une nouvelle version existe. Si oui, il demande :

```
Nouvelle version disponible v0.6.0 -> v0.6.1, installer ? [Y/n]
```

* **Y / ENTRÉE / ESPACE** : Pixel_Code se ferme, installe la nouvelle version (la sortie de pip s'affiche dans le terminal), puis vous demande de le relancer avec `pixel-code`.
* **n'importe quelle autre touche** : Pixel_Code démarre normalement.

Vos projets et paramètres ne sont **jamais touchés** par une mise à jour : ils sont enregistrés en dehors du code (voir [configuration](/docs/fr/config.md)).

> [!NOTE]
>
> * **Pas de connexion ?** Pixel_Code attend GitHub 3 secondes au maximum, puis démarre normalement sans rien demander.
> * Pour désactiver la vérification : mettez ``check_update_at_launch`` à ``false`` dans les paramètres (touche ``p``) ou dans ``parametres.json``.
> * ``allow_prerelease`` (dans ``parametres.json``) choisit si les pre-releases comptent comme des mises à jour. Pour l'instant toutes les versions de Pixel_Code sont des pre-releases, donc laissez-le à ``true``.

### Installé avec `pip install -e .` ?

Dans ce cas le code vient de votre clone git, donc Pixel_Code n'installe rien : il vous dit de faire ``git pull`` dans le dossier du clone.

### Mettre à jour à la main

Si la mise à jour automatique échoue, réinstallez depuis un nouveau clone :

```bash
git clone https://github.com/OrAxelerator/Pixel_Code.git
cd Pixel_Code
pipx install --force .   # ou : pip install --upgrade .
```

> [!IMPORTANT]
>
> Les versions **0.5.2 et plus anciennes** utilisent l'ancien système de mise à jour, qui ne marche pas avec pipx. Réinstallez-les à la main **une fois** (commandes au-dessus). Ensuite les mises à jour sont automatiques.

---

## Pour les développeurs

Code : ``pixel_code/utils/update.py``, appelé depuis ``App.run()`` (``app.py``) et ``__main__.py``.

1. ``App.check_update()`` demande à l'API GitHub (``/repos/OrAxelerator/Pixel_Code/releases``, timeout de 3s) la release la plus récente. Toute erreur (pas de connexion, rate limit, 404...) renvoie ``None`` et Pixel_Code démarre simplement.
2. Le tag de la release (``vX.Y.Z``) est comparé à la version installée (``importlib.metadata.version("pixel-code")``, c'est-à-dire ``version`` dans ``pyproject.toml``).
3. Si l'utilisateur accepte, le tag est enregistré dans ``App.update_tag`` et l'``App`` s'arrête **avant** de lancer l'interface.
4. Une fois curses fermé, ``__main__.py`` lance :
    ```bash
    <python de Pixel_Code> -m pip install --upgrade https://github.com/OrAxelerator/Pixel_Code/archive/refs/tags/vX.Y.Z.zip
    ```
    Utiliser le python qui fait tourner Pixel_Code (``sys.executable``) permet que ça marche pareil avec pipx et avec pip.

### Publier une nouvelle version

1. Changez ``version`` dans ``pyproject.toml`` (ex : ``0.6.1``).
2. Mergez dans ``main``, puis créez une release GitHub avec le tag **``v`` + la même version** (``v0.6.1``).

> [!WARNING]
>
> Si le tag et ``pyproject.toml`` ne correspondent pas, les utilisateurs ont la demande de mise à jour à chaque lancement (c'est arrivé avec la v0.5.0).

### Debug

En mode ``--debug``, Pixel_Code ne contacte **pas** GitHub (trop de requêtes et on se fait bloquer un moment) et affiche une fausse mise à jour ``v999.9.9`` qui ne fait rien si on l'accepte. Ajoutez ``--wifi`` pour vraiment vérifier GitHub en mode debug :

```bash
python3 pixel_code/__main__.py --debug --wifi
```
