# Task 1
# The user types in three numbers. The program prints the sum or product of these numbers based on the user’s choice.
number1 = int(input("Zadej prvni cislo: "))
number2 = int(input("Zadej druhe cislo: "))
number3 = int(input("Zadej treti cislo: "))

choice = int(input("Zadej svoji volbu (1 pro nasobeni, 2 pro scitani): "))

if choice == 1:
    print("____nasobim_____")
    print(f"Vysledek nasobeni: {number1 * number2 * number3}")
elif choice == 2:
    print("____scitam_____")
    print(f"Vysledek scitani: {number1 + number2 + number3}")
else:
    print("chybne zadani, musis napsat 1 nebo 2.")
print()


# Task 2
# The user types in three numbers. Based on the user’s choice, the program prints a maximum of three, a minimum of three, or arithmetic mean of three numbers.
number1 = int(input("Zadej prvni cislo: "))
number2 = int(input("Zadej druhe cislo: "))
number3 = int(input("Zadej treti cislo: "))

choice = int(input("Zadej svoji volbu (1 pro maximum, 2 pro minimum, 3 pro prumer): "))

if choice == 1:
    print(f"Maximum je: {max(number1,number2,number3)}")
elif choice == 2:
    print(f"Minimum je: {min(number1,number2,number3)}")
elif choice == 3:
    print(f"Prumer je: {(number1 + number2 + number3)/3}")
else:
    print("chybne zadani, musis napsat 1 nebo 2.")
print()

# Task 3
# The user types in the number of meters. Based on the user’s choice, the program converts meters to miles, inches, or yards.
meters = int(input("Zadej delku v metrech: "))
choice = int(input("Zadej cislo (1 prevod na miles, 2 prevod na inches, 3 prevod na yards): "))

if choice == 1:
    miles = meters / 1609.34
    print(f"{meters} metru je {miles:,.2f} mili.")
elif choice == 2:
    inches = meters * 39.37
    print(f"{meters} metru je {inches:,.2f} palcu.")
elif choice == 3:
    yards = meters * 1.0936
    print(f"{meters} metru je {yards:,.2f} yardu.")
else:
    print("Chybne zadani.")
print()

