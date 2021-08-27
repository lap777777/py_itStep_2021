# Task 1
# There is some text. Implement the following features:
text = """sla nanynka do zeli, natrhala tam lupeni! natrhala 10 baliku sena, 5 jich snedla! pak sla na pole, byla tam do 20:00!"""
#   ■ Change the text so that each sentence starts with a capital letter;

text1 = text.lower()
seznam1 = text1.split("!")
print(seznam1)
seznam2 = [vety.strip().capitalize() for vety in seznam1]  # list comprehension
print(seznam2)
text2 = "! ".join(seznam2)
print(text2)
print()

#   ■ Count how many times numbers appear in the text;
my_count = sum(cislo.isdigit() for cislo in text)  # generator expression
print(f"V textu je {my_count} numerickych znaku.")

#   ■ Count how many times punctuation marks appear in the text;
my_count = 0
for i in text:
    if "!" <= i <= "/":
        my_count += 1
print(f"V textu je {my_count} punctuation marks.")
print("------alternativa-------")
my_count = sum("!"<=znak<="/" for znak in text)

#   ■ Count the number of exclamation marks 
my_count = sum(znak == "!" for znak in text)
print(f"V textu je {my_count} vykricniku.")
print()


# # Task 2
# # The user types in a list of integers and a number. Count how many times this number appears in the list. Print the result.
my_list = [4, 7, 9, 13, 45, 7, 9, 5, 0, -5, 3, 4]
number = int(input("Zadej cislo: "))
result = my_list.count(number)
print(my_list)
print(f"Zadane cislo {number} je v seznamu {result}x.")
print()

# # Task 3
# # The user types in a list of integers. Calculate the sum and average of these elements. Print the result.
number = 0
my_list = []
my_count = 0
while number != 999:
    number = int(input("Zadej libovolne cislo (pro ukonceni zadavani zadej 999) : "))
    if number == 999:
        break
    my_list.append(number)
    my_count += 1
my_sum = sum(my_list)
my_avg = my_sum / my_count
print(f"Soucet zadaneho listu je {my_sum}.")
print(f"Prumer zadaneho listu je {my_avg}.")
print()



