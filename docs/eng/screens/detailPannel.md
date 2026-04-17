### Detail pannel screens :

This screen is only used when ``"display_projects" = "side" `` 

Preview : 
![](/docs/assets/detailPannel.png)

Screen is composed by 5 information :

* Name of the project center and in **bold**
* Description of the project
* Languages used
* Local path of the project 
* Link of the github REPO

The code to display this windows is in ``display_project_full()`` in ``Project`` and use self.detail_panel.win to accesse to the screen

### Display of the description :
Description can be longer than the width of detailPannel, unfortunately curses doesn't do backslash and return error : ``addwstr()`` or bug display

The text in  ``description_str`` is cut in several line  in ``description_cut``, we can calculate where to add '\n' .

```python
overflow:int =math.ceil(len(description_str) / w - 3)
# -3 bcs 2ch for the border and 1 for "margin-left"
# math.ceil round to the top value 
```
After that :
```python
max_width = w - 3 #2 ch border + 1 space left
    for i in range(0, len(description_str), max_width):
    description_cut.append(description_str[i:i + max_width])
```

> Must add + overflow in ``y`` to all other data after the description for always have the same gap of 2charactère between the description and the rst of the data.