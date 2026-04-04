### Detail pannel screens :

En réalité il est utilisé que quand le paramètre ``"display_projects" = "side" ``  car quand ce parametre vaut ``"bottom"`` les donnés du project sont affiché en dessous de son nom sur la fenetre main.


Preview : 
![](/docs/assets/detailPannel.png)

La fenetre est composé de 5 info :

* Le nom du projet centré et en **gras**
* La description du projet
* Les langages utilisé
* Le chemin du projet sur la machine
* Le lien du dépo github

Le code permettant d'afficher cette fenetre est dans la fonction ``display_project_full`` de la classe Project et utilise self.detail_panel.win pour acceder a la fenetre


### L'affichage de la description :
La description du projet peut etre plus longe que la largeur de la fenetre, malheuresement curses ne s'occupe pas de faire des retour a la ligne et renvoi l'erreur : ``addwstr()`` ou affichage incorectte.

Le texte ``description_str`` est découpé en plusieur ligne dans ``description_cut``, on peut calculer le nombre de ligne nécéssaire avec : 
```python
overflow:int =math.ceil(len(description_str) / w - 3)
# -3 parceque 2ch pour la bordure et 1 pour la "margin-left"
# math.ceil pour arrondir valeur supérieur 
```
Puis ont fait : 
```python
max_width = w - 3 #2 ch border + 1space left
    for i in range(0, len(description_str), max_width):
    description_cut.append(description_str[i:i + max_width])
```

> il faut rajouter + overflow en y au autre données après description pour toujours avoir un écart de 2ch entre description et le reste des donnés en dessous

parler de sys ytaducton et param manager