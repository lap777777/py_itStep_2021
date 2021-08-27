print("1-------------------------------------------------------------")
seznam = [5, 7, 9, 15, 2, 11, 50, 1, 4, 16, 6, 20]

# mam cislo 4 a chci zjistit, jestli je v seznamu
# nesmim pouzit in, .find nebo .index

# LINEARNI VYHLEDAVANI -> slozitost linearni, prochazim seznam 1x, delka je n
def list_search(list):
    for i in seznam:
        if i == 4:
            return True
    return False

print(list_search(seznam))

# rychlejsi zpusob je binarni vyhledavani - seznam vzdy rozdelim na dve pulky, porovnam s hledanym cislem a pulku ve ktere neni, tu vyhodim a takhle postupuji nez najdu/nenajdu svoje cislo -> logaritmicka slozitost (log(2))
# potrebuji setridenou kolekci (napr. seznam) - vyplati se, kdyz setridim jednou a vyhledavam vickrat. Pokud setridim jednou a hledam jednou, tak trideni je take narocne, tak se to uz nemusi vyplatit proti jednomu cyklu
print("2-------------------------------------------------------------")

def binary_division(list, number):
    while len(list) != 0:
        my_len = len(list)
        middle = my_len // 2
        if number == list[middle]:
            return True
        elif number < list[middle]:
            list = list[:middle]
        else:
            list = list[middle+1:]  # jednoprvkovy seznam se opakuje do nekonecna, tak pridam + 1 abych mel dvouprvkovy
        print(list)
    return False
    
seznam = [5, 7, 9, 15, 2, 11, 50, 1, 4, 16, 6, 20]
seznam.sort()

number = 4
print(binary_division(seznam, number))

print("3-------------------------------------------------------------")

def binary_division1(list, number):
    low = 0
    high = len(list)    
    while low <= high:
        print(list[low:high])
        middle = low + (high - low) // 2
        print(middle)
        if number == list[middle]:
            return True
        elif number < list[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return False

seznam = [5, 7, 9, 15, 2, 11, 50, 1, 4, 16, 6, 20]
seznam.sort()

number = 5
print(binary_division1(seznam, number))
