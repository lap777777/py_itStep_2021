# Task1
# Write a function that calculates the sum of elements from a list of integers. The list is passed as a parameter.

def my_sum(list):
    my_sum = sum(list)
    return my_sum

result = my_sum([1, 10, 20, 30, 40, 50])
print(f"Soucet je: {result}")
print()

# Task 2
# Write a function to find the maximum in the list of integers. The list is passed as a parameter.

def my_max(list):
    return max(list)

result = my_max([1, 10, 20, 30, 40, 50])
print(f"Maximum je: {result}")
print()

# Task 3
# Write a function that determines the number of even, odd, positive, negative elements in the list of integers. The list is passed as a parameter.

def pocitani(list):
    even = sum(i % 2 ==0 for i in list)
    odd = sum(i % 2 != 0 for i in list)
    positive = sum(i > 0 for i in list)
    negative = sum(i < 0 for i in list)
    # return [oven, odd, positive, negative] - pokud bych to chtel takto, tak udelam list
    # return {"sude": even, "liche": odd, "kladne": positive, "zaporne": negative} - nebo do slovniku si to muzu dat
    return {"sude": even, "liche": odd, "kladna": positive, "zaporna": negative}

print(pocitani([1, 2, 3, 4, -5, -6, -10, 5, 0]))
print()

# Task 4
# Write a function that flips the contents of the list of integers.

def flip(list):
    list1 = list[::-1]
    return list1

obraceny = flip([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(obraceny)
print()

# Task 5
# Write a function that searches for some number in the list of integers.

def is_number(number, list):
    if number in list:
        return True
    else:
        return False

print(is_number(1, [1, 2, 3, 4, 5, 6, 7,]))
print(is_number(10, [1, 2, 3, 4, 5, 6, 7,]))
print()

# Task 6
# Write a function that calculates the factorial of each element in the list of integers. The function returns a new list containing the resulting factorials.
import math

def factorial(list):
    my_list = []
    for i in list:
        print(f"Faktorial cisla {i} je: {math.factorial(i):_d}")
        my_list.append(math.factorial(i))
    print(my_list)


factorial([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print()

