### Detail pannel screens :

In fact this screen is only used when the setting ``"display_project" = "side"``, because when this setting was ``"bottom"`` (deleted since v0.4.0) the data of the project was displayed below its name in the main window.

Preview : 
![](/docs/assets/detailPannel.png)

The window is composed of 5 pieces of information:

* Name of the project center and in **bold**
* Description of the project
* Languages used
* Local path of the project 
* Link of the github REPO

The code that displays this window is in the function ``display_project_full()`` of the class ``Project`` and uses ``self.detail_panel.win`` to access the window.

### Display of the description :
The description can be longer than the width of the window, unfortunately curses doesn't go to the next line by itself and returns the error ``addwstr()`` or displays badly.

The text ``description_str`` is cut in several lines in ``description_cut``, the number of lines needed is calculated with:

```python
overflow:int =math.ceil(len(description_str) / w - 3)
# -3 bcs 2ch for the border and 1 for "margin-left"
# math.ceil round to the top value 
```
Then:
```python
max_width = w - 3 #2 ch border + 1 space left
    for i in range(0, len(description_str), max_width):
    description_cut.append(description_str[i:i + max_width])
```

> + overflow must be added to ``y`` of all the other data after the description, to always have a gap of 2 characters between the description and the rest of the data.