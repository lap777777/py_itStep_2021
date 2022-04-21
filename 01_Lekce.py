# operatory

# + scitani, - odcitani, * nasobeni, / deleni, // deleni celym cislem, % modulo = zbytek po celociselnem deleni
# x = x + 1, stejny zapis je x += 1
# ** mocnina, 2 ** 3 - to jsou 2 na treti

# velka cisla - muzu davat potrzitka 123_456_789.56

# datove typy:
# "ahoj" - string ... retezec
# 4 - integer, cele cislo
# 4.0 - float, desetinne cislo
# [4, 5, 6] - list, seznamy hodnot
# True, False - boolean - vsechny cisla krome nuly jsou True, 0 ... je False, False .. 0, nebo prazdna promenna, None
# type() ... vraci datovy typ promenne

# pretypovani datoveho typu ... int(x), float(x), str(x), bool(x)

# pokud udelam cislo = int(bool(9)) ... vrati 1

cislo = 5  # integer
print(cislo)
cislo = float(cislo)  # float
print(cislo)
print("***********************")
print()
print(2 + 4)
print("ahoj", "Pavle,", "jak se mas?", sep="---")    # definice oddelovace ve funkci print
print("Co si das", "dnes k veceri?")
print("Nic,", "uz jsem toho mel dost", sep="???")
print("Pojd", "uz", "domu", sep="\"")
print("***********************")
print()

# defaultne nastaveno sep=" ", end="\n"  - defaultne separator je mezera a na konci radku je zalomeni

# Task 1
"""
Print the quote “Nothing will work unless you do” on
different lines. Like this:
            Nothing
            will work
            unless you do
"""
print("Task1:")
print()
print("      Nothing \n      will work \n      unless you do.")
print()

# Task 2
"""
Print the quote “Anyone who stops learning is old, whether
at twenty or eighty” Henry Ford on different lines. like this:
“Anyone who
    stops
        learning is old,
            whether at twenty or eighty”
                                Henry Ford
"""
print("Task2:")
print('\"Anyone who')
print("\tstops")
print("\t\tlearning is old,")
print('\t\t\twhether at twenty or eighty\"')
print('\t\t\t\t\t\tHenry Ford')

# Task 3
# The user types in two numbers. Find the sum, difference, and product of these numbers. Display the result on the screen.
print("Task3:")
cislo1 = int(input("Zadej prvni cislo: "))
cislo2 = int(input("Zadej druhe cislo: "))
soucet = cislo1 + cislo2
rozdil = cislo1 - cislo2
product = cislo1 * cislo2
print("Soucet: ", soucet)
print("Rozdil: ", rozdil)
print("Soucin: ", product)
print()

# Task 4
# The user types in two numbers. The first number is a value, and the second is a percentage to be calculated. Let’s say we typed in 50 and 10. The displayed number should be 10% of 50. Result: 5.
print("Task4:")
cislo = int(input("Zadej cislo: "))
procento = int(input("Zadej procento jako cele cislo: "))
vypocet = cislo * procento / 100
print(f"{procento}% z {cislo} je {vypocet}")
print()

# Task 5
# Write a program that calculates the area of a rectangle. The user types in the width and height of the rectangle.
print("Task5:")
strana = int(input("Zadej delku strany a: "))
strana2 = int(input("Zadej delku strany b: "))
obsah = strana * strana2
print(f"Obsah obdelniku je: {obsah}")
print()


