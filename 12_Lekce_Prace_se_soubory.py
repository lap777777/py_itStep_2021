import os
"""
print()
print(os.getcwd())       # get current working directory - divam se v jake slozce pracuji
print(os.listdir)        # vypise nam vse co je v danem adresari
os.chdir("07_Python")    # meni slozku odkud beru soubor
os.chdir("..")            # o jeden adresar vyse
print()

file = open(os.path.join(os.curdir, "Archiv", "Slovniky", "Slovniky.txt"))
# vyjdi z aktualniho adresare, bez do podslozky archiv, slovniky a tam otevri soubor Slovniky.txt"
# os.curdir jde vyhodit pokud nechci odkazovat od soucasneho kalendare

"""
print("1-Otevirani_souboru-READ--------------------------------------")

file = open("slova.txt", encoding="utf-8")   # oteviram si soubor a ukladam ho do promenne

fruit = file.read()

print(fruit)

file.close()
# kdyz otevru soubor, tak je potreba ho zavrit
print()

file = open(os.path.join(os.curdir, "12_Lekce_zzzpodklady", "slova1.txt"), encoding="utf-8")

fruit1 = file.read()

print(fruit1)
file.close()

# read ma velkou casovou narocnost, ukladam si celkovy soubor do promenne
print("2-Otevirani_souboru-READLINES----------------------------------")
file = open("slova.txt", encoding="utf-8")
fruit2 = file.readlines()
# precte vsechny radky a ulozi je do listu
# casove velmi narocne
print(fruit2)
file.close()

print("3-Otevirani_souboru-READLINE-ITEROVANI--------------------------")

file = open("slova.txt", encoding="utf-8")
fruit3 = file.readline()
# tohle vraci pouze prvni radku = nejmene casove narocne
print(fruit3)
file.close()
print()

file = open("slova.txt", encoding="utf-8")
for line in file:
    print(line, end="")
# v promenne line mam ulozeny pouze jeden aktualni radek = zabira malo pameti
# idealni pro prohledavani - iterovani - vezmu radku, aplikuji podminku, pokud false, tak zahodim, pokud true, tak muzu ulozit nekam
file.close()
print()

# kratsi zapis
for line in open("slova.txt", encoding="utf-8"):
    print(line, end="")
file.close()
print()

# nejlepsi zapis:
with open("slova.txt", encoding="utf=8") as f:
    for line in f:
        print(line, end="")
    print("posledni prikaz uvnitr with")
print()
# with = context management - stara se automaticky o soubor, praci s nim a hlavne na konci zavreni souboru

## MODY pro cteni open(file, "r")

print("4-Zapisovani_do_noveho_souboru-----------------------------------")

my_list = [55, 66, 78, 95, 56, 23]

with open("cisla.txt", "w") as f2:    # parametr "w" pro zapisovani
    for cislo in my_list:
        f2.write(str(cislo) + "\n")          # zapisuji cisla do souboru cisla.txt
    

print("5-Zapisovani_do_stavajiciho_souboru------------------------------")

my_list = [55, 66, 78, 95, 56, 23]

with open("slova.txt", "a") as f2:    # parametr "a" pro pridani
    for cislo in my_list:
        f2.write("\n" + str(cislo))      

print("6-Zapisovani_ze_stareho_do_noveho_souboru-----------------------")

with open("slova.txt") as f1, open("nova_slova.txt", "w") as f2:
    for line in f1:
        f2.write(line)


