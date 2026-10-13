# App.py

## Initialisation

``__main__.py`` crée la classe `App` dans ``curses.wrapper()``. À l'init, `App` crée le ``ParamManager``, vérifie les mises à jour, puis crée tous les écrans :
- `Logo`
- `ParamScreen`
- `MainScreen`
- `DetailPanel`

Avec comme argument `self`, pour que, depuis n'importe quelle classe, on puisse accéder aux autres.

La fenêtre affichée (seulement les fenêtres qui prennent 100 % de l'espace, donc ``"main"`` ou ``"param"``) est enregistrée dans `self.current`, et la boucle principale se lance avec `self.run()`.

---

## self.run()

S'occupe :
- De vérifier les mises à jour (voir [mise à jour](/docs/fr/update.md)). Si l'utilisateur accepte, ``run()`` s'arrête là et la mise à jour est installée par ``__main__.py``.
- D'afficher le logo.
- D'afficher la fenêtre `main` au démarrage.
- Puis de lancer une boucle `while True`.

Cette boucle détecte :
- Quelle touche est pressée.
- Quoi faire en fonction de l'écran (``self.current``).

---

## Gestion des touches

> [!WARNING]
>
> `get_key()` ne renvoie pas toutes les touches du clavier.

Pour rajouter une touche, il faut la rajouter dans ``pixel_code/script/keybord.py``, dans la condition ``os.name == "nt"`` (Windows) **ET** dans le ``else`` (macOS / Linux), pour que ça marche sur tous les OS. Puis rajoutez ce que fait la touche dans la boucle de ``App.run()``.
