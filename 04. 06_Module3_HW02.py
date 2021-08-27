# Task 1
# The user types in an arithmetic expression. For example, 23+12.
# Print its result. In our example, the output is 35. The arith- metic expression can have only three parts: number, operation, number. Possible operations: +, -, *, /.
my_string = input("Zadej aritmeticky vyraz bez mezer pro +, -, *, / (napr. 23+12, 50/10): ")
my_list = []
result = 0
for i in my_string:
    if i == "+":
        my_list = my_string.split("+")
        result = int(my_list[0]) + int(my_list[1])
    elif i == "-":
        my_list = my_string.split("-")
        result = int(my_list[0]) - int(my_list[1])
    elif i == "*":
        my_list = my_string.split("*")
        result = int(my_list[0]) * int(my_list[1])
    elif i == "/":
        my_list = my_string.split("/")
        result = int(my_list[0]) / int(my_list[1])
print(f"Vysledek operace {my_string} je {result}.")
print()

# Task 2
# You have a list of integers filled with random numbers. Find the largest and the smallest elements, count negative and positive elements, as well as zeros. Print the results.
import random
my_list = []
for i in range(20):
    my_list.append(random.randint(-20, 20))
print(my_list)
print(f"Minimum je: {min(my_list)}")
print(f"Maximum je: {max(my_list)}")
neg_count = sum(i < 0 for i in my_list)
pos_count = sum(i > 0 for i in my_list )
zero_count = sum(i == 0 for i in my_list)

print(f"Pocet negativnich cisel je: {neg_count}")
print(f"Pocet pozitivnich cisel je: {pos_count}")
print(f"Pocet nul je: {zero_count}")
print()




