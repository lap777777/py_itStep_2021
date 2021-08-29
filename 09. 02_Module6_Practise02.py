print("1---------------------------------------------------------")
# Task 1
# You have a set containing country names. Provide the following features:
my_set = {"CZ", "SK", "AT", "PL", "HU", "GE"}
print(my_set)

# ■ Add a country;
my_set.add("US")
print(my_set)

# ■ Delete a country;
my_set.remove("GE")
print(my_set)

# ■ Search for a country by entered characters;
my_search = input("Zadej hledanou zemi: ")
if my_search in my_set:
    print(f"Zadana zeme {my_search} je v setu.")
else:
    print(f"Zadana zeme {my_search} neni v setu.")

# ■ Check whether the country exists inside the set.
my_search = "CZ"
if my_search in my_set:
    print(f"{my_search} is in my_set.")
else:
    print(f"{my_search} is not in my_set.")
print()

print("2---------------------------------------------------------")
# Task 2
# You have two sets containing city names. Create a third set containing names present in both sets.
set1 = {"Prague", "Bratislava", "Wien", "Dortmund"}
set2 = {"Dalas", "Dortmund", "LA", "NY", "Chicago"}
set3 = set1 & set2
print(set3)
set3 = set1.intersection(set2)
print(set3)
print("----alternativa-pomoci-listu---------------")
set3 = [i for i in set1 if i in set2]
set3 = set(set3)
print(set3)
print()

print("3---------------------------------------------------------")
# Task 3
# You have two sets containing city names. Create a third set containing names present in the first set but not in the second.
set1 = {"Prague", "Bratislava", "Wien", "Dortmund"}
set2 = {"Dalas", "Dortmund", "LA", "NY", "Chicago"}
set3 = set1 - set2
print(set3)
set3 = set1.difference(set2)
print(set3)
print("----alternativa-pomoci-listu---------------")
set3 = [i for i in set1 if i not in set2]
set3 = set(set3)
print(set3)
print()

print("4---------------------------------------------------------")
# Task 4
# You have two sets containing city names. Create a third set containing names present in the second set but not in the first.
set1 = {"Prague", "Bratislava", "Wien", "Dortmund"}
set2 = {"Dalas", "Dortmund", "LA", "NY", "Chicago"}
set3 = set2 - set1
print(set3)
set3 = set2.difference(set1)
print(set3)
print("----alternativa-pomoci-listu---------------")
set3 = [i for i in set2 if i not in set1]
set3 = set(set3)
print(set3)
print()

print("5---------------------------------------------------------")
# Task 5
# You have two sets containing city names. Create a third set containing names unique to each set.

set1 = {"Prague", "Bratislava", "Wien", "Dortmund"}
set2 = {"Dalas", "Dortmund", "LA", "NY", "Chicago"}
set3 = set1 ^ set2
print(set3)
set3 = set1.symmetric_difference(set2)
print(set3)
print("----alternativa-pomoci-listu---------------")
set3 = []
for i in set1:
    if i not in set3 and i not in set2:
        set3.append(i)
for i in set2:
    if i not in set3 and i not in set1:
        set3.append(i)
print(set3)

print("5---------------------------------------------------------")
# Task 6
# A dictionary contains a set of pairs: Country name -> Capital. Provide the possibility to add, delete, search, and replace them.

countries = {"CZ": "Prague", "SK": "Bratislava", "GE": "Berlin", "AT": "Wien", "PL": "Warsau"}

print(countries)

# pridat prvek
country = input("Vloz novy klic - zemi: ")
capital = input("Zadej hlavni mesto k zadane zemi: ")
countries[country] = capital
print(countries)

# delete prvek a)
del_key = input("Vloz stat na vymazani: ")
countries.pop(del_key)
print(countries)
# delete prvek b)
del_key =  input("Vloz stat na vymazani: ")
del countries[del_key]
print(countries)

# search prvek
my_search = input("Zadej stat na vyhledani: ")
if my_search in countries:
    print(f"Nasel jsem {my_search}.\nHlavni mesto je {countries[my_search]}.")
else:
    print("Zadany stat neni v databazi.")

# replace a) key
old_key = input("Zadek klic, ktery chces zmenit: ")
new_key = input("Zadej novy klic: ")
countries[new_key] = countries.pop(old_key)
print(countries)
# replace b) value
key = input("Zadej stat pro ktery chces zmenit hodnotu: ")
new_value = input("Zadej novou hodnotu: ")
countries[key] = new_value
print(countries)

print("---------------------------------------------------------")

