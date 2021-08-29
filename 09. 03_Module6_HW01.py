print("1-------------------------------------------------------------")
# Task 1
# You have three tuples of integers. Find elements present in all tuples.
tuple1 = (10, 5, 4, 3, 8, 9, 7)
tuple2 = (1, 2, 3, 4, 5, 6, 7, 11)
tuple3 = (5, 9, 4, 3, 10, 15)

my_tuple = tuple(set(tuple1) & set(tuple2) & set(tuple3))
print(my_tuple)
print("    ----------alternativa-listy-----------")

my_list = [i for i in tuple1 if i in tuple2]
my_list1 = [i for i in tuple3 if i in my_list]
my_tuple = tuple(my_list1)
print(my_tuple)
print()

print("2-------------------------------------------------------------")
# Task 2
# You have three tuples of integers. Find elements unique for each list.
tuple1 = (10, 5, 4, 3, 8, 9, 7, 1)
tuple2 = (1, 2, 4, 3, 5, 6, 7, 11)
tuple3 = (5, 9, 4, 3, 10, 15, 13)

my_tuple1 = tuple(set(tuple1)-set(tuple2)-set(tuple3))
my_tuple2 = tuple(set(tuple2)-set(tuple1)-set(tuple3))
my_tuple3 = tuple(set(tuple3)-set(tuple2)-set(tuple1))

print(my_tuple1)
print(my_tuple2)
print(my_tuple3)

print("    ----------alternativa-listy-----------")
my_tuple1 = tuple([i for i in tuple1 if i not in tuple2 and i not in tuple3])
my_tuple2 = tuple([i for i in tuple2 if i not in tuple1 and i not in tuple3])
my_tuple3 = tuple([i for i in tuple3 if i not in tuple2 and i not in tuple1])

print(f"Jedinecne prvky v prvnim setu: {my_tuple1}")
print(f"Jedinecne prvky v druhem setu: {my_tuple2}")
print(f"Jedinecne prvky v tretim setu: {my_tuple3}")
print()

print("-------------------------------------------------------------")

# Task3
# You have three tuples of integers. Find elements that are present in each tuple and at the same position in each tuple.
tuple1 = (1, 5, 4, 3, 8, 9, 7, 10)
tuple2 = (1, 2, 4, 3, 5, 6, 7, 11)
tuple3 = (5, 9, 4, 3, 10, 15, 13, 7)

my_list = [
    tuple1[i]
    for i in range(len(tuple1))
    if tuple1[i] == tuple2[i] and tuple1[i] == tuple3[i]
]

print(f"Stejny prvek na stejnem miste ve vsech tuple: {my_list}.")
print()

print("-------------------------------------------------------------")
