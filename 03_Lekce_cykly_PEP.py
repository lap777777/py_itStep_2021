# cykly:
# cykly se skladaji ze 3 kroku:
#  * neco nastavim, musim dat podminku a pak to v cyklu porad menit

# while cyklus
print("Program kalkulacka")
print()
number1 = 1
while number1 != 0:
    number1 = int(input("Zadej prvni cislo: "))
    number2 = int(input("Zadej druhe cislo: "))
    vysledek = number1 + number2
    print("Vysledek je " + str(vysledek))
    print()

number1 = 1
while number1 < 11:
    print(number1)
    number1 += 1
print("konec")
print()

# for cyklus
# for cyklus ma zacatek, konec a krok ..... konec je vzdy n-1, a zacatek, konec a krok se da uvest ve funkci range()
for number in range(5): # cyklus provede 5 operaci od 0 do 4
    print(number)
print()

for number in range(2,7): # cyklus provede 5 operaci od 2 do 6
    print(number)
print()

for number in range(2, 17, 5): # cyklus se provede od 2 do 16, ale bude skakat po krocich o velikossti 5
    print(number)
print()

for number in range(10, 3, -1): # zacnu na desitce, jdu o -1 dolu a koncim (n-1) takze 4
    print(number)
print()

# PEP - Python enhancement proposal - vylepsovani pythonu
# PEP 498 - zavedeni f stringu
# PEP 20 -- The Zen of Python - 19. doporuceni jak spravne programovat
# PEP 8 -- Style Guide for Python Code - https://www.python.org/dev/peps/pep-0008/

cislo = 1
while cislo:
    cislo = int(input("Zadej cislo: "))
    print(cislo)
print()
# program bude porad chtit zadavat cislo a tisknout ho
# a zapis while cislo: je stejny jako while cislo != 0:
# protoze 0 je False, takze while se dela dokud je True, jak mile da nekdo 0, tak je to False a while konci

# continue a break
# continue - vrati cyklus na zacatek
# break - ukonci cyklus

# tisk cisel do 10
cislo = 0
while cislo < 10:
    cislo += 1
    if cislo == 5:
        continue
    print(cislo)
print()

for cislo in range(10):
    if cislo == 5:
        continue
    if cislo == 9:
        break
    print(cislo)
print()
