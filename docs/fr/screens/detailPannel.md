### Detail pannel screens :

En réalité il n'est utilisé que lorsque le paramètre ``"display_projects" = "side" ``  car quand ce paramètre vaut ``"bottom"`` (supprimé depuis v0.4.0) les données du projet sont affichées en dessous de son nom sur la fenêtre main.


Preview : 
![](/docs/assets/detailPannel.png)

La fenêtre est composée de 5 infos :

* Le nom du projet centré et en **gras**
* La description du projet
* Les langages utilisés
* Le chemin du projet sur la machine
* Le lien du dépot github

Le code permettant d'afficher cette fenêtre se trouve dans la fonction ``display_project_full`` de la classe ``Project`` et utilise self.detail_panel.win pour accéder à la fenêtre


### L'affichage de la description :
La description du projet peut être plus longue que la largeur de la fenêtre, malheureusement curses ne s'occupe pas de faire des retours à la ligne et renvoie l'erreur : ``addwstr()`` ou affichage incorrect.

Le texte ``description_str`` est découpé en plusieurs lignes dans ``description_cut``, on peut calculer le nombre de lignes nécéssaires avec : 
```python
overflow:int =math.ceil(len(description_str) / w - 3)
# -3 parceque 2ch pour la bordure et 1 pour la "margin-left"
# math.ceil pour arrondir valeur supérieur 
```
Puis on fait : 
```python
max_width = w - 3 #2 ch border + 1 space left
    for i in range(0, len(description_str), max_width):
    description_cut.append(description_str[i:i + max_width])
```

> il faut rajouter + overflow en ``y`` aux autres données après la description pour toujours avoir un écart de 2 caractères entre la description et le reste des donnés en dessous
