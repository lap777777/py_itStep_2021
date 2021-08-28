print("1---------------------------------------------------------------")
# Task 1
# Write a function that prints formatted text given below:
#   “Don’t compare yourself with anyone in this world... 
#       if you do so, you are insulting yourself.”
#                                             Bill Gates
def print_quote():
    print('"Don`t compare yourself with anyone in this world...')
    print('    if you do so, your are insulting yourself."     ')
    print('                                          Bill Gates')

print_quote()

print("2---------------------------------------------------------------")
# Task 2
# Write a function that takes two numbers as a parameter and displays all even numbers in between.
def even_numbers(low, high):
    my_list = [i for i in range(low, high + 1) if i % 2 != 0]
    return my_list
    
low = int(input("Zadej dolni hranici rozsahu: "))
high = int(input("Zadej horni hranii rozsahu: "))
print(even_numbers(low, high))


print("3---------------------------------------------------------------")
# Task 3
# Write a function that prints an empty or solid square made out of some symbol. The function takes the following as parameters: the length of the side of the square, a symbol, and a boolean variable:
#   ■ if it is True, the square is solid; 
#   ■ if False, the square is empty.

def print_square(number, symbol, bool):
    if bool:
        for i in range(1, number + 1):
            print((symbol + " ") * number)
    else:
        for i in range(1, number + 1):
            if i == 1 or i == number:
                print((symbol + " ") * number)
            else:
                print(symbol + " " + "  " * (number - 2) + symbol)


number = int(input("Zadej delku strany: "))
symbol = input("Zadej znak: ")
my_bool = input("Zadej: True pro vypln, nic pro prazdny ctverec: ")

print_square(number, symbol, my_bool)


print("4---------------------------------------------------------------")
# Task 4
# Write a function that returns the smallest of five numbers. Numbers are passed as parameters.

def smallest_number(list):
    my_min = 10000000000000000000000000000000000000000000000000000000000000
    for i in list:
        if i < my_min:
            my_min = i
    return f"nejmensi zadane cislo je {my_min}"

my_list = []
for i in range(5):
    number = int(input(f"Zadej {i+1}. cislo: "))
    my_list.append(number)

print(smallest_number(my_list))


print("5---------------------------------------------------------------")
# Task 5
# Write a function that returns the product of numbers in a specified range. The start and end points of the range are passed as parameters. If the order of these points is incorrect (e.g., 5 is the end, and 25 is the start), swap them.

def product(low, high):
    if low < high:
        my_list = [i * i for i in range(low, high+1)]
        return my_list
    elif high < low:
        my_list = [i * i for i in range(high, low+1)]
        return my_list
    else:
        return low * high

low = int(input("Zadej dolni hranici: "))
high = int(input("Zadej horni hranici: "))

print(product(low, high))

print("6---------------------------------------------------------------")
# Task 6
# Write a function that counts how many digits a number has. The number is passed as a parameter. Return the received number of digits from the function. For example, if the passed number is 3456, it has 4 digits.

def no_digits(number):
    number = str(number)
    my_len = len(number)
    return f"delka zadaneho cisla je: {my_len}"

number = int(input("Zadej libovolne cislo: "))

print(no_digits(number))

print("7---------------------------------------------------------------")
# Task 7
# Write a function that checks if a number is a palindrome. The number is passed as a parameter. If the number is a palindrome, return true, otherwise false.
# A palindrome is a number which reads the same backward as forward. For instance, 123321 is a palindrome, 546645 is a palindrome, but 421987 is not.

def palindrome(number):
    my_list = list(str(number))
    my_len = len(my_list)
    middle = my_len//2
    l1 = my_list[:middle]
    l2 = my_list[middle:]
    l3 = l2[::-1]
    if l1 == l3:
        return f"Zadane cislo {number} je palindrome."
    else:
        return f"Zadane cislo {number} neni palindrome."

number = int(input("Zadej libovolne cislo: "))

print(palindrome(number))
