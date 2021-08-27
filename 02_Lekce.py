
# funkce help() ... obsahuje dokumentaci, napr. se muzu zeptat help>keywords, ven se vyskajuje pomoci   quit nebo control C
# nebo rovnou help("keywords")

# matematicke operatory: ==, !=, <, >, >=, <=

# podminky:
# True ... vsechny cisla krome 0
# False ... 0, none, prazdny string, list, dictionary
# v pripade porovnavani podminek, Python pracuje, dokud jsou podminky splneny, pokud nejsou splneny, tak nevrati False, ale vrati promennou, funkci, cislo, list, ktery je false, to same plati pro True, nevrati True, ale vrati prvni promennou, cislo, list, funkci, ktera je True

vek = 20
prukazka = "VIP"
if vek >= 18:
    print("Vitejte")
    print("Pojdte dal")
    if vek > 30:
        print("mam pro tebe specialni darek")
        print("je tamhle v krabici")
        if prukazka == "VIP":
            print("stav se ve VIP salonku")
    else:
        print("kup si vino na baru")
        print("stoji 30 korun")
else:
    print("Bez domu")
    print("Vrat se, az ti bude 18.")
print("konec programu")
print()

# Practise 1
# Task 1
# The user types in a number. Check if it is even or odd. If the number is even, print the number and the text “Even number.” If the number is odd, print the number and the text “Odd number.”
cislo = int(input("Zadej libovolne cele cislo: "))
if cislo % 2 == 0:
    print(f"Zadane cislo {cislo} je sude")
else:
    print(f"Zadane cislo {cislo} je liche.")
print()

# Task 2
# The user types in a number. Check if it is a multiple of 7. If it is, print the number and the text “Your number is a multiple of 7.” If it is not, print the number and the text “Your number is not a multiple of 7.”
cislo1 = int(input("Zadej libovolne cele cislo: "))
if cislo1 % 7 == 0:
    print(f"Zadane cislo {cislo1} je nasobek cisla 7")
else:
    print(f"Tvoje zadane cislo {cislo1} neni nasobek cisla 7")
print()

# Task 3
# The user types in two numbers. Find the maximum of two numbers and print it.
number1 = int(input("Zadej cele cislo: "))
number2 = int(input("Zadej cele cislo: "))
if number1 > number2:
    print(f"Maximum je {number1}")
else:
    print(f"Maximum je {number2}")
print()

# Task 4
# The user types in two numbers. Find the minimum of two numbers and print it.
number1 = int(input("Zadej cele cislo: "))
number2 = int(input("Zadej cele cislo: "))
if number1 < number2:
    print(f"Minimum je {number1}")
else:
    print(f"Minimum je {number2}")
print()

# Task 5
# The user types in two numbers. Based on the user’s choice, print the result of the sum, difference, product of these num- bers or their arithmetic mean.
number1 = int(input("Zadej cele cislo: "))
number2 = int(input("Zadej cele cislo: "))
volba = int(input("Zadej svoji volbu: 1 pro sumu, 2 pro rozdil, 3 pro soucin, 4 pro podil, 5 pro prumer: "))
if volba == 1:
    print(f"Soucet cisel: {number1 + number2}")
elif volba == 2:
    print(f"Rozdil cisel je: {number1 - number2}")
elif volba == 3:
    print(f"Soucin cisel je: {number1 * number2}")
elif volba == 4:
    print(f"Podil cisel je {(number1 / number2)}")
elif volba == 5:
    print(f"Prumer cisel je: {(number1 + number2)/2}")
else:
    print("Spatne zadana volba, priste vyber 1 az 4.")
print()




# operatory and, not, or
# A .. True  /  not A ... False 
# B .. False / not B ... True
# not bool(5) ... False
# not False ... True
# not True ... False

vek = 50
if vek > 10 and vek < 20 or vek > 50 or vek < 60:
    print("prosel jsi testem")
else: 
    print("spatny vek")

# priorita vyhodnoceni 1. >, 2. and, 3. or - pokud si nejsem jisty, tak to ozavorkuji
# if ((vek > 10) and (vek < 20)) or ((vek > 50) and (vek < 60))
# if (10 < vek < 20) or (50 < vek < 60):