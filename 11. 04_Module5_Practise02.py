import random

print("1---------------------------------------------------------")
# Task 1
# Write a program that sorts a list of integers using Shell’s method.

my_list = [5, 7, 9, 15, 2, 11, 50, 1, 4, 16, 6, 20, 3, 56, 8, 14, 10]


print("2---------------------------------------------------------")
# Task 2
# Write a program that sorts a list of integers using the heap sort.


print("3---------------------------------------------------------")
# Task 3
# Write a program that sorts a list of integers using the quick sort.


print("4---------------------------------------------------------")
# Task 4
# You have a stack of pancakes different in radius. The only operation performed on them is this: put a spatula between two pancakes and swap the pancakes above the spatula. Sort the pancakes from the largest to the smallest bottom-up using as little operations as you can.

def pancakes(list):
    pos = random.randint(1, len(list)-2)
    print(list[pos])
    list1 = list[:pos]
    list1 = list1[::-1]
    list2 = list[pos:]
    list2.sort(reverse=True)
    list3 = list1 + list2
    return list3

my_list = [2, 3, 5, 8, 12, 15, 16, 35, 25, 18, 13, 29]
print(my_list)
print(pancakes(my_list))
