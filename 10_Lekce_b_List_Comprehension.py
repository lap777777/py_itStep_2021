# LIST COMPREHENSION

# listx = [
#    1. radek - vyraz, ktery pouziji do vysledneho listu
#    2. radek - cyklus, pres ktery iteruji
#    3. radek - podminka, ktera vyradi nektere hodnoty (nemusi byt)
# ]

print("1-----------------------------------------------------")
# chci vytisknout cisla od 0 do 9
my_list = []
for x in range(10):
    my_list.append(x)
print(my_list)

my_list1 = [x for x in range(10)]
print(my_list1)

print("2-----------------------------------------------------")

my_list3 = []
for x in range(10):
    my_list3.append(x*x)
print(my_list3)

my_list4 = [x*x for x in range(10)]
print(my_list4)

print("3-----------------------------------------------------")

my_list5 = []
for x in range(10):
    if x % 2 == 1:
        my_list5.append(x)
print(my_list5)

# list comprehension s podminkou if
my_list6 = [x*x for x in range(10) if x%2 == 1]
print(my_list6)

# 1) co se s tim deje, 2) na cem to prochazim - cyklus, 3) podminka if

print("4-----------------------------------------------------")

# pro prehlednost:

my_list7 = [ 
    x*x                      # co delam
    for x in range(10)       # cyklus
    if x % 2 == 1            # podminka
]
print(my_list7)


print("5-----------------------------------------------------")
# s podminkou if a else

my_list8 = [
    x * x if x > 10 else x * x * x      # co delam, muzu vlozit podminku
    for x in range(20)                  # cyklus
    if x % 2 == 1                       # podminka
]
print(my_list8)

print("6-----------------------------------------------------")
# DICTIONARY COMPREHENSION
# u slovniku musim do prvniho radku pridat klic :

dict1 = {
    x : x * x
    for x in range(10)
    if x % 2 == 1
}
print(dict1)

dict2 = {
    char: char + "_ahoj"
    for char in "nosorozec"
}
print(dict2)

dict3 = {
    word: word.capitalize()
    for word in "tohle je moje veta".split()
}
print(dict3)


print("7-----------------------------------------------------")
# SET COMPREHENSION

set1 = {
    word.upper()
    for word in "tohle je moje auto a moje kocka a moje letadlo".split()
}
print(set1)

set2 = {
    word.upper()
    for word in "tohle je moje auto a karoliny kocka a moje kolo".split()
    if word.startswith("k")
}
print(set2)


print("8-----------------------------------------------------")
# GENERATOR EXPRESION = (
#   vnitrek stejny jako u listu, lisi se jenom typ zavorek
#   vhodny pokud potrebuji dale iterovat - hodnoty se vytvari postupne
# )
# napr. for number in (x*x for i in range(100_000_000)):
    # generator my ty cisla dava jedno po druhem a ja s tim muze delat
    # ma to male naroky na pamet
# for i in (char.upper() for char in "dlouheeeeeslovooooo")
    # idealni pokud potrebuji dale iterovat - Python mi tady dava velke pismenka postupne z daneho retezce
