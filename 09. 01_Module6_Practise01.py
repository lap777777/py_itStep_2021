# Task 1
# The user inputs a fruit from the keyboard. Display the number of times this fruit occurs as an element.

fruit_dic = {}

while True:
    fruit = input("Zadejte ovoce: ")
    if fruit == "":
        break
    if fruit in fruit_dic:
        fruit_dic[fruit] += 1
    else:
        fruit_dic[fruit] = 1
print(fruit_dic)

print("-----alternativa--------------")

fruit_dic = {}

while True:
    fruit = input("Zadej ovoce: ")
    if not fruit:
        break
    fruit_dic[fruit] = fruit_dic.get(fruit,0) + 1
print(fruit_dic)

print("---------------------------------------------------------")

# Task 2
# Improve Task 1 by adding the possibility to calculate how many times this fruit occurs as a part of an element. Here, for example,
# banana, apple, bananamango, mango, strawberry-banana the word banana occurs three times.

my_string = input("Zadej retezec, obsahujici ovoce: ")
my_search = input("Zadej hledane slovo: ")

my_count = my_string.count(my_search)
print(f"Hledane slovo {my_search} se v zadanem retezci nachazi {my_count}x.")

print("---------------------------------------------------------")

# Task 3
# You have a tuple containing names of car manufacturers (a name may occur from 0 to N times). The user inputs a manufacturer and a replacement word. Replace all elements in the tuple with the replacement word. The match must be complete.

cars = ("volvo", "porsche", "vw", "renault", "volvo", "citroen", "volvo")
print(cars)
old_car = input("Zadej vyrobce ze seznamu: ")
new_car = input("Zadej nahradniho vyrobce: ")

car_string = " ".join(cars)
new_car_string = car_string.replace(old_car, new_car)
new_cars = tuple(new_car_string.split())
print(new_cars)

print("---------------------------------------------------------")

# Task 4
# You have a tuple of integers. Display statistics on the number of digits in tuple elements. For instance:
# One digit — 3 elements Two digits — 4 elements Three digits — 5 elements.

numbers = (1, 45, 2, 156, 35, 45, 135, 2, 5)
my_dic = {}
for i in numbers:
    if len(str(i)) == 1:
        my_dic["one_digit"] = my_dic.get("one_digit",0) + 1
    if len(str(i)) == 2:
        my_dic["two_digits"] = my_dic.get("two_digits",0) + 1
    if len(str(i)) == 3:
        my_dic["three_digits"] = my_dic.get("three_digits",0) + 1
for key, value in my_dic.items():
    print(f"{key}: {value} elements")

print("---------------------------------------------------------")
