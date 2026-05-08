# Changelog

Toutes les modifications importantes de ce projet sont documentées ici.

Format : Y/M/D

---

## [0.1.1] - 2025-12-31

### Rajouté
- Ajout du système de navigation clavier
- Ajout du support multi-langue
- Ajout vue "bottom"
- Ajout page Parametre (lang, nerdfont, "tuto")
- muti os (que des print())

---

## [0.1.2] - 2026-01-16

### Changé
- Nouvelle architecture avec ``/script`` et ``/data`` et project.json avec toute les donnés de tout les jsno dedans.

---

## [0.2.0]

### Rajouté 
- raccourci clavier "a" pour rajouter projet

---

## [0.3.0] - 2026-01-26

### Rajouté
-  Git feature, lettre "g" pour clone/pull projet

---

## [0.4.0] - 2026-05-06


### Changé
- Interface gérer avec module py ``curses`` (bcp mieux que print())
- Meilleur support de multi-langage grace à paramManager
- Gestion des projets : toutes les info son dans .pixelcode.json a la racine du projet en question
- Mode débug (--debug)
- nouvelle interface paramètre
- architecture global plus propre (/screens /utils)

### Rajouté :
- Documentation fr/eng
- ParamManger [voir doc](/docs/fr/param_manager.md)

### Suprimé
- Affichage mode "bottom" (├─ description : ...)


## [0.5.0] - 2026-05-08

### Rajouté :
- Utilisation de platformdirs
- message d'erreur quand .pixelcode.json pas trouvé sur chemin d'un projet