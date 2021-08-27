# Task 1
# The user types in two numbers. Find the sum of all even, odd numbers and multiples of 9 in the specified range, as well as arithmetic mean of each group.
number1 = int(input("Zadej zacatek rozsahu (cele cislo): "))
number2 = int(input("Zadej konec rozsahu (cele cislo): "))
sum1 = 0
sum2 = 0
sum3 = 0
count1 = 0
count2 = 0
count3 = 0
for i in range(number1, number2 + 1):
    if i % 2 == 0:
        sum1 += i
        count1 += 1
    else: 
        sum2 += i
        count2 += 1
for i in range(number1, number2 + 1):
    if i % 9 == 0:
        sum3 += i
        count3 += 1
print(f"Suma sudych cisel: {sum1}.")
print(f"Prumer sudych cisel: {sum1/count1}.")
print(f"Suma lichych cisel: {sum2}.")
print(f"Prumer lichych cisel: {sum2/count2}.")
print(f"Suma nasobku deviti: {sum3}.")
print(f"Prumer nasobku deviti: {sum3/count3}.")
print()


# Task 2
# The user types in the length of a line and a symbol to fill the line. Print a vertical line made out of the typed in symbol of the specified length.
# For instance, if the typed in number and symbol are 3 and %, the output will be as follows:
#   %
#   %
#   %
count = int(input("Zadej pocet znaku: "))
symbol = input("Zadej symbol: ")
for i in range(count):
    print(symbol)
print()


# Task 3
# The user types in numbers. If the number is greater than 0, print “Your number is positive”; if it is less than zero, print “Your number is negative”; if it is equal to 0, print “Your number is equal to zero.” When the user types in 7, the program stops and prints “Good bye!”
number = int(input("Zadej cislo (kladne, zaporne, 0): "))
while number != 7:
    if number < 0:
        print("Cislo je zaporne.")
    elif number > 0:
        print("Cislo je pozitivni.")
    elif number == 0:
        print("Cislo je rovno 0.")
    number = int(input("Zadej cislo: "))
print("Good bye.")
print()


# Task 4
# The user types in numbers. The program must calculate their sum and find the maximum and minimum. When the user types in 7, the program stops and prints “Good bye!”.
number1 = int(input("Zadej prvni cislo: "))
number2 = int(input("Zadej druhe cislo: "))
while number1 != 7 and number2 != 7:
    print(f"Suma zadanych cisel je: {number1 + number2}.")
    print(f"Max zadanych cisel je: {max(number1, number2)}.")
    print(f"Min zadanych cisel je: {min(number1, number2)}.")
    number1 = int(input("Zadej prvni cislo: "))
    number2 = int(input("Zadej druhe cislo: "))
print("Good bye.")
print()
