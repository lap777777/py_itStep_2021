import os

print("1-------------------------------------------------------")
# Task 1
# You have a text file. Create a new file where you should write all words consisting of at least seven letters found in the source file.
with open("12_Lekce_zzz/task1.txt", encoding="utf-8") as f1, open(os.path.join(os.curdir, "12_Lekce_zzz", "task1_novy.txt"), "w", encoding="utf-8") as f2:
    for line in f1:
        if len(line) >=7:
            f2.write(line)

print("2-------------------------------------------------------")
# Task 2
# You have a text file. Write its lines to another file. The order of lines in the second file must match the order of lines in the source file.
with open("12_Lekce_zzz/task1.txt", encoding="utf-8") as f1, open("12_Lekce_zzz/task2_novy.txt", "w", encoding="utf-8") as f2:
    for line in f1:
        f2.write(line)

print("3-------------------------------------------------------")
# Task 3
# You have a text file. Write its lines to another file. The order of lines in the second file must be inverse.
my_list = []
with open("12_Lekce_zzz/task1.txt", encoding="utf-8") as f1, open("12_Lekce_zzz/task3_novy.txt", "w", encoding="utf-8") as f2:
    my_list = [line.rstrip("\n") for line in f1]
    my_list1 = my_list[::-1]
    print(my_list1)
    for i in my_list1:
        f2.write(i + "\n")

with open("12_Lekce_zzz/task1.txt", encoding="utf-8") as f1, open("12_Lekce_zzz/task3_novy_b.txt", "w", encoding="utf-8") as f2:
    my_list = f1.readlines()
    print(my_list)
    my_list = my_list[::-1]
    for i in my_list:
        f2.write(i.rstrip("\n") + "\n")

print("4-------------------------------------------------------")
# Task 4
# You have a text file. Add a line consisting of twelve asterisks (************) after the last line among the lines that have no comma. If there are no such lines in the file, the asterisks should be added after all lines of the existing file. Write the result to another file.

# line1
with open("12_lekce_zzz/line1.txt") as f1, open("12_Lekce_zzz/task4a.txt", "w", encoding="utf-8") as f2:
    my_list1 = [line.rstrip("\n") for line in f1]
    print(my_list1)
    my_list2 = []
    for i in my_list1:
        if i[-1] == ",":
            my_list2.append("************")
        my_list2.append(i)
    if my_list2[-1][-1] != ",":
        my_list2.append("************")
    print(my_list2)
    for i in my_list2:
        f2.write(i+"\n")

# line2
with open("12_lekce_zzz/line2.txt") as f1, open("12_Lekce_zzz/task4b.txt", "w", encoding="utf-8") as f2:
    my_list1 = []
    for line in f1:
        my_list1.append(line.rstrip("\n"))
    my_list2 = []
    for i in my_list1:
        if i[-1] == ",":
            my_list2.append("************")
        my_list2.append(i)
    if my_list2[-1][-1] != ",":
        my_list2.append("************")
    for i in my_list2:
        f2.write(i+"\n")

print("5-------------------------------------------------------")
# Task 5
# You have a text file. Calculate the number of words that begin with a character set by the user.
while True:
        letter = input("Zadej libovolne pismeno: ")
        if not letter.isalpha():
            letter = input("Zadej libovolne pismeno: ")
        else:
            break
letter = letter.lower()

# 1 slovo na radek
with open("12_Lekce_zzz/task5_slova.txt", encoding="utf-8") as f1:
    my_sum = 0
    for line in f1:
        if line[0].lower() == letter:
            my_sum += 1
    print(f"{my_sum} slovo/a zacina/ji zadanym pismenem {letter}")

# souvisly text:
with open("12_Lekce_zzz/text.txt") as f1:
    my_string = f1.read()
    my_list = my_string.split()
    my_sum = 0
    for i in my_list:
        if i[0].lower() == letter:
            my_sum += 1
    print(f"{my_sum} slovo/a zacina/ji zadanym pismenem {letter}")


print("6-------------------------------------------------------")
# Task 6
# You have a text file. Write all its lines to another file while replacing * with & and vice versa.
with open("12_Lekce_zzz/podklad.txt", encoding="utf-8") as f1, open("12_Lekce_zzz/task6.xtx", "w", encoding="utf-8") as f2:
    my_list = f1.readlines()
    print(my_list)
    my_list1 = []
    for line in my_list:
        new_line = ""
        for i in line:
            if i == "*":
                new_line += "&"
            elif i == "&":
                new_line += "*"
            else:
                new_line += i
        my_list1.append(new_line)
    print(my_list1)
    for i in my_list1:
        f2.write(i)

print("7-------------------------------------------------------")
# Task 7
# You have an array of strings. Write them to a file while placing each array element on a separate line and preserving the order.
my_list = [
    "tohle je prvni radek",
     "tohle je druhy radek",
      "tohle je treti radek",
       "tohle je ctvrty radek",
        "tohle je paty radek"]

with open("12_Lekce_zzz/task7.txt", "w", encoding="utf-8") as f1:
    for i in my_list:
        f1.write(i + "\n")

print("8-------------------------------------------------------")
# Task 8
# You have an array of strings. Write them to a file while placing each array element on a separate line and reversing the order.
my_list = [
    "tohle je prvni radek",
     "tohle je druhy radek",
      "tohle je treti radek",
       "tohle je ctvrty radek",
        "tohle je paty radek"]

with open("12_Lekce_zzz/task8.txt", "w", encoding="utf-8") as f1:
    my_list = my_list[::-1]
    for i in my_list:
        f1.write(i + "\n")

print("9-------------------------------------------------------")
# Task 9
# You have a text file. Calculate the number of characters in it.
with open("12_Lekce_zzz/podklad.txt") as f1:
    my_string = f1.read()
    my_len = len(my_string)
    print(f"Soubor obsahuje {my_len} znaku.")
    my_sum = 0
    my_sum1 = 0
    for i in my_string:
        if i.isalpha():
            my_sum += 1
        elif i.isdigit():
            my_sum1 += 1
    print(f"Soubor obsahuje {my_sum} pismenek.")
    print(f"Soubor obsahuje {my_sum1} cislic.")
    print(f"Soubor obsahuje {my_len - my_sum - my_sum1} ostatnich znaku.")
    
print("10------------------------------------------------------")
# Task 10
# You have a text file. Calculate the number of lines in it.

my_sum = 0
with open("12_Lekce_zzz/podklad.txt") as f1:
    for lines in f1:
        my_sum += 1
print(f"Pocet radku v souboru je: {my_sum}")
