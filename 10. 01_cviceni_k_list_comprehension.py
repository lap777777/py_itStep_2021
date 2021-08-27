print("3----------------------------------------------------")
# Task 3
# Napiste funkci, ktera vrati treti mocniny vsech cisel v zadanem rozsahu
def treti_mocnina(lower, upper):
    return [x*x*x for x in range(lower, upper+1)]

print(treti_mocnina(1, 10))

print("4a---------------------------------------------------")
# Task 4
# a) vytvorte funkci, ktera vezme seznam cisel (list of int) a vytvori z nich retezce
def int_to_string(list):
    return [str(i) for i in list]

print(int_to_string([1,2,3]))

print("4b---------------------------------------------------")
# b) vytvori retezec jen z tech cisel, co jsou mensi nez  15.
def int_to_string1(list):
    return [str(i) for i in list if i < 15]

print(int_to_string1([1, 10, 2, 20, 3, 30, 4, 40]))

print("5----------------------------------------------------")
# Task 5
# sectete vsechna cisla od 15 do 35 (muzete pouzit funkci sum)
my_sum = sum(i for i in range(15, 36))
print(f"Soucet vsech cisel od 15 do 35 je {my_sum}.")


print("6----------------------------------------------------")
# Task 6
# Napiste funkci, ktera vezme retezec, kde jsou cisla a shluky pismenek oddelene mezerami. Funkce vrati soucet cisel a pismenka ignoruje
# Napr. "10 abc 20 de44 30 55fg 40" -> 100
def my_sum(string):
    return sum(int(i) for i in string if i.isdigit())

soucet = my_sum("10 abc 20 de44 30 55fg 40")
print(f"Soucet cisel v retezci je: {soucet}.")

print("7----------------------------------------------------")
# Task 7
# otocte slovnik:
# vytvorte funkci, ktera vezme slovnik a vytvori novy slovnik, kde klice jsou to, co bylo minule hodnoty a naopak
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

def reverse_dict(dictionary):
    my_dict1 = {
        value: key
        for key, value in dictionary.items()
    }
    return my_dict1

print(reverse_dict(my_dict))

print("8----------------------------------------------------")
# Task 8
# Vytvorte funkci, ktera narovna seznam - tj. ze seznamu dve urovne hlubokeho vytvori seznam jednourovnovy.
# [[1,2], [3,4]] => [1, 2, 3, 4]
# asi budete potrebovat vnoreny cyklus = v list comprehensions lze vnorovat take

my_list1 = [[1,2], [3,4], [5,6]]
my_list2 = []

for i in my_list1:
    for j in i:
        my_list2.append(j)
print(my_list2)

# pomoci list comprehension
my_list2 = [j for i in my_list1 for j in i]
print(my_list2)


print("-----------------------------------------------------")