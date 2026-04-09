![](preview.png)

### Qu'est-ce que Pixel_Code ?
Pixel_Code est un outil en Python permettant de facilement enregistrer vos projets en cours, et de les ouvrir facilement depuis le terminal avec une petite interface.


--- 

# Comment marche le lancement de l'app
tout ce fait dans __main__.py (/pixel_code/__main__.py)

La fonction ``main()``appelle la classe Main() qui lance le programme

> [!NOTE]
>
> SI la classe Main() n'est pas appelez le programme fait rien

Pour lancer le programme tapez :
```python
python3 pixel_code/__main__.py
````

--- 

# Update de v0.3.4

Nouvelle fonction ``exec_sh()`` qui permet de lancer .sh se trouvant dans le dossier ``pixel_code/script/sh``
il suffit juste de donner le nom du fichier en string en argument de la fonction **(ne pas mettre .sh)**

---

> [!NOTE]
>
> Raccourcis clavier :
> 
> * **ESPACE** : afficher / désactiver la vue complète sur un projet
> * **q** : arrêter l’exécution du fichier
> * **↑/↓** : navigation
> * **p** : ouvrir les paramètres
> * **r** : recharger l’affichage (marche seulement dans main)
