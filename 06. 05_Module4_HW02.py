print("1---------------------------------------------------------------")
# Task 1
# Write a function that calculates the product of the elements from a list of integers. The list is passed as a parameter. The result is returned from the function.

def product(list):
    product = 1
    for i in list:
        product *= i
    return f"soucin zadanych cisel je: {product:_d}"

print(product([1, 2, 3, 4]))
print(product([1, 10, 100, 1000]))


print("2---------------------------------------------------------------")
# Task 2
# Write a function to find the minimum in a list of integers. The list is passed as a parameter. The result is returned from the function.

def my_min(list):
    my_min = 10000000000000000000000000000000000000000000000000000000000000
    for i in list:
        if i < my_min:
            my_min = i
    return f"Minimum je {my_min}"

print(my_min([1, 2, 3, 4, 5]))
print(my_min([100, 20, 30, 50, 60]))


print("3---------------------------------------------------------------")
# Task 3
# Write a function that determines how many prime numbers there are in the list of integers. The list is passed as a parameter. The result is returned from the function.

def no_prime_numbers(list):
    prime = 0
    for i in list:
        my_list = []
        for j in range(2, i):
            if i % j == 0:
                my_list.append(0)
            else:
                my_list.append(1)
        if 0 not in my_list:
            prime += 1
    return f"Pocet prvocisel v seznamu je: {prime}"

print(no_prime_numbers([3, 4, 5, 6, 7, 13, 15, 17, 19, 22, 23]))

print("4---------------------------------------------------------------")
# Task 4
# Write a function that removes a given number from the list of integers. Return the number of removed elements from the function.

def list_remove(number, list):
    list.remove(number)
    return list

print(list_remove(10, [10, 12, 14, 16, 18]))
print(list_remove(12, [10, 12, 14, 16, 18]))
print(list_remove(14, [10, 12, 14, 16, 18]))

print("5---------------------------------------------------------------")
# Task 5
# Write a function that takes two lists as a parameter and returns a list containing the elements of both lists.

def list_union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    list3 = list(set1 | set2)
    return list3

print(list_union([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))

print("6---------------------------------------------------------------")
# Task 6
# Write a function that calculates the power of each element from the list of integers. A value for the power is passed as a parameter, the list is also passed as a parameter. The function returns a new list containing the results.

def list_power(power, list):
    my_list = [i**power for i in list]
    return my_list

print(list_power(3, [2, 3, 4, 5, 6, 7]))