# Task 1
# The user types in a string. Rotate the strings and display the result.
my_string = input("Zadejte retezec: ")
reverse_string = ""
for i in range(len(my_string)-1, -1, -1):
    reverse_string += my_string[i]
print(f"Obraceny retezec: {reverse_string}")
print()

# Task 2
# The user types in a string. Count the number of letters and digits in the string. Print both results.
my_string = input("Zadejte libovolny retezec obsahujici cisla, pismena a znaky: ")
digit = 0
letter = 0
other = 0
for i in my_string:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        digit += 1
    else:
        other +=1
print(f"Zadany retezec obsahuje {digit} cislic, {letter} pismen a {other} ostatnich znaku.")
print("______alternativa__________")
numbers = sum(c.isdigit() for c in my_string)
letters = sum(c.isalpha() for c in my_string)
others  = len(my_string) - numbers - letters 
print(f"Zadany retezec obsahuje {numbers} cislic, {letters} pismen a {others} ostatnich znaku.")
print()

# Task 3
# The user types in a string and a symbol to be searched for. Count how many times this symbol appears in the string. Print the result.
my_string = input("Zadej libovolny retezec: ")
my_letter = input("Zadej znak, ktery chces hledat: ")
my_count = 0
for i in my_string:
    if i == my_letter:
        my_count += 1
print(f"Hledany znak {my_letter} je v danem retezci {my_count}x.")
print()

# Task 4
# The user types in a string and a search word. Count how many times this word appears in the string. Print the result.
my_string = input("Zadej libovolny retezec - vety: ")
my_word = input("Zadej hledane slovo: ")
my_list = my_string.split()
my_count = 0
for i in my_list:
    if i == my_word:
        my_count += 1
print(f"Hledane slovo {my_word} je v danem retezci {my_count}x.")
print()

# Task 5
# The user types in a string, a search word, and a replacement word. Replace one word with another one in the string. Print the resulting string.
my_string = input("Zadej libovolny retezec: ")
old = input("Zadej slovo, ktere chces nahradit: ")
new = input("Zadej slovo, ktere ma nahradit puvodni slovo: ")
result = my_string.replace(old, new)
print(result)
print()
