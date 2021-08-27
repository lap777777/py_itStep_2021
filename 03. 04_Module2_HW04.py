# Task 1
# The user types in two numbers (start and end points of the range). Analyze all the numbers in this range as follows: if the number is a multiple of 7, print it.
number1 = int(input("Zadej zacatek rozsahu (cele cislo): "))
number2 = int(input("Zadej konec rozsahu (cele cislo): "))
print()
for i in range(number1, number2 + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()
print()

# Task 2
# The user types in two numbers (start and end points of the range). Analyze all the numbers in this range. Print the following:
#   1. All numbers in the range;
#   2. All numbers in the range in descending order; 
#   3. All numbers that are multiples of 7;
#   4. How many numbers are multiples of 5.
number1 = int(input("Zadej zacatek rozsahu (cele cislo): "))
number2 = int(input("Zadej konec rozsahu (cele cislo): "))
print("1.")
for i in range(number1, number2 + 1):
    print(i, end=" ")
print()
print()
print("2.")
for i in range(number2, number1 - 1, -1):
    print(i, end=" ")
print()
print()
print("3.")
for i in range(number1, number2 + 1):
    if i % 7 == 0:
        print(i, end=" ")
print()
print()
count = 0
for i in range(number1, number2 + 1):
    if i % 5 == 0:
        count += 1
print(f"V zadanem range je {count} nasobku cisla 5.")
print()

# Task 3
# The user types in two numbers (start and end points of the range). Analyze all the numbers in this range. The output should be according to the rules specified below.
# If the number is a multiple of 3 (divisible by 3 without remainder), print the word Fizz. If it is a multiple of 5, print Buzz. If it is a multiple of 3 and 5, print Fizz Buzz. If the number is not a multiple of 3 or 5, print the number itself.
number1 = int(input("Zadej zacatek rozsahu (cele cislo): "))
number2 = int(input("Zadej konec rozsahu (cele cislo): "))
for i in range(number1, number2 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
print()
