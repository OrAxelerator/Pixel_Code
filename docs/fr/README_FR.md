# 🇫🇷 - Version française

[See the 🇬🇧/🇺🇸 README](/README.md)

![](/docs/assets/preview.png)

### Qu'est-ce que Pixel_Code ?
Pixel_Code est un outil en Python permettant d'enregistrer facilement vos projets en cours, et de les ouvrir facilement depuis le terminal avec une interface.


> [!NOTE]
>
> Pixel_Code est une TUI app (Terminal User Interface)

#### Comment ça marche ?
Voir la **documentation** : [ici](/docs/fr/index.md)



### Installation sur :

Pixel_Code a besoin de **Python 3.10+** et de **git**.

<details>
<summary><strong>1. Ubuntu/Linux</strong></summary>

* Si **pipx n'est pas installé :**

    ```bash
    sudo apt install pipx
    pipx ensurepath
    ```
* Téléchargez le projet et installez l'outil :

    ```bash
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    pipx install .
    ```
</details>

---
<details>
<summary><strong>2. MacOs</strong></summary>


 * Téléchargez le projet et installez l'outil (ou ``pip install .`` sans pipx) :

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


* Téléchargez le projet et installez l'outil :
    ```cmd
    git clone https://github.com/OrAxelerator/Pixel_Code.git
    cd Pixel_Code
    py -m pip install .
    ```
    (ou python)
    > [!WARNING]
    >
    > * Si vous recevez une erreur :
    > **Allez voir l'installation avancée Windows [en cliquant ici](/docs/fr/install.md)**

</details>

---

> [!IMPORTANT]
>
> Au premier lancement, Pixel_Code crée automatiquement ses fichiers utilisateur avec ``platformdirs``.
> Les anciens fichiers ``pixel_code/data/projects.json`` et ``pixel_code/data/parametres.json`` sont migrés si aucun fichier utilisateur n'existe déjà.


> Lancez l'app en tapant la commande : **pixel-code**

> [!NOTE]
>
> **Mises à jour** : au lancement, Pixel_Code propose d'installer la nouvelle version s'il y en a une (et démarre normalement sans connexion). Vos projets et paramètres sont conservés. Voir [mise à jour](/docs/fr/update.md).
>
> Vous venez de la **v0.5.2 ou plus ancienne** ? Réinstallez une fois à la main avec les commandes au-dessus (``pipx install --force .``).

> [!TIP]
>
> Pour que les icônes marchent, il faut mettre la police **"0xProto Nerd Font"** dans votre terminal, et si vous souhaitez exécuter le code dans VS Code, il faut aussi définir **Terminal › Integrated: Font Family** = `"0xProto Nerd Font"`
>
> Lien pour installer la police : https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/0xProto.zip

> [!TIP]
>
> Raccourcis clavier (tous [ici](/docs/fr/raccourci_clavier.md)) :
>
> * **↑/↓** : navigation.
> * **ENTRÉE** : ouvrir le projet avec votre éditeur.
> * **ESPACE** : afficher / cacher les détails d'un projet.
> * **/** : chercher un projet par nom, **c** : effacer la recherche.
> * **f** : filtrer les projets par statut, **m** : marquer un projet fini / à finir.
> * **a** : ajouter un projet, **e** : éditer un projet, **d** : supprimer un projet.
> * **p** : ouvrir les paramètres.
> * **q** : quitter.

---

### Fabriqué avec :
* Python
* Librairie python : curses pour l'affichage
* Librairie python : requests pour le système de mise à jour
* pyproject.toml
* .json pour les données enregistrées

### Licence :
Le projet est sous licence MIT - voir le fichier [LICENSE](/LICENSE.md) pour plus d'informations.

### Contribuer

[ici](/CONTRIBUTING.md)
