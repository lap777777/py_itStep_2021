# Task 1
# Two lists of integers are filled with random numbers. Do the following:
import random
list1 = []
for i in range(10):
    list1.append(random.randint(1, 100))
list2 = []
for i in range(10):
    list2.append(random.randint(1,100))
print(list1)
print(list2)
print()

#  Create the third list containing elements of both lists;
list3 = list1 + list2
print(list3)
print()

#  Create the third list containing elements of both lists without repetitions;
list4 = []
for i in list1:
    if i not in list4:
        list4.append(i)
    for y in list2:
        if y not in list4:
            list4.append(y)
    list4.sort()
print(list4)
print("----------------------------alternativa-----------------------------------")
list5 = []
list5 = list(set(list1) | set(list2))
list5.sort()
print(list5)
print()

#  Create the third list containing elements common to both lists;
list6 = []
for i in list1:
    for y in list2:
        if i == y:
            list6.append(i)
print(list6)
print()

#  Create the third list containing elements that are unique to each list;
#  kde je prunik, tak to vyhotim uplne pryc (repetition znamena, ze je ve dvou a dam jenom jednou a unique je, ze pokud je ve dvou, tak uplne vyhodim pryc)
list8 = list1[:]
for y in list2:
    if y in list8:
        list8.remove(y)
    else:
        list8.append(y)
list8.sort()
print(list8)
print()

#  Create the third list containing only the smallest and the largest values of each list.
list7 = []
list7.append(min(list1))
list7.append(max(list1))
list7.append(min(list2))
list7.append(max(list2))
print(list7)
print()
