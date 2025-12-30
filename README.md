```text
$$$$$$$\  $$\                     $$\        $$$$$$\                  $$\           
$$  __$$\ \__|                    $$ |      $$  __$$\                 $$ |          
$$ |  $$ |$$\ $$\   $$\  $$$$$$\  $$ |      $$ /  \__| $$$$$$\   $$$$$$$ | $$$$$$\  
$$$$$$$  |$$ |\$$\ $$  |$$  __$$\ $$ |      $$ |      $$  __$$\ $$  __$$ |$$  __$$\ 
$$  ____/ $$ | \$$$$  / $$$$$$$$ |$$ |      $$ |      $$ /  $$ |$$ /  $$ |$$$$$$$$ |
$$ |      $$ | $$  $$<  $$   ____|$$ |      $$ |  $$\ $$ |  $$ |$$ |  $$ |$$   ____|
$$ |      $$ |$$  /\$$\ \$$$$$$$\ $$ |      \$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$\ 
\__|      \__|\__/  \__| \_______|\__|$$$$$$\\______/  \______/  \_______| \_______|
                                      \______|
```
### 🇫🇷 :
### Qu'est-ce que Pixel_Code ?
Pixel_Code est un outil en Python permettant de facilement enregistrer vos projets en cours, et de les ouvrir facilement depuis le terminal avec une petite interface.

![](./Capture%20d’écran%202025-12-28%20à%2014.52.06.png)

> [!NOTE]
>
> Pixel_Code est une TUI app (Terminal User Interface)

#### Comment ça marche ?

Objectif => faciliter l’ouverture via VS Code et une meilleure organisation et visualisation des projets en cours et finis.

> Appelez l'app en tapant la commande : **pixel-code**


> [!IMPORTANT]
>
> Pour que les icônes marchent, il faut mettre la police **"0xProto Nerd Font"** dans votre terminal, et si vous souhaitez exécuter le code dans VS Code, il faut aussi définir **Terminal › Integrated: Font Family** = `"0xProto Nerd Font"`
>
> Lien pour installer la police : https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/0xProto.zip

> [!NOTE]
>
> Raccourcis clavier :
> 
> * **ESPACE** : afficher / désactiver la vue complète sur un projet
> * **q** : arrêter l’exécution du fichier
> * **↑/↓** : navigation
> * **p** : ouvrir les paramètres
> * **r** : recharger l’affichage (marche seulement dans main)
> * **e** : éditer les données d’un projet depuis Pixel_Code (pas encore fonctionnel)

Installation pour Ubuntu (linux) : 

**Si pipx n'est pas installé :**
```cmd
sudo apt install pipx
pipx ensurepath
```
Téléchargez le projet et installez l’outil :
```cmd
git clone https://github.com/OrAxelerator/Pixel_Code.git
cd Pixel_Code
pipx install .
```
Lancez ensuite le programme avec :
```cmd
pixel-code
```