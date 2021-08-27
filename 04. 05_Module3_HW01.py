# Task 1
# The user types in a string. Check if this string is a palinDodrome. A palindrome is a word or text that reads the same backward as forward. For instance, racecar; “Do geese see God?”; tenet; “Was it a car or a cat I saw?” . . . . . . . . . . . . . .
s = input("Zadej libovolny retezec: ")
s1 = s.rstrip("!.?")
s2 = s1.lower()
l = s2.split()
s3 = ""
for i in l:
    s3 += i
s4 = s3[::-1]
if s4 == s3:
    print(f"Retezec '{s}' je palindrom.")
else:
    print(f"Retezec '{s}' neni palindrom.")
print()

# Task 2
# The user types in text followed by a list of reserved words. Find all reserved words in the text and change lowercase to uppercase there. Print the modified text.
my_string = input("Zadej libovolny retezec: ")
my_string = my_string.rstrip(".,!?")
my_list = []
while i != "x":
    i = (input("Zadej libovolne slovo (pro ukonceni zadej x): "))
    if i == "x":
        break
    my_list.append(i)
my_list1 = my_string.split()
my_list2 = [slovo.upper() if slovo in my_list else slovo for slovo in my_list1]    # list comprehension
my_string1 = " ".join(my_list2)
print(my_string1)
print()

# Task 3
# There is some text. Count the number of sentences in it and print the result.
my_string = "Sel do lesa. Trhal jahody. Nasel boruvky. Potkal medveda. Sel domu."
my_count = 0
for i in my_string:
    if i == ".":
        my_count += 1
print(f"Retezec obsahuje {my_count} vet.")
print("----alternativa-----------")
my_count = sum(i == "." for i in my_string)
print(f"Retezec obsahuje {my_count} vet.")
print()

