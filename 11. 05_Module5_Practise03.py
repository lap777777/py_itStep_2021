# Task 1
# You have a list of 10 elements populated with random numbers. Find a number input by a user. Use the linear search algorithm.

import random

print("1---------------------------------------------------")
def find_number1(list, number):
    for i in list:
        if i == number:
            return True
    return False

while True:
    number = (input("Zadej libovolne cislo od 1 do 100: "))
    if  number.isdigit():
        number = int(number)
        break
    else:
        print("Nebylo zadano cislo.")

my_list = [] 
for i in range(20):
    my_list.append(random.randint(1, 100))
print(my_list)

print(find_number1(my_list, number))
print()

print("2---------------------------------------------------")
# Task 2
# You have a list of 10 elements populated with random numbers. Find a number input by a user. Use the binary search algorithm.

def find_number2(list, number):
    low = 0
    high = len(list)
    if number < list[low] or number > list[high-1]:
        return False
    while low <= high:
        print(list[low:high])
        middle = low + (high - low) // 2
        print(middle)
        if number == list[middle]:
            return True
        elif number < list[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return False

while True:
    number = (input("Zadej libovolne cislo od 1 do 100: "))
    if  number.isdigit():
        number = int(number)
        break
    else:
        print("Nebylo zadano cislo.")

my_list = [] 
for i in range(19):
    my_list.append(random.randint(1, 100))
my_list.sort()

print(find_number2(my_list, number))
print()

print("Alternativa-Binarni_deleni------------------------------")

def binary_search(list1, item_to_search):
    '''
    This is "docstring" - dokumentacni popisek.
    Searches for item in list.
    Returns True if present, False if absent.
    '''
    low = 0
    high = len(list1) - 1 
    # divam se pouze na prvky v seznamu a tak vyhodi prvky mimo seznam)
    while True:
        mid_index = (high + low) // 2
        mid_item = list1[mid_index]
        if item_to_search > mid_item:
            low = mid_index + 1
        elif item_to_search < mid_item:
            high - mid_index - 1
        elif item_to_search == mid_item:
            return True
    return False

# assert - pro testy - predpokladam, ze neco je pravda, pokud ne, tak vyhodi chybovou hlasku, kterou si zadam
assert binary_search([1,2,3,4,5],1) == True, "1 working incorrectly"
assert binary_search([1,2,3,4,5],2) == True, "2 working incorrectly"
assert binary_search([1,2,3,4,5],3) == True, "3 working incorrectly"
assert binary_search([1,2,3,4,5],4) == True, "4 working incorrectly"
assert binary_search([1,2,3,4,5],5) == True, "5 working incorrectly"
assert binary_search([1,2,3,4,5],2.5) == False, "2.5 working incorrectly"
assert binary_search([1,2,3,4,5],0) == False, "0 working incorrectly"
assert binary_search([1,2,3,4,5],8) == False, "8 working incorrectly"

"""
assert True, "True will never raise an error"
assert False, "False will raise - vyhodi chybu"
raise IndexError    # tohle vyhodi index error
"""
print(binary_search.__doc__)   # vola docstring
