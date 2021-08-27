# Task 1
# You have three tuples of integers. Find elements present in all tuples.
tuple1 = (10, 5, 4, 3, 8, 9, 7)
tuple2 = (1, 2, 3, 4, 5, 6, 7, 11)
tuple3 = (5, 9, 4, 3, 10, 15)

my_list = []
my_list1 = []

for i in tuple1:
    if i in tuple2:
        my_list.append(i)

for i in tuple3:
    if i in my_list:
        my_list1.append(i)
my_list1 = tuple(my_list1)
print(my_list1)
print()

print("-------------------------------------------------------------")

# Task 2
# You have three tuples of integers. Find elements unique for each list.
tuple1 = (10, 5, 4, 3, 8, 9, 7, 1)
tuple2 = (1, 2, 4, 3, 5, 6, 7, 11)
tuple3 = (5, 9, 4, 3, 10, 15, 13)

my_tuple1 = []
my_tuple2 = []
my_tuple3 = []

for i in tuple1:
    if i not in tuple2 and i not in tuple3:
        my_tuple1.append(i)
for i in tuple2:
    if i not in tuple1 and i not in tuple3:
        my_tuple2.append(i)
for i in tuple3:
    if i not in tuple2 and i not in tuple1:
        my_tuple3.append(i)

print(f"Jedinecne prvky v prvnim setu: {tuple(my_tuple1)}")
print(f"Jedinecne prvky v druhem setu: {tuple(my_tuple2)}")
print(f"Jedinecne prvky v tretim setu: {tuple(my_tuple3)}")
print()

print("-------------------------------------------------------------")

# Task3
# You have three tuples of integers. Find elements that are present in each tuple and at the same position in each tuple.
tuple1 = (1, 5, 4, 3, 8, 9, 7, 10)
tuple2 = (1, 2, 4, 3, 5, 6, 7, 11)
tuple3 = (5, 9, 4, 3, 10, 15, 13, 7)

my_list = []

for i in range(len(tuple1)):
    if tuple1[i] == tuple2[i] and tuple1[i] == tuple3[i]:
        my_list.append(tuple1[i])

print(f"Stejny prvek na stejnem miste ve vsech tuple: {my_list}.")
print()

print("-------------------------------------------------------------")
