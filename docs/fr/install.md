# Installation - avancée

Pixel_Code a besoin de **Python 3.10 ou plus récent** et de **git**.

<details>
<summary><strong>1. Ubuntu/Linux</strong></summary><br>

* Regardez si pipx est installé : ``pipx --version``. Sinon :

    ```bash
    sudo apt install pipx
    pipx ensurepath
    ```
    Puis fermez et ré-ouvrez le terminal.

* Clonez le dépôt et installez la TUI :

    ```bash
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pipx install .
    ```
</details>

<details>
<summary><strong>2. MacOS</strong></summary><br>

* Avec pipx (recommandé) :

    ```bash
    brew install pipx
    pipx ensurepath
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pipx install .
    ```

* Ou avec pip :

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
> L'installation sur Windows n'est pas encore documentée à 100% dans tous les cas.

* Téléchargez le projet et installez l'outil :

    ```cmd
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    py -m pip install .
    ```
    Les erreurs les plus courantes sont :
    - pip n'est pas installé (voir en dessous)
    - vous avez tapé ``python`` mais votre ordinateur utilise ``py`` (ou l'inverse)

* Si vous recevez cette erreur :
    ```
    WARNING: The script xxx.exe is installed in 'C:\Users\XXX\AppData\Local\Microsoft\WindowsApps' which is not on PATH
    ```
    C'est que vous avez sûrement téléchargé python depuis le Microsoft Store (pas bien).
    Téléchargez-le depuis le site officiel : [python.org](https://www.python.org/)

    Puis installez pip avec python :
    * ``py -m ensurepip --upgrade``
    * ``py -m pip install --upgrade pip``

* Si vous recevez cette erreur :
    ```
    WARNING: The script pixel-code.exe is installed in 'C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\Scripts' which is not on PATH.
    ```
    <details>
    <summary>Faites :</summary>

    1. Win + R
    2. Dans la popup rentrez : ``sysdm.cpl``
    3. Onglet avancé
    4. Variables d'environnement
    5. Dans Variables utilisateur → sélectionnez ``Path``
    6. Modifier
    7. Nouveau
    8. Collez ce chemin (changez avec votre nom d'utilisateur) : ``C:\Users\USERNAME\AppData\Local\Python\pythoncore-3.14-64\Scripts``
    9. OK -> OK -> OK
    10. Fermez et ré-ouvrez le terminal.

    Problème réglé (normalement).
    </details>

</details>

---

### Une fois l'installation terminée

> [!NOTE]
>
> Lancez l'app en tapant la commande : **pixel-code**

* Si l'app se lance **sans crash** mais que certains caractères sont mal affichés : allez voir [configuration](/docs/fr/config.md).
* Les mises à jour sont proposées automatiquement au lancement : voir [mise à jour](/docs/fr/update.md).
* Optionnel : depuis le clone, ``python3 first_use.py`` ajoute Pixel_Code lui-même comme projet d'exemple (marche seulement si Pixel_Code est installé avec pip, pas pipx). Vous pouvez aussi simplement ajouter un projet avec la touche ``a``.

### Pour les développeurs

```bash
pip install -e .
```
Avec une installation éditable, le code utilisé est votre clone : mettez-le à jour avec ``git pull`` (Pixel_Code n'installera pas les mises à jour lui-même).

### Désinstaller

```bash
pipx uninstall pixel-code   # ou : pip uninstall pixel-code
```
Vos projets et paramètres restent sur votre ordinateur (voir [configuration](/docs/fr/config.md) pour savoir où).
