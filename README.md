# 🇬🇧/🇺🇸 - English Version

[See the 🇫🇷 README](/docs/fr/README_FR.md)

![](/docs/assets/preview.png)

## What is Pixel_Code?
Pixel_Code is a Python tool that makes it easier to open projects in VS Code and provides better organization and visualization of ongoing and completed projects. It works from the terminal with a simple interface.


> [!NOTE]
>
> Pixel_Code is a TUI app (Terminal User Interface)

#### How does it work?

see **documentation** : [here](/docs/eng/index.md)


### Installation on:
<details>
<summary><strong>1. Ubuntu/Linux</strong></summary>

* If **pipx isn't installed:**
    
    ```bash
    sudo apt install pipx
    pipx ensurepath
    ```
* Clone the repo and install the TUI:

    ```bash
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pipx install .
    ```
</details>

---
<details>
<summary><strong>2. MacOS</strong></summary>


* Clone the repo and install the TUI:

    ```cmd
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pip install -e .
    ```
    
</details>

---

<details>
<summary><strong>3. Windows</strong></summary>


* Download the project and install the tool:
    ```cmd
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd ./Pixel_Code
    py -m pip install -e .
    ```
    (or python)
    * If you get an error:
    **See advanced Windows installation [by clicking here](/docs/eng/install.md)**
        
    </details>

---


> Launch the app by typing the command: **pixel-code**


> [!IMPORTANT]
>
> For the icons to work, you need to set the **"0xProto Nerd Font"** in your terminal, and if you want to run the code in VS Code, you also need to set **Terminal › Integrated: Font Family** = `"0xProto Nerd Font"`.
>
> Link to install the font: https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/0xProto.zip

> [!NOTE]
>
> Keyboard shortcuts:
> 
> * **SPACE**: show/hide full view on a project.
> * **q**: stop the execution of the tui.
> * **↑/↓**: navigation.
> * **p**: open settings.
> * **r**: reload the display (only works in main branch).
> * **e**: edit project data from Pixel_Code (not yet functional).
> * **a**: add a project.
> * **d**: delete a project.
> * **g**: perform github action (not available).

---

### Built with:
* Python
* Python library: curses for display
* Python library: requests for the update system
* pyproject.toml
* .json for saved data

### License:
The project is under MIT license - see the [LICENSE](/LICENSE.md) file for more information.

### Contributing info

[here](/CONTRIBUTING.md)