# Task 1
# vypocet sumy a soucinu zadanych 3 cisel.
print()
prvni = int(input("Zadej prvni cislo: "))
druhe = int(input("Zadej druhe cislo: "))
treti = int(input("Zadej treti cislo: "))
suma = prvni + druhe + treti
product = prvni * druhe * treti
print()
print(f"Suma zadanych cisel je: {suma:.2f}")
print(f"Soucin zadanych cisel je: {product: .2f}")
print()

# Task 2
# vypocet zustatku po mzde a hypotece a ostatnich nakladech
salary = int(input("Zadej vysi platu: "))
loan = int(input("Zadej vysi pujcky: "))
naklady = int(input("Zadej vysi dalsich nakladu: "))
zbytek = salary - loan - naklady
print(f"Zbytek po vsech splatkack je: {zbytek:0.2f}")
print()

# Task 3
# vypocet obsahu kosoctverce a diamtu na zaklade zadanych diagonal
diag1 = int(input("Zadej delku diagovanly 1: "))
diag2 = int(input("Zadej delku diagonaly 2: "))
obsah_kosoctverce = (diag1 * diag2) / 2
pocet_stran = 57
obsah_diamantu = pocet_stran * obsah_kosoctverce
print(f"Obsah kosoctverce: {obsah_kosoctverce}")
print(f"Obsah diamantu: {obsah_diamantu}")
print()

# Task 4
print("To be \nor not \nto be")
print()

# Task 5
print('"Life is what happens')
print("   when")
print('          you`re busy making other plans"')
print("                                      John Lennon")
print()
