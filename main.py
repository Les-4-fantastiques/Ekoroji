from trad import *

a = TradHtml(['index.html', 'explorer.html', 'messcans.html', 'styleexplorer.css', 'styleindex.css', 'stylemesscans.css'], "Ekoroji", 'templates/')
a.read()
a.tradFiles()