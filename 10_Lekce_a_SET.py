# Datovy typ SET ... mnozina
# mnozina je podobna seznamu, ale hodnoty se tam nesmi opakovat
# pokud zadam vice stejnych hodnot, tak mi vrati set pouze z jedinecnymi hodnotami
# uvadi se stejne jako slovnik v {}
# je mutable - lze ji menit pomoci add a remove
# hlavni vyuziti je odstraneni duplicit
# A set object is an unordered collection of distinct hashable objects. Common uses include membership testing, removing duplicates from a sequence, and computing mathematical operations such as intersection, union, difference, and symmetric difference. 

set1 = {1,2,3,4,1,2,3,4,5,6,7,1,1,1,1}
print(set1)

list1 = [1, 1, 3, 4, 5, 5, 6]
set2 = set(list1)
print(set2)


set2.add(9)
print(set2)
set2.add(9)   # tady se nestane nic, 9 uz v setu je

set2.remove(9)   # odmaze konkretni parametr
print(set2)
# remove vraci chybu, pokud prvek neni v setu, takze but muzim osetrit vyjimku nebo muzu pouzit metodu discard(), ktera bud vymaze prvek nebo nevyhazuje chybu, pokud tam prvek neni

set2.pop()  # vymaze libovolny prvek setu, tady nelze zadat argument
print(set2)


delka = len(set2)
print(f"delka: {delka}")

if 3 in set2:
    print(f"3 je v {set2}")
else:
    print("3 neni v setu")
print()

print("SET - matematicke funkce: ")

{2, 3} < {2, 3, 5}   # tohle vrati True - prvni je podmnozina druheho
{2, 7} < {2, 3, 5}   # tohle vrati False - prvni neni podmnozina druheho

{1, 2}.issubset([1, 2, 3])    # prvni je podmnozinou druheho
{1, 2, 3}.issuperset([1, 2])  # druhe je podmnozinou prvniho

set3 = {2, 7} | {2, 3, 5}   # sjednoceni, union - vrati svechny prvky v prvnim a druhem setu, lze take pouzit set3 = setA.union(setB)
print(f"union: {set3}")

set4 = {2, 7} & {2, 3, 5}   # prunik, intersection, vrati, ty ktere jsou spolecne obou, lze take pouzit set4 = setA.intersection(setB)
print(f"intersection: {set4}")

set5 = {1, 2, 3} - {3, 4} # difference - vrati vsechny prvky z prvni, ktere nejsou v druhe
print(f"difference: {set5}")
setA = {1, 2, 3}
setB = {3, 4, 5}
setD = setA.difference(setB)

set6 = {2, 7} ^ {2, 3, 5}   # symetric diference - vrati ty, ktere nejsou v obou spolecne, takze unikatni z prvni a druhe, lze take pouzit set6 = setA.symetric_difference(setB)
print(f"symetric_difference: {set6}")

print()

# cviceni 1
# udelejte si list cisel, cisla se muzou opakovat. Zjistete pocet unikatnich cisel.

my_list = [1, 2, 1, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 5, 4]
my_set = set(my_list)
l_len = len(my_list)
l_set = len(my_set)
print(my_list)
print(f"Delka seznamu je {l_len} prvku.")
print(f"Delka setu je {l_set} prvku.")
print()


# cviceni 2 = neni na sety
# napiste funkci, ktera vezme retezec a vrati stejne dlouhy retezec
# v novem retezci budou ale pismenka serazena podle abecedy

my_str = "ahoj ahoj ahoj"
my_list = list(my_str)
[my_list.remove(i) for i in my_list if i == " "]
my_list.sort()
my_str1 = ''.join(my_list)
print(my_str)
print(my_str1)
print()

