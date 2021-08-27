print("1_________________________________________________")
# Task 1
# You have a text file. Create a new file and remove all bad words from it. The list of bad words is in another file. 

# 1 slovo jeden radek
with open("12_Lekce_zzzpodklady/02task1.txt", encoding="utf-8") as f1, open("12_Lekce_zzzpodklady/02badwords.txt", encoding="utf-8") as f2, open("12_Lekce_zzzpodklady/02task1_reseni.txt", "w", encoding="utf-8") as f3:
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
            f3.write(i+"\n")

# text souvisly
with open("12_Lekce_zzzpodklady/02task1b.txt", encoding="utf-8") as f1, open("12_Lekce_zzzpodklady/02badwords.txt", encoding="utf-8") as f2, open("12_Lekce_zzzpodklady/02task1_resenib.txt", "w", encoding="utf-8") as f3:
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
            f3.write(i+" ")

print("2_________________________________________________")
# Task 2
# Write a Russian-English transliteration program. Data for transliteration are taken from a file and written to another file. The direction is chosen by the user through a menu.

# input: zada se smer prekladu - CZ -> EN nebo EN->CZ
# input: zada se slovo na preklad
# output: prelozene slovo
# podle smeru vezmu prvni file, podivam se, jestli je tam hledane slovo - pokud je pokracuji, pokud ne, hlaska
# pak vezmu druhy file a divam, se, jestli je tam dane slovo, pokud ano, tak ho ulozim do promenne a pak vytisknu


# dovjka - z jednoho souboru do druheho, vyuzit 3 soubor kde je slovnik
def translator(direction, word):
    with open("12_Lekce_zzzpodklady/02task2_cz.txt") as f1, open("12_Lekce_zzzpodklady/02task2_en.txt") as f2:
        if direction == 1:
            for line in f1:
                if line == word:
                    rank = f1[line]
                    print(rank)
                if word not in f1:
                    return f"Zadane slovo {word} neni obsazeno ve slovniku"
        
while True:
  try:
     direction = int(input("Zadej smer prekladu: 1 pro CZ->EN, 2 pro EN->CZ: "))
  except ValueError:
     print("Chybne zadani, zadej cislo 1 nebo 2.")
     continue
  else:
    if direction == 1 or direction == 2:
        word = input("Zadej slovo na preklad: ")
        break
    else:
        print("Chybne zadani, zadej 1 nebo 2")

print(translator(direction, word))


print("3_________________________________________________")
# Task 3
# The user enters file names until he or she enters the word “quit.” After the input completes, the program must combine the contents of all files listed by the user into one.

# vytvorit si bokem soubory - podle zadani vybrat soubory a ty spojit do jednoho


print("4_________________________________________________")
# Task 4
# The user enters file names until he or she enters the word “quit.” After the input completes, the program must write characters present in all listed files to the final file (each file must contain characters).

# vyber jedinecnych znaku ze souboru
