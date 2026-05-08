# Configuration nécéssaire :

* Activer réellement les icones :

    Pour Activer les icones il suffit de changer la font de votre terminal par **"0xProto Nerd Font"**, et si vous souhaitez exécuter le code aussi dans VS Code, il faut appliquer la font dans le terminal vscode **Terminal › Integrated: Font Family** = `"0xProto Nerd Font"`.
    >[!NOTE]
    >
    > Peut etre que votre cmd ne supporte pas NerdFont alors trouver une alternative.
    

    > Lien pour installer la police : https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/0xProto.zip

<br>

>  Changer les paramètres :
>  Pour changer les paramètres une fenêtre est accessible via la touche ``p`` mais peut-être que certains paramètres **ne sont pas encore modifiables** depuis cette interface.
>  Les paramètres sont enregistrés dans le dossier de configuration utilisateur géré par ``platformdirs`` :
>  - macOS : ``~/Library/Application Support/Pixel_Code/parametres.json``
>  - Linux : ``~/.config/Pixel_Code/parametres.json`` ou selon vos variables XDG
>  - Windows : ``C:\Users\<user>\AppData\Local\OrAxelerator\Pixel_Code\parametres.json``

> [!NOTE]
>
> Les projets sont enregistrés séparément dans le dossier de données utilisateur :
>  - macOS : ``~/Library/Application Support/Pixel_Code/projects.json``
>  - Linux : ``~/.local/share/Pixel_Code/projects.json``
>  - Windows : ``C:\Users\<user>\AppData\Local\OrAxelerator\Pixel_Code\projects.json``
>
> Ces fichiers sont conservés même si le code de Pixel_Code est remplacé pendant une mise à jour.

>[!NOTE]
>
> Lancer en **mode debug** :
>   Depuis la racine du projet vous pouvez taper la commande : ``python3 pixel_code/__main__.py --debug`` (ou py/python selon votre machine). Les logs sont envoyés dans ``debug.log`` dans le dossier de données utilisateur. A noter que pour le moment les log ne sont quasiment pas utilisés.

