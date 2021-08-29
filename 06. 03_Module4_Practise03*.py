# Task 1
# Write a recursive function to find the power of a number.
def my_power(number):
    return number ** 2

print(my_power(2))
print(my_power(4))
print(my_power(6))
print("-----------------------------------------------------------------------")

# Task 2
# Write a recursive function that calculates the sum of all numbers in the range from a to b. The user types in a and b. Illustrate how the function works with an example.
def my_sum(number1, number2):
    my_sum = 0
    if number1 < number2:
        for i in range(number1, number2 + 1):
            my_sum += i
    elif number2 > number1:
        for i in range(number2, number1 + 1):
            my_sum += 1
    else:
        print("Musis zadat dve cisla, ktera si nejsou rovna.")
    return my_sum

print(my_sum(1, 4))
print(my_sum(10, 20))
a = int(input("Zadej prvni cislo: "))
b = int(input("Zadej druhe cislo:  "))
print(my_sum(a, b))
print("-----------------------------------------------------------------------")

# Task 3
# Write a recursive function that prints N asterisks in a row, N is set by the user. Illustrate how the function works with an example.
def asterix(number):
    print("*"*number, end="")
    print()

number = int(input("Zadej pocet opakovani: "))
asterix(number)
print("-----------------------------------------------------------------------")

# Task 4
# Develop a game of Tic-tac-toe.


print("-----------------------------------------------------------------------")
# Task 5
# Write a recursive function that takes a list of 100 random integers and finds the position at which a sequence of 10 numbers begins, and their sum must be the smallest.


print("-----------------------------------------------------------------------")
# Task 6
# Write a function that takes two dates (i.e., the function takes six parameters) and calculates the difference in days between those dates. To solve this problem, you should also write a function that checks if the year is a leap year.

print("-----------------------------------------------------------------------")




