# Task 1
# zadej 3 cisla a udelej z nich trojciferne cislo
prvni = input("Zadej prvni cislo: ")
druhe = input("Zadej druhe cislo: ")
treti = input("Zadej treti cislo: ")
cislo = prvni + druhe + treti
print(cislo)
print("----matematicky-----")
prvni = int(prvni)
druhe = int(druhe)
treti = int(treti)
cislo1 = prvni * 100 + druhe * 10 + treti
print(cislo1)
print()

# Task 2
# zadej 4ciferne cislo a udelej soucin jeho jednotlivych cifer
cislo = input("Zadej 4ciferne cislo: ")
prvni = int(cislo[0])
druhe = int(cislo[1])
treti = int(cislo[2])
ctvrte = int(cislo[3])
soucin = prvni * druhe * treti * ctvrte
print(f"Vysledny soucit cisla {cislo} je {soucin}")
print("----matematicky----------")
cislo = int(cislo)
prvni == cislo // 1000
druhe == cislo % 1000 // 100
treti == cislo % 1000 % 100 // 10
ctvrte == cislo % 1000 % 100 % 10
soucin == prvni * druhe * treti * ctvrte
print(f"Vysledny soucin cisla {cislo} je: {soucin}")
print()

# Task 3
# zadej delku v metrech a prepocti ji na mm, cm, dm a mile.
metry = int(input("Zadej delku v metrech: "))
print(f"Zadano {metry} metru, coz je: ")
mm = 1000 * metry
cm = 100 * metry
dm = 10 * metry
mile = metry / 1000 * 0.6214
print(f"{mm:,} mm,")
print(f"{cm:,} cm,")
print(f"{dm:,} dm,")
print(f"{mile:,} mile.")
print()

# Task 4
# spocitej obsah trojuhelniku na udaju zadanych uzivatelem - zakladny a vysky
zakladna = int(input("Zadej delku zakladny trojuhleniku: "))
vyska = int(input("Zadej vysku trojuhelniku: "))
obsah = zakladna * vyska / 2
print(f"Obsah trojuhelniku je {obsah}")
print()

# Task 5
# zadej 4ciferne cislo a obrat ho. Napr. pokud zadas 1234, tak vysledek ma byt 4321
cislo = input("Zadej 4ciferne cislo: ")
cislo1 = cislo[3] + cislo[2] + cislo[1] + cislo[0]
print(cislo1)
print("----matematicky------")
cislo = int(cislo)
prvni == cislo // 1000
druhe == cislo % 1000 // 100
treti == cislo % 1000 % 100 // 10
ctvrte == cislo % 1000 % 100 % 10
cislo1 = ctvrte * 1000 + treti * 100 + druhe * 10 + prvni
print(cislo1)
print()
