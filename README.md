# 🇬🇧/🇺🇸 - English Version

[See the 🇫🇷 README](/docs/fr/README_FR.md)

![](/docs/assets/preview.png)

## What is Pixel_Code?
Pixel_Code is a Python tool that makes it easier to open projects in VS Code and provides better organization and visualization of ongoing and completed projects. It works from the terminal with a simple interface.


> [!NOTE]
>
> Pixel_Code is a TUI app (Terminal User Interface)

#### How does it work?

See the **documentation**: [here](/docs/eng/index.md)


### Installation on:

Pixel_Code needs **Python 3.10+** and **git**.

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


* Clone the repo and install the TUI (or ``pip install .`` without pipx):

    ```bash
    brew install pipx
    pipx ensurepath
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pipx install .
    ```

</details>

---

<details>
<summary><strong>3. Windows</strong></summary>


* Download the project and install the tool:
    ```cmd
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    py -m pip install .
    ```
    (or python)
    * If you get an error:
    **See advanced Windows installation [by clicking here](/docs/eng/install.md)**

</details>

---
> [!IMPORTANT]
>
> On first launch, Pixel_Code automatically creates its user files with ``platformdirs``.
> Old ``pixel_code/data/projects.json`` and ``pixel_code/data/parametres.json`` files are migrated if no user file already exists.

> Launch the app by typing the command: **pixel-code**

> [!NOTE]
>
> **Updates**: at launch, Pixel_Code proposes to install the new version if there is one (and starts normally without connection). Your projects and settings are kept. See [update](/docs/eng/update.md).
>
> Coming from **v0.5.2 or older**? Reinstall once by hand with the commands above (``pipx install --force .``).

> [!IMPORTANT]
>
> For the icons to work, you need to set the **"0xProto Nerd Font"** in your terminal, and if you want to run the code in VS Code, you also need to set **Terminal › Integrated: Font Family** = `"0xProto Nerd Font"`.
>
> Link to install the font: https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/0xProto.zip

> [!NOTE]
>
> Keyboard shortcuts (all of them [here](/docs/eng/key_bind.md)):
>
> * **↑/↓**: navigation.
> * **ENTER**: open the project with your editor.
> * **SPACE**: show/hide the details of a project.
> * **/**: search a project by name, **c**: clear the search.
> * **f**: filter projects by status, **m**: mark a project done / to finish.
> * **a**: add a project, **e**: edit a project, **d**: delete a project.
> * **p**: open settings.
> * **q**: quit.

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
