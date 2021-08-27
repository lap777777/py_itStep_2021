# Task 1
# The user types in two numbers. Print all the numbers in the specified range
number1 = int(input("Zadej cislo1: "))
number2 = int(input("Zadej cislo2: "))
if number1 < number2:   
    for i in range(number1, number2 + 1):
        print(i)
else:
    for i in range(number2, number1 + 1):
        print(i)
print()

# Task 2
# The user types in two numbers. Print all odd numbers in the specified range.
number1 = int(input("Zadej cislo1: "))
number2 = int(input("Zadej cislo2: "))

if number1 % 2 == 0:
    number1 = number1 + 1
else:
    number1 = number1

for i in range(number1, number2 + 1, 2):
    print(i)
print()

# Task 3
# The user types in two numbers. Print all even numbers in the specified range.
number1 = int(input("Zadej cislo1: "))
number2 = int(input("Zadej cislo2: "))

if number1 < number2:
    for i in range(number1, number2 + 1):
        if i % 2 == 0:
            print(i)
else:
    for i in range(number2, number1 + 1):
        if i % 2 == 0:
            print(i)
print()

# Task 4
# The user types in two numbers. Print all numbers in the specified range in descending order
number1 = int(input("Zadej cislo1: "))
number2 = int(input("Zadej cislo2: "))

if number1 < number2:
    for i in range(number2, number1 - 1, -1):
        print(i)
else:
    for i in range(number1, number2 - 1, -1):
        print(i)
print()

# Task 5
# The user types in two numbers. Print all odd numbers in the specified range. If the end and start points of the range are incorrect, normalize them. Let`s say the user typed in 33 and 13, normalization will assingn 13 to the start and 33 to the end of the range.
number1 = int(input("Zadej cislo1: "))
number2 = int(input("Zadej cislo2: "))

if number1 < number2:
    for i in range(number1, number2 + 1):
        if i % 2 != 0:
            print(i)
else:
    for i in range(number2, number1 + 1):
        if i % 2 != 0:
            print(i)
print()