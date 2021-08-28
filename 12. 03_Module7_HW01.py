print("1----------------------------------------------------")
# Task 1
# You have two text files. Find out if their lines match. If they don’t, print the mismatched line from each file.

with open("12_Lekce_zzz/task1.txt") as f1, open("12_Lekce_zzz/task1b.txt") as f2:
    my_list1 = [line.rstrip("\n") for line in f1]
    my_list2 = [line.rstrip("\n") for line in f2]
    my_len = len(my_list1)
    for i in range(my_len):
        if my_list1[i] != my_list2[i]:
            print(f"prvni soubor: {my_list1[i]}, druhy soubor: {my_list2[i]}")


print("2----------------------------------------------------")
#Task 2
#You have a text file. Create a new file and write the following statistics based on the source file to it:
#   ■ Number of characters; 
#   ■ Number of lines;
#   ■ Number of vowels;
#   ■ Number of consonants; 
#   ■ Number of digits.

my_str = ""
no_lines = 0
no_char = 0
no_vowels = 0
no_digits = 0
with open("12_Lekce_zzz/text.txt", encoding="utf-8") as f1:
    for line in f1:
        no_lines += 1
        my_str += line
for i in my_str:
    if i.isdigit():
        no_digits += 1
    if i.isalpha():
        no_char +=1
    if i in "aeiouAEIOU":
        no_vowels +=1
no_consonants = no_char - no_vowels

with open("12_Lekce_zzz/text_copy.txt", "w", encoding="utf-8") as f1:
    f1.write(f"Pocet znaku: {no_char}\n")
    f1.write(f"Pocet radku: {no_lines}\n")
    f1.write(f"Pocet samohlasek: {no_vowels}\n")
    f1.write(f"Pocet souhlasek: {no_consonants}\n")
    f1.write(f"Pocet cisel: {no_digits}\n")


print("3----------------------------------------------------")
#Task 3
#You have a text file. Delete the last line from it. Write the result to another file.

with open("12_Lekce_zzz/text.txt", encoding="utf-8") as f1:
    my_list = [line.rstrip("\n") for line in f1]
my_len = len(my_list)
print(f"pocet radku: {my_len}")
with open("12_Lekce_zzz/text_del.txt", "w", encoding="utf-8") as f1:
    for i in range(my_len-1):
        f1.write(my_list[i] + "\n")


print("4----------------------------------------------------")
#Task 4
#You have a text file. Find the length of the longest line.

with open("12_Lekce_zzz/text.txt", encoding="utf-8") as f1:
    my_list = [line.rstrip("\n") for line in f1]
my_max = 0
line = 0
for i in range(0, len(my_list)):
    if my_max < len(my_list[i]):
        my_max = len(my_list[i])
        line = i + 1
print(f"Nejdelsi radek ma cislo: {line}")
print(f"Ma delku {my_max} znaku.")


print("5----------------------------------------------------")
#Task 5
#You have a text file. Count how many times the word specified by the user occurs in it.

def search_word(word):
    with open("12_Lekce_zzz/text.txt", encoding="utf-8") as f1:
        my_str = ""
        for line in f1:
            my_str += line
        my_list = my_str.split()
        my_count = 0
        for i in my_list:
            if i == word:
                my_count += 1
    return f"Hledane slovo je v souboru {my_count}x." 

word = input("Zadej hledane slovo: ")
print(search_word(word))


print("6----------------------------------------------------")
#Task 6
#You have a text file. Find and replace the specified word. The user determines what to search for and to what it should be replaced.

def search_word(old, new):
    with open("12_Lekce_zzz/text.txt", encoding="utf-8") as f1, open("12_Lekce_zzz/text_replace.txt", "w", encoding="utf-8") as f1:
        my_list = [line.rstrip("\n") for line in f1]
        my_list1 = [i.replace(old, new) for i in my_list]
        for i in my_list1:
            f2.write(i + "\n")
    return my_list1

old = input("Zadej heldane slovo: ")
new = input("Zadej slovo, ktere ho nahradi: ")

print(search_word(old, new))
print()

