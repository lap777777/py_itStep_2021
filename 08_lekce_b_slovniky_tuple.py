# dosavadni datove typy
my_string = "abcde"         # imutable - neda se menit
my_list = [1, 2, 3, 4, 5]   # da se menit jednotlive prvky
# jsou hodne podobne typy, ale string se neda menit
# retezec je seznam znaku, seznam je seznam cehokoliv
# oba jsou sekvence

# *********************************************************************
# TUPLE - ntice
# *********************************************************************
# tuple je stejny jako list, ale nelze ho menit - IMUTABLE
# pouziti jako napr. klic pro slovniky
my_tuple = (1, 2, 3, 4, 5, 6, 7,)
try:
    my_tuple[0] = 10
except:
    print("V tuple nelze menit hodnoty")
# jinak se tuple pracuje jako s listem
my_tuple[:10]
tuple1 = my_tuple[:]
# nelze menit, tak nefunguje .append()

# existuje prazdna ntice 
tuple2 = ()
print(type(()))
print(type(tuple2))
print(len(my_tuple))
print(len(tuple2))

# narozdil od seznamu nejde udelal 1 prvkovou netici
a = [1]
b = (1)  # tohle neni tuple, tohle je priorita matematicka
# jednoprvkovou ntici mohu zadat takto
tuple3 = (10,)
print(tuple3)
# stejne jako string, to jde nasobit
c = (5+6,)*3
print(c)    # vysledek je (11, 11, 11)

# tuple ze stringu:
t1 = tuple("abcef")
print(t1)
# tuple z listu:
t2 = tuple([1,2,3,4])
print(t2)
t3 = tuple([3])     # z jednoprvkoveho listu dostanu jednoprvkovou tuple
print(t3)   

# muzu menit list uvnitr tuple
t4 = ([1, 2], [3, 4])      # tuple ma dva prvky a list ma dva prvky
t4[0][0] = 5
print(t4)

# specialni pouziti entice - pro ukladani vice promenych (nepouziji zavorky)
prvni, druha = "ahoj", "papousek"
print(prvni)
print(druha)
# prohozeni zapisu:
pomocna = prvni
prvni = druha
druha = pomocna
print(prvni)
print(druha)
# zapis zkraceny
prvni, druha = druha, prvni     # takhle to prohodim pomoci tuple
print()

# *********************************************************************
# DICTIONARY  ... slovnik
# *********************************************************************
# soubor dvojic {klic: hodnota, klic: hodnota, klic: hodnota, ...}
# seznam/list ma svuj ciselny index
# slovnik ma index dle klicu, takze volam klice
# klic nelze menit, ale hodnotu klice lze menit
# pristup do slovnika pomoci hranatych zavorek, stejne jako vsude
# jako klic lze dat string, cislo, tuple - immutable, nelze dat list
eng_cz = {"red": "cervena", "blue": "modra", "green": "zelena"}
eng_cz["white"] = "bila"      # pridavani do slovniku
print(eng_cz)
klice = eng_cz.keys()    # vypise klice - vypisou se v listu, tak pres klice muzu iterovat
print(klice)
values = eng_cz.values()    # vypisuji hodnoty
print(values)
vsechno = eng_cz.items()    # vypisuji cely slovnik, ale jako seznam = lze iterovat
print(vsechno)    
# keys, values, items = VIEWS = neprave seznamy ... jsou zive, meni se pokud se prida klic, hodnota
for key in eng_cz.keys():
    print(f"{key} = {eng_cz[key]}")
# lepsi priklad
for key, value in eng_cz.items():
    print(f"{key} = {value}")

del eng_cz["red"]   # vymaze prvek ze slovniku
print()
