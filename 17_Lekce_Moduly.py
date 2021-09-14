### MODULY ########################################

# moduly - soubory v Pythonu, ktere obsahuji funkce a konstanty (promenne)
# vkladam je pomoci import a pak pisu nazev_modulu.nazev_funkce()

import math  # matematicky modul
# nainportoval jsem modul math - pak pisu vsechny funkce z modulu math.

sinus = math.sin(5)
print(sinus)
print(math.pi)

# pokud bych chtel psat funkce bez tecky, tak musim napsat tento zapis
from math import log, pi, cosh
print(pi)
# lepsi pouzivat vzdy cely nazev modulu, je pak jasne videt, ze je to funkce z daneho modulu a nespinim si globalni prostor

import pandas as pd # lze modulum davat i vlastni aliasy

# jak zjistim, co je v modulu - jit do dokumentace neba dam funkci dir(math) a ten vyspise seznam se vsemi funkcemi a konstantami
# dir lze pouzit na vse - na objekty napr - vypise metody a promenne na objektu

print(dir(math))

import os   # modul operacni system

print(os.getcwd())  # funkce, ktera mi vrati adresar, kde ted jsem

### Vlastni modul #####################################

import mymodule as my

print(my.konstanta)
print(my.scitani(10,20))
print(my.scream())
print()

# sys.path ... ukazuje cesty, kam se Python diva pro moduly a kam je muzu ulozit a na prvnim miste je aktualni adresar, kam muzu davat svoje moduly

# pypi.org - prehled modulu, ktere jsou nainstalovat
# balicky - nadrazene modulum - velke baliky funkci a konstant




# globalni promenna name, ktera je nastavena na main


