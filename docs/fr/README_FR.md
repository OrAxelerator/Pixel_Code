# 🇫🇷 - Versions :

![](/docs/assets/preview.png)

### Qu'est-ce que Pixel_Code ?
Pixel_Code est un outil en Python permettant de facilement enregistrer vos projets en cours, et de les ouvrir facilement depuis le terminal avec une interface.


> [!NOTE]
>
> Pixel_Code est une TUI app (Terminal User Interface)

#### Comment ça marche ?
Voir la **documentation** : [ici](/docs/fr/index.md)



### Instalation sur :
<details>
<summary><strong>1. Ubuntu/Linux</strong></summary>

* Si **pipx n'est pas installé :**
     
    ```bash
    sudo apt install pipx
    pipx ensurepath
    ```
* Téléchargez le projet et installez l’outil :

    ```bash
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pipx install .
    ```
</details>

---
<details>
<summary><strong>2. MacOs</strong></summary>


 *  Téléchargez le projet et installez l’outil  :

    ```cmd
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pip install -e .
    ```
    
</details>

---

<details>
<summary><strong>3. Windows</strong></summary>


*  Téléchargez le projet et installez l’outil :
     ```cmd
        git clone https://github.com/OrAxelerator/Pixel_Code.git
        cd ./Pixel_Code
        py -m pip install -e .
    ```
    >[!WARNING]
    >
    > * Si vous recevez une erreur :
    > **Allez voir installation avancée windows [en cliquant ici](/docs/fr/install.md)**
        
    </details>

---

> [!NOTE]
>
> Appelez l'app en tapant la commande : **pixel-code**


> [!TIP]
>
> Pour que les icônes marchent, il faut mettre la police **"0xProto Nerd Font"** dans votre terminal, et si vous souhaitez exécuter le code dans VS Code, il faut aussi définir **Terminal › Integrated: Font Family** = `"0xProto Nerd Font"`
>
> Lien pour installer la police : https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/0xProto.zip

> [!TIP]
>
> Raccourcis clavier :
> 
> * **ESPACE** : afficher / désactiver la vue complète sur un projet
> * **q** : arrêter l’exécution du programme
> * **↑/↓** : navigation
> * **p** : ouvrir les paramètres
> * **r** : recharger l’affichage (marche seulement dans branch main)
> * **e** : éditer les données d’un projet depuis Pixel_Code (pas encore fonctionnel)
> * **a** : ajouter un projet
> * **d** : suprimer un projet
> * **g** : faire action github (pas dispo)

---

### Fabriqué avec :
* python
* librairie python : curses pour l'affichage
* librairie python : request pour le systeme de mise a jour
* pyproject.tmol
* .json pour les données enregistrées

### License : 
Le projet est sous license GNU - voir le fichier [LICENSE](/LICENSE.md) pour plus d'informations.

### Contributing info

[ici](/CONTRIBUTING.md)