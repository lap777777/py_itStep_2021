print("1_________________________________________________")
# Task 1
# You have a text file. Create a new file and remove all bad words from it. The list of bad words is in another file. 

# 1 slovo jeden radek
with open("12_Lekce_zzz/task1_zadani.txt", encoding="utf-8") as f1, open("12_Lekce_zzz/badwords.txt", encoding="utf-8") as f2, open("12_Lekce_zzz/task1_reseni.txt", "w", encoding="utf-8") as f3:
    bad_words = []
    for line in f2:
        bad_words.append(line.rstrip("\n"))
    print(bad_words)
    my_list = []
    for line in f1:
        my_list.append(line.rstrip("\n"))
    print(my_list)
    for i in my_list:
        if i not in bad_words:
            print(i)
            f3.write(i+"\n")

# text souvisly
with open("12_Lekce_zzz/task1_zadanib.txt", encoding="utf-8") as f1, open("12_Lekce_zzz/badwords.txt", encoding="utf-8") as f2, open("12_Lekce_zzz/task1_resenib.txt", "w", encoding="utf-8") as f3:
    bad_words = []
    for line in f2:
        bad_words.append(line.rstrip("\n"))
    my_str = f1.read()
    print(my_str)
    my_list = my_str.split()
    for line in f1:
        my_list.append(line.rstrip("\n"))
    for i in my_list:
        if i not in bad_words:
            print(i)
            f3.write(i+" ")

print("2_________________________________________________")
# Task 2
# Write a Russian-English transliteration program. Data for transliteration are taken from a file and written to another file. The direction is chosen by the user through a menu.

# z jednoho souboru prehazuji do druheho, vyuzit 3 soubor kde je slovnik

my_dict = {"apple": "jablko", "pear": "hruška", "plum": "švestka", "table": "stůl", "table": "stůl", "chair": "židle", "carpet": "koberec", "window": "okno", "door": "dveře", "roof": "střecha", "floor": "podlaha"}
my_dict1 = {value: key for key, value in my_dict.items()}

def translator(direction):
    if direction == 1:
        with open("12_Lekce_zzz/slovnik_cz.txt", encoding="utf-8") as f1, open("12_Lekce_zzz/slovnik_en1.txt", "w") as f2:
            my_list = [line.rstrip("\n") for line in f1]
            for i in my_list:
                f2.write(my_dict1[i] + "\n")
                print(f"{i}: {my_dict1[i]}")
    elif direction == 2:
        with open("12_Lekce_zzz/slovnik_en.txt", encoding="utf-8") as f1, open("12_Lekce_zzz/slovnik_cz1.txt", "w", encoding="utf-8") as f2:
            my_list = [line.rstrip("\n") for line in f1]
            print(my_list)
            for i in my_list:
                f2.write(my_dict[i] + "\n")
                print(f"{i}: {my_dict[i]}")
    else:
        return False
        
while True:
  try:
     direction = int(input("Zadej smer prekladu: 1 pro CZ->EN, 2 pro EN->CZ: "))
  except ValueError:
     print("Chybne zadani, zadej cislo 1 nebo 2.")
     continue
  else:
    if direction == 1 or direction == 2:
        break
    else:
        print("Chybne zadani, zadej 1 nebo 2")

translator(direction)


print("3_________________________________________________")
# Task 3
# The user enters file names until he or she enters the word “quit.” After the input completes, the program must combine the contents of all files listed by the user into one.
# vytvorit si bokem soubory - podle zadani vybrat soubory a ty spojit do jednoho

my_list = ["soubor1.txt", "soubor2.txt", "soubor3.txt", "soubor4.txt", "soubor5.txt"]
file = ""
selection = []
while file != "quit":
    file = input("Zadej nazev souboru (pro ukonceni smycky napis quit): ")
    selection.append(file)

for i in selection:
    if i in my_list:
        with open(f"12_Lekce_zzz/{i}", encoding="utf-8") as f1, open(f"12_Lekce_zzz/soubor_merge.txt", "a", encoding="utf-8") as f2:
            for line in f1:
                f2.write(line)
            f2.write("\n")
    else:
        if i != "quit":
            print(f"soubor {i} neni ve vyberu souboru, vybere se dalsi soubor")
print("hotovo, text z vybranych souboru pridan do hlavniho souboru")



print("4_________________________________________________")
# Task 4
# The user enters file names until he or she enters the word “quit.” After the input completes, the program must write characters present in all listed files to the final file (each file must contain characters).
# vyber stejnych znaku ve vsech souborech

def set_creation(file):
    with open(file, encoding="utf-8") as f1:
        my_str = ""
        for line in f1:
            my_str += line.rstrip("\n")
    my_list = [i for i in my_str]
    my_set = set(my_list)
    return my_set

my_list = ["soubor1.txt", "soubor2.txt", "soubor3.txt", "soubor4.txt", "soubor5.txt"]
file = ""
selection = []
while file != "quit":
    file = input("Zadej nazev souboru (pro ukonceni smycky napis quit): ")
    selection.append(file)

set_list = []
for i in selection:
    if i in my_list:
        set_i = set_creation(f"12_Lekce_zzz/{i}")
        set_list.append(set_i)
    else:
        if i != "quit":
            print(f"soubor {i} neni ve vyberu souboru, vybere se dalsi soubor")

set_intersection = set_list[0]
for i in range(1, len(set_list)):
    set_intersection = set_intersection & set_list[i]
print(set_intersection)

with open("12_Lekce_zzz/soubor_znaky.txt", "w", encoding="utf-8") as f1:
    for i in set_intersection:
        f1.write(i + ", ")

print("hotovo, vytvoren vystup pro znaky v souboru soubor_znaky.txt")
