# Task 1
# Calculate the following in a list filled with random numbers:
my_list = [-1, -3, 45, 35, 22, 444, 56, 5, -85, 4, 3, -10, 20, 10, -56]

# a) sum of negative numbers:
my_sum = 0
for i in my_list:
    if i < 0:
        my_sum += i
print(my_list)
print(f"Suma negativnich cisel: {my_sum:_d}")
print("-------pocet-------------")
my_sum = sum(i < 0 for i in my_list)
print(f"Pcet negativnich cisel: {my_sum:_d}")
print()

# b) sum of even (sude) numbers:
my_sum = 0
for i in my_list:
    if i % 2 == 0:
        my_sum += i
print(f"Suma sudych cisel ze seznamu: {my_sum:_d}")
print()

# c) sum of odd numbbers
my_sum = 0
for i in my_list:
    if i % 2 != 0:
        my_sum += i
print(f"Soucet lichych cisel ze seznamu: {my_sum:_d}")
print()

# d) product of elements with indices divisible by 3:
my_product = 1
for i in my_list:
    if i % 3 == 0:
        my_product *= i
print(f"Soucin cisel ze seznamu s indexem delitelnym 3: {my_product:_d}")
print()

# e) product of elements between the smallest and the largest
print("Varianta 1 - ciselne")
my_list = [-1, -3, 45, 35, 22, 444, 56, 5, -85, 4, 3, -10, 20, 10, -56]
my_list1 = my_list[:]
my_list2 = my_list1.remove(max(my_list1))
my_list3 = my_list1.remove(min(my_list1))
result = 1
for i in my_list1:
    result *= i
print(f"Soucin: {result:_d}")
print("-------------------------")
print("Varianta 2 - rozdil pozicni")
my_list = [-1, -3, 45, 35, 22, 444, 56, 5, -85, 4, 3, -10, 20, 10, -56]
smallest = my_list.index(max(my_list))
largest = my_list.index(min(my_list))
if smallest < largest:
    new_list = my_list[smallest+1 : largest]  # beru jenom cisla mezi, takze spodni + 1 a horni bez +1
else:
    new_list = my_list[largest+1 : smallest]
result = 1
for i in new_list:
    result *= i
print(f"Vysledek soucinu: {result:_d}")
print()

# f) The sum of the elements between the first and the last positive elements.
my_list = [-1, -3, 45, 35, 22, 444, 56, 5, -85, 4, 3, -10, 20, 10, -56]
first = -1
last = -1
for i in range(len(my_list)):
    if my_list[i] >= 0:
        first = i
        break
for i in range(len(my_list)-1, -1, -1):
    if my_list[i] >= 0:
        last = i
        break
print(f"Suma prvku mezi kladnymi: {sum(my_list[first+1 : last])}") # bez tech hranic
print(f"Suma vcetne hranic: {sum(my_list[first : last+1])}")
print()
print("------------------------------------------------")
print()

# Task 2
# There is a list of integers filled with random numbers. Do the following based on this data:
import random
my_list = []
for i in range(10):
    my_list.append(random.randint(-100, 100))
print(my_list)

#   ■ Create a list of integers containing only even numbers;
my_list1 = []
for i in my_list:
    if i % 2 == 0:
        my_list1.append(i)
print(f"sude: {my_list1}")

#   ■ Create a list of integers containing only odd numbers;
my_list2 = []
for i in my_list:
    if i % 2 != 0:
        my_list2.append(i)
print(f"liche: {my_list2}")

#   ■ Create a list of integers containing only negative numbers; 
my_list3 = []
for i in my_list:
    if i < 0:
        my_list3.append(i)
print(f"zaporne: {my_list3}")

#   ■ Create a list of integers containing only positive numbers.
my_list4 = []
for i in my_list:
    if i > 0:
        my_list4.append(i)
print(f"kladne: {my_list4}")
print()
