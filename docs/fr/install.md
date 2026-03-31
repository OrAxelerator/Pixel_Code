# Installation - poussé


<details>
<summary><strong>1. Installation sur Linux :</strong></summary><br>

tapez dans un terminal : ```pipx --version```

Si rien est affiché installé pipx avec :
```sudo apt install pipx``` et ```pipx ensurepath```

Puis cloner le depo github :     
```bash
git clone https://github.com/OrAxelerator/Pixel_Code.git
cd Pixel_Code
pipx install .
```

</details>

<details>
<summary><strong>2. Installation sur MacOs :</strong></summary><br>

clonez le dépot et initialisez le module
```cmd
git clone https://github.com/OrAxelerator/Pixel_Code.git
cd Pixel_Code
pip install -e .
```

</details>

<details>
<summary><strong>3. Installation sur Windows :</strong></summary><br>

L'instalation sur windows n'es pas encore 100% documenté dans tout les cas..

Téléchargez le projet :
```cmd
git clone https://github.com/OrAxelerator/Pixel_Code.git
cd ./Pixel_Code
```
regardez si pip est installez avec : ```pip --version``` ou ```py -m pip --version```<br>
Si **pip n'est pas installé**, installez le.


Puis Tapez : ```py -m pip install -e .``` :
* Si vous recevez l'erreur :
    ```
    Successfully uninstalled pixel-code-0.1.0 WARNING: The script pixel-code.exe is installed in 'C:\Users\User\AppData\Local\Python\pythoncore-3.14-64\Scripts' which is not on PATH. Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location. Successfully installed pixel-code-0.1.0
    ```
    <details>
    <summary>Faite :</summary>
    
    1. faite : 
    2. Win + R 
    3. dans la popup rentrez : sysdm.cpl
    4. onglet avancé
    5. variables d'environement
    6. Dans Variables utilisateur → sélectionner Path
    7. Modifier
    8. Nouveau
    9. coller ce chemin si (changez avec votre username) : C:\Users\votre username\AppData\Local\Python\pythoncore-3.14-64\Scripts
    10. OK -> OK -> OK
    11. Fermez et re-ouvrez le terminal après ça.
        
    et problème réglez
    </details>

* Ou sinon si vous recevez cette eurreur : 
    ```
    WARNING: The script xxx.exe is installed in 'C:\Users\XXX\AppData\Local\Microsoft\WindowsApps' which is not on PATH
    ```
    C'est que vous avez surement télécharger python depuis le Microsoft store (pas bien)
    allez le télechrgez sur le site officiel : [python.org](https://www.python.org/)

    installé pip avrec python : 
    * py -m ensurepip --upgrade
    * py -m pip install --upgrade pip

</details>

--- 

### Une fois l'intstalation fini :

> [!NOTE]
>
> Appelez l'app en tapant la commande : **pixel-code**

---

Si le code se lance **sans crash** mais a des bugs a affiché certain caractère icone : allez voir [CONFIG](/docs/fr/config.md)