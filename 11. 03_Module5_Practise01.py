print("1------------------------------------------------")
# Task 1
# Write a program that sorts a list of integers using bubble sort.
# bubble sort - kvadarticka casova slozitost - n * n = n**2 - prochazim dva cykly:
def bubble_sort(list):
    my_len = len(list)
    for i in range(my_len-1):
    # Traverse through all list elements
    # range(n) also work but outer loop will repeat one time more than needed.
        for j in range(my_len-i-1):
        # Last i elements are already in place
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if list[j] > list [j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

my_list = [2, 11, 50, 1, 4, 16, 6, 20, 3, 56, 8, 14, 5, 10]
print(my_list)
print(bubble_sort(my_list))

print("2------------------------------------------------")
# Task 2
# Write a program that sorts a list of integers using insertion sort.
# 
def insertion_sort(list):
    for i in my_list:
        j = my_list.index(i)
        print(j)
        while j>0:
            if my_list[j-1] > my_list[j]:
                my_list[j-1],my_list[j] = my_list[j], my_list[j-1]
            else:
                break
            j = j-1
    return list

my_list = [2, 11, 50, 1, 4, 16, 6, 20, 3, 56, 8, 14, 5, 10]
print(my_list)
print(insertion_sort(my_list))

print("3------------------------------------------------")
# Task 3
# You have a list of integers. Sort the first half of the list in descending order, and the second in ascending order.
middle = len(my_list) // 2
my_list1 = my_list[:middle]
my_list2 = my_list[middle:]
my_list1.sort()
my_list2.sort(reverse=True)
my_list3 = my_list1 + my_list2
print(my_list3)

print("4------------------------------------------------")
# Task 4
# Write a program that sorts a list of integers using merge sort.


print("5------------------------------------------------")
# Task 5
# selection sort
def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        # prochazime cele pole
        for j in range(i+1, len(list)):
            # projedeme zbyvajici prvky pole (protoze i+1)
            if(list[min_index] > list[j]):
                # nalezli jsme nejmensi prvek, tak si ulozime jeho index
                min_index = j
        # prohodime prvek z prvniho iteracniho cyklu s nejmensim nalezenym
        list[i], list[min_index] = list[min_index], list[i]
    return list

my_list = [2, 11, 50, 1, 4, 16, 6, 20, 3, 56, 8, 14, 5, 10]
print(my_list)
print(selection_sort(my_list))
print()


