# Task 1
# The user types in a six-digit number. Write a program that determines if this number is lucky. (A lucky number is a six-digit number with the sum of its first three digits being equal to the sum of its last three digits.)
# For example, 123321 is a lucky number because 1+2+3 = 3+2+1.
# But 378423 is not a lucky number because 3+7+8 != 4+2+3. If the user typed in a non-six-digit number, display an error message.
number = (input("Zadej sesticiferne cislo: "))
if len(number) == 6:
    number = int(number)
    prvni = number // 100_000
    druhe = number % 100_000 // 10_000
    treti = number % 100_000 % 10_000 // 1000
    ctvrte = number % 100_000 % 10_000 % 1000 // 100
    pate = number % 100_000 % 10_000 % 1000 % 100 // 10
    seste = number % 100_000 % 10_000 % 1000 % 100 % 10
    if (prvni + druhe + treti) == (ctvrte + pate + seste):
        print(f"Cislo {number} je lucky number")
    else:
        print(f"Cislo {number} neni lucky number")
    print()
else:
    print("Chyba, zadej sesticiferne cislo.")
print()


# Task 2
# The user types in a six-digit number. Swap the first and the sixth digits, as well as the second and the fifth.
# For instance, 723895 should become 593827.
# If the user typed in a non-six-digit number, display an error message.
number = (input("Zadej sesticiferne cislo: "))
if len(number) == 6:
    number = int(number)
    prvni = number // 100_000
    druhe = number % 100_000 // 10_000
    treti = number % 100_000 % 10_000 // 1000
    ctvrte = number % 100_000 % 10_000 % 1000 // 100
    pate = number % 100_000 % 10_000 % 1000 % 100 // 10
    seste = number % 100_000 % 10_000 % 1000 % 100 % 10
    number1 = seste*100_000 + pate*10_000 + ctvrte*1000 + treti*100 + druhe*10 + prvni
    print(f"Cislo {number} je obracene {number1}")
else:
    print("Chyba, zadej sesticiferne cislo.")
print()


# Task 3
# The user types in a number of the month (from 1 to 12). Based on the typed in number, the program displays one of the following: Winter if the number is 1, 2, or 12, Spring if the number is in the range from 3 to 5, Summer if from 6 to 8, Autumn if from 9 to 11.
# If the number is out of the range, display an error message.
number = int(input("Zadej cislo pro mesic (1 - leden, 12 - prosinec): "))
if number == 12 or number == 1 or number == 2:
    print(f"Zima")
elif number <= 5:
    print("Jaro")
elif number <= 8:
    print("Leto")
elif number <= 11:
    print("Podzim")
else:
    print("Chybne zadani")
print()
