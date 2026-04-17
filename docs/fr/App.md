# App.py

## Initialisation

À l'init, la classe `App` s'occupe de créer toutes les classes :
- `Logo`
- `ParamScreen`
- `MainScreen`
- `DetailPanel`
- `ParamManager`

Avec comme argument `self`, pour que, depuis n'importe quelle classe, on puisse accéder aux autres.

Puis, la fenêtre affichée (seulement les fenêtres qui prennent 100 % de l'espace, donc `main` ou `paramètre`) est enregistrée dans `self.current`, et la boucle principale se lance avec `self.run()`.

---

## self.run()

S'occupe :
- D'afficher le logo.
- D'afficher la fenêtre `main` à l'init.
- Puis de lancer une boucle `while True`.

Cette boucle détecte :
- quelle touche est pressée.
- quoi faire en fonction de l'écran.

---

## Gestion des touches

>[!WARNING]
>
>`get_key()` ne renvoie pas toutes les touches du clavier.

Pour rajouter une fonction à l'appui d'une touche, il faut rajouter cette touche dans :
`pixel_code/script/keybord.py` dans la condition os == "nt" (windows), os == "Darwin" ("macos") et Linux. 
Pour que cela marche pour tout les OS.