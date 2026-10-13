# Installation - advanced

Pixel_Code needs **Python 3.10 or newer** and **git**.

<details>
<summary><strong>1. Ubuntu/Linux</strong></summary><br>

* Check if pipx is installed: ``pipx --version``. If not:

    ```bash
    sudo apt install pipx
    pipx ensurepath
    ```
    Then close and re-open the terminal.

* Clone the repo and install the TUI:

    ```bash
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pipx install .
    ```
</details>

<details>
<summary><strong>2. MacOS</strong></summary><br>

* With pipx (recommended):

    ```bash
    brew install pipx
    pipx ensurepath
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pipx install .
    ```

* Or with pip:

    ```bash
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pip install .
    ```
</details>

<details>
<summary><strong>3. Windows</strong></summary><br>

> [!NOTE]
>
> Windows installation is not 100% documented for every case yet.

* Download the project and install the tool:

    ```cmd
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    py -m pip install .
    ```
    The most common errors are:
    - pip isn't installed (see below)
    - you typed ``python`` but your computer uses ``py`` (or the opposite)

* If you get this error:
    ```
    WARNING: The script xxx.exe is installed in 'C:\Users\XXX\AppData\Local\Microsoft\WindowsApps' which is not on PATH
    ```
    You surely use python from the Microsoft Store (bad).
    Download python from the official website: [python.org](https://www.python.org/)

    Then install pip with python:
    * ``py -m ensurepip --upgrade``
    * ``py -m pip install --upgrade pip``

* If you get this error:
    ```
    WARNING: The script pixel-code.exe is installed in 'C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\Scripts' which is not on PATH.
    ```
    <details>
    <summary>Do:</summary>

    1. Win + R
    2. In the popup write: ``sysdm.cpl``
    3. Advanced tab
    4. Environment Variables
    5. In User variables → select ``Path``
    6. Edit
    7. New
    8. Paste this path (change with your username): ``C:\Users\USERNAME\AppData\Local\Python\pythoncore-3.14-64\Scripts``
    9. OK -> OK -> OK
    10. Close and re-open the terminal.

    Issue solved (normally).
    </details>

</details>

---

### Once the installation is done

> [!NOTE]
>
> Launch the app by typing the command: **pixel-code**

* If the app starts **without crashing** but some characters are badly displayed: see [config](/docs/eng/config.md).
* Updates are proposed automatically at launch: see [update](/docs/eng/update.md).
* Optional: from the clone, ``python3 first_use.py`` adds Pixel_Code itself as an example project (only works if Pixel_Code is installed with pip, not pipx). You can also simply add a project with the ``a`` key.

### For developers

```bash
pip install -e .
```
With an editable install, the code used is your clone: update it with ``git pull`` (Pixel_Code won't install updates by itself).

### Uninstall

```bash
pipx uninstall pixel-code   # or : pip uninstall pixel-code
```
Your projects and settings stay on your computer (see [config](/docs/eng/config.md) for where they are).
