<p align="center"><img src="sources\client\assets\logos\Ekoroji_light.svg" alt="Icon" width="128"/></p>

## <p align="center">Ekoroji</p>

Ekoroji est une application web pour téléphone. Elle a pour but de renseigner l'utilisateur sur la manière dont recycler chaque objet, que ce soit des aliments, déchets ou autres. Elle inclut également une rubrique d'articles pour sensibiliser l'utilisateur.


## <p align="center">Auteur(e)s</p>

- [@ambre66160](https://github.com/ambre66160) web developer
- @benoiurlc database manager
- @ghostizzoks python developer
- [@untypequicode](https://github.com/untypequicode) python developer


## <p align="center">Documentation</p>

Il est nécessaire d'installer la bibliothèque Flask, ainsi au lancement du fichier Ekoroji.py. Ensuite il sera possible d'accéder au site web depuis l'adresse url fourni dans le terminal.

Il est egalement disponible une bibliothèque permettant de convertir un site web entier HTML et CSS en programme python grace au fichier "trad.py".


## <p align="center">Captures d'écran</p>

<p align="center">
<img src="/doc/img/Ekoroji_app_informer.png" alt="Ekoroji_app_informer.png" width=30%/>
<img src="/doc/img/Ekoroji_app_explorer.png" alt="Ekoroji_app_explorer.png" width=30%/>
<img src="/doc/img/Ekoroji_app_scans.png" alt="Ekoroji_app_scans.png" width=30%/>
</p>


## <p align="center">Utilisation / Exemples</p>

Pour utiliser la bibliothèque disponible "trad.py"

```python
from trad import *

siteweb = TradHtml([index.html, index.css, compte.html, compte.css], "Nom_du_site_web", "Emplacement fichiers HTML et CSS")
siteweb.read()
siteweb.tradFiles()

>>>"Nom_du_site_web.py"
```
