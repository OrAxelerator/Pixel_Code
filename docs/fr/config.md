# Configuration

### Activer les icônes

Pour activer les icônes, utilisez la police **"0xProto Nerd Font"** dans votre terminal, puis activez ``Utiliser nerd font`` dans les paramètres (touche ``p``). Si vous lancez Pixel_Code dans VS Code, définissez aussi **Terminal › Integrated: Font Family** = `"0xProto Nerd Font"`.

> [!NOTE]
>
> Peut-être que votre terminal ne supporte pas les Nerd Fonts, alors trouvez une alternative.

> Lien pour installer la police : https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/0xProto.zip

### Changer les paramètres

Utilisez l'écran des paramètres avec la touche ``p``. **Certains paramètres ne sont pas encore modifiables** depuis cet écran, changez-les directement dans ``parametres.json`` (voir [architecture](/docs/fr/architecture.md) pour toutes les clés).

Paramètres disponibles sur l'écran : langue (``en``/``fr``), nerd font, éditeur (``code``/``vim``/``cmd``), dépôt (lien par défaut quand on ajoute un projet), vérifier les mises à jour au lancement, position du logo, version (lecture seule).

### Où sont mes fichiers ?

Pixel_Code utilise ``platformdirs`` pour enregistrer vos fichiers en dehors du code, donc ils sont **conservés pendant les mises à jour** :

| | ``parametres.json`` (paramètres) | ``projects.json`` et ``debug.log`` |
| --- | --- | --- |
| macOS | ``~/Library/Application Support/Pixel_Code/`` | ``~/Library/Application Support/Pixel_Code/`` |
| Linux | ``~/.config/Pixel_Code/`` (ou selon vos variables XDG) | ``~/.local/share/Pixel_Code/`` |
| Windows | ``C:\Users\<user>\AppData\Local\OrAxelerator\Pixel_Code\`` | ``C:\Users\<user>\AppData\Local\OrAxelerator\Pixel_Code\`` |

Chaque projet a aussi un fichier ``.pixelcode.json`` à sa racine avec son nom, sa description, ses langages et son dépôt.

### Mode debug

Depuis la racine du clone, tapez : ``python3 pixel_code/__main__.py --debug`` (ou ``py``/``python`` selon votre OS). Les logs sont écrits dans ``debug.log`` (voir le tableau au-dessus), suivez-les avec ``tail -f debug.log``.

En mode debug la vérification des mises à jour est fausse (voir [mise à jour](/docs/fr/update.md#debug)), ajoutez ``--wifi`` pour vraiment vérifier GitHub.

### Sous-commandes

| Commande | Action |
| --- | --- |
| ``pixel-code --clean-projects`` | supprime les projets invalides si leur chemin n'existe pas/plus |
| ``pixel-code --clean-projects-hard`` | supprime les projets invalides si leur chemin ou leur ``.pixelcode.json`` n'existe pas |
| ``pixel-code --reset-config`` | réinitialise ``parametres.json`` (vos projets sont conservés) |
| ``pixel-code --clear-log`` | efface le contenu de ``debug.log`` |
| ``pixel-code --debug`` | active les logs de debug |
| ``pixel-code --wifi`` | vérifie vraiment les mises à jour sur GitHub, même en mode debug |
| ``pixel-code -h`` | affiche l'aide |
