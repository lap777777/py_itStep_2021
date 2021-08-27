# Task 1
# Write a program that requests two integers x and y, and then calculates and prints the value of x raised to the power of y.
x = int(input("Zadej cislo x: "))
y = int(input("Zadej cislo y: "))
power_x = x ** y
print(f"mocnina y z cisla x: {power_x:_d}")
print()

# Task 2
# Count the number of integers in the range from 100 to 999 that have two identical digits.
x1 = 100
x2 = 999
a1 = 1
a2 = 2
a3 = 3
count = 0
for i in range(x1, x2 + 1):
    a1 = i // 100
    a2 = i % 100 // 10
    a3 = i % 100 % 10
    if a1 == a2 or a1 == a3 or a2 == a3:
        count += 1
print(f"Pocet cisel, ktere maji 2 stejne cislice: {count}.")
print()


# Task 3
# Count the number of integers in the range from 100 to 9999 that have different digits.
x1 = 100
x2 = 9999
a1 = 0
a2 = 0
a3 = 0
a4 = 0
count = 0
for i in range(x1, x2 + 1):
    a1 = i // 1000
    a2 = i % 1000 // 100
    a3 = i % 1000 % 100 // 10
    a4 = i * 1000 % 100 % 10
    if a1 != a2 and a1 != a3 and a1 != a4 and a2 != a3 and a2 != a4 and a3 != a4:
        count += 1
print(f"Pocet cisel, ktere maji ruzne cislice: {count}.")
print()


# Task 4
# The user types in an integer value. Remove all 3s and 6s from this integer and print it.
number = int(input("Zadej jakekoliv cele cislo: "))
my_len = len(str(number))
final = ""
for i in range(my_len):
    number = str(number)
    if number[i] == "3" or number[i] == "6":
        final = final
    else:
        final = final + number[i]
number = int(number)
final = int(final)
print(f"Zadane cislo: {number}")
print(f"Upravene cislo: {final}")
print()