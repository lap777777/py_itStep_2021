### NumPY
# zakladni datova struktura v numpy je pole (podobne seznamu v Pythonu)
# vsechny hodnoty musi byt idealne stejny datovy typ
# chceme dopredu znat jeho velikost - dobre pro rychle vypocty

import numpy as np

#print(np.__version__)

# pole:
# 1 rozmerne - vektor
# 2 rozmerne - matice
# 3 a vice rozmerne

pole = np.array([1, 2, 3, 4, 5, 6])  # jednorozmerne pole - zadavam to tam jako list nebo tuple
print(pole)
print()

print(pole.dtype) # datovy typ pole
print(pole.shape) # pocet radku a sloupcu
print(pole.ndim) # pocet dimenzi
print(pole.size) # pocet policek
print()

pole1 = np.array([1, 2, 3, 4, 5, 6], dtype=float) 
# np.array ma dva argumenty (prvni povinny = pole) a druhy je datovy typ
print(pole1.dtype)
print()

pole2 = np.zeros(7)
print(pole2)
pole3 = np.ones(4)
print(pole3)
pole4 = np.zeros(5, dtype=bool)
print(pole4)
print()

# prazdne pole ... metoda empty
pole5 = np.empty(5)
print(pole5)
print()

"""
pole6 = np.array([[[0,0,0,0]
                [0,0,0.0]],
                [[1,1,1,1]
                [2,2,2,2]],
                [[3,3,3,3]
                [4,4,4,4]]]).shape(3, 2, 4)  # 3 dimenze, dva radky, 4 smloupce
"""

# pole mohu scitat a dalsi operace (-, *, /, //, %, **) - musi byt stejny pocet prvku
pole7 = np.array([5,6,7,8,9])
pole8 = np.array([10,11,12,13,14])
print(pole7)
print(pole8)
pole9 = pole7 + pole8
pole10 = pole7 * pole8
pole11 = pole7 // pole8
print(pole9)
print(pole10)
print(pole11)
print()

# muzi i pricist jedno cislo ke vsem prvnkum
pole12 = pole7 + 10
print(pole12)
# pokud tech 10 precitat i pres jednoprvnkove pole
pole13 = np.array([10])
# kdyz jedno z poli ma mensi rozmer, tak numpy prida hodnoty
pole14 = pole7 + pole13
print(pole14)
pole15 = pole14 / 10
print(pole15)
print()

# metody - matematicke - napr. suma, mean, min, max atd
# numpy.ndarray.sum() - volam na poli metody
print(pole14.sum())
print()

# Python Data Science Book, O`Reilly
# nauc se python - NumpPy

# plneni poli
pole16 = np.full(8, 5)  # naplni cislem 5, 8 poli jednorozmerne matice
pole17 = np.full((4,6),5)  # naplni cislem 5 dvourozmerne pole o 4 radcich a 6 sloupcich

# plneni pole np.arrange (funguje stejne jako range v Pythonu)
pole18 = np.arange(7) # udela to pole o 7 prvcich, od 0 az do 6
print(pole18)
pole19 = np.arange(7,70,7) # udela pole od 7 do 63, krok = 7
print(pole19)
print()
# plneni pole np.linspace ... od, do a kolik chlivku
pole20 = np.linspace(1, 10, 10, dtype=int)
print(pole20)
print()

# indexovani poli
pole31 = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
print(pole31[0])  # prvni prvek
pole32 = np.array([0, 5, 7])
print(pole31[pole32]) # indexovani pres pole - vrati 0., 5. a 7. prvek
print(pole31[[0, 1, 2]]) # jiny zpusob indesovani pres pole, vracim 0., 1, a 2. 
print()
# indexovani vicerozmernych poli 
pole33 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(pole33)
print(pole33[1][2])
print(pole33[1,2])
print()

# predalani pole = np.reshape
pole34 = np.arange(1, 21)
print(pole34)
print()
pole35 = pole34.reshape(2,2,5)
print(pole35)
print()

# operatory >, < 
pole36 = np.array([2,3,4,5,6,7,8,7,6,5,4,3,2])
print(pole36)
print(pole36 > 4)
print(pole[pole > 4]) # pres podminku muzu indexovat, vypadnou mi jenom hodnoty, kde jsou cisla vetsi nez 4
print()

# horizontalni a vertikalni spojovani
# p.hstack((pole1,pole2)) .. .horizontalni spojeni poli (vedle sebe)
# np.vstack((p)ole1, pole2) ... vertikalni spojeni poli (pod sebe)
pole37 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pole38 = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
pole39 = np.hstack((pole37,pole38))
print(pole39)
pole40 = np.vstack((pole37,pole38))
print(pole40)
print()



