# Task 1
# The user types in two numbers. Find the sum and average of numbers in the specified range.

number1 = int(input("Zadej cislo1: "))
number2 = int(input("Zadej cislo2: "))

my_sum = 0
my_count = 0
if number1 < number2:
    for i in range(number1, number2 + 1):
        my_sum += i
        my_count += 1
else: 
    for i in range(number2, number1 + 1):
        my_sum += i
        my_count += 1
print(f"Soucet vsech cisel je: {my_sum}")
print(f"Prumer vsech cisel je: {my_sum/my_count:,.2f}")
print()

# Task 2
# The user types in a number. Calculate the factorial of a number. Calculate the factorial of a number. For instance, if the user typed in 3, the factorial is 1*2*3 = 6. The formula for calculating the factorial: n! = 1*2*3*...*n, where n is the user defined number
number = int(input("Zadej cislo pro vypocet faktorialu: "))
my_factorial = 1
for i in range(1, number + 1):   # musim si tady zadat 1 pro zacatek, pokud bych nechal range(number1+1), tak bych dostaval porad 0, protoze cyklus for zacina od 0.
    my_factorial *= i
print(f"Faktorial cisla {number} je: {my_factorial:_d}")
print("----pomoci_while------")
result = 1
while number:
    result = result * number
    number = number - 1
print(f"Faktorial cisla {number} je: {result}.")
print()

# Task 3 
# The user types in the line lenght. Print a horizontal line made out of * of the specified lentht. For instance, if the typed in number is 7, the output will be as follows *******.
number = int(input("Zadej cislo pro pocet hvezdicek: "))
for i in range(1, number + 1):
    print("*", end="")
print()
# varianta udelat trojuhlenik s poctem hvezdicek
for i in range(number + 1):
    for j in range(1, i + 1):    # pro vnitrni cyklus nastavim pocet opakovani podle prvniho cyklu
        print("*", end="")
    print()
print()
# varianta trojuhlenik bez vnoreneho cyklu s retezcem
my_string = ""
for i in range(number + 1):
    my_string = my_string + "*"
    print(my_string)
print()

# Task 4
# The user types in the lenght of a line and a symbol to fill the line. Print a horizontal line made out of the typed in symbel o the specified lenght. If the typed in number and symbol are 5 and %, the output will be as follows
number = int(input("Zadej cislo pro pocet opakovani: "))
symbol = input("Zadej symbol: ")
for i in range(1, number + 1):
    print(symbol, end="")
print()