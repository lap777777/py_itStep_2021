print("1-----------------------------------------------------------")
# Task 1
# vytvorte slovnik, ktery vypada jako menu restaurace
# klice jsou jmena jidel (jednoslovna), hodnoty jsou ceny
# a) vytvorte ho jednim prikazem s nekolika jidly
# b) vytvorit prazdny, jidla postupne pridavejte do prvniho
# c) zkuste nejake jidlo vymazat
# d) zmenit u nejakeho jidla cenu

jidelak1 = {"svickova": 250, "tatarak": 200, "losos": 400, "pstruh": 250}
jidelak2 = {}
jidelak2["svickova"] = 250
jidelak2["tatarak"] = 200
jidelak2["losos"] = 400
jidelak2["pstruh"] = 250
print(jidelak1)
print(jidelak2)
del jidelak2["losos"]
jidelak1["svickova"] = 300
print(jidelak2)
print()

print("2-----------------------------------------------------------")
# Task 2
# vytvorit funkci, ktera si od hosta vezme objednavku a vytvori ucet
# host bude postupne zadavat jidla, ktere si chce dat (pomoci inputu).
# pokud jidlo mame v menu, tak se vypise potvrzeni a cena (muze si objednat jedno jidlo vickrat)
# pokud jidlo neni, vypise se, ze jidlo neni v nabidce
# pokud zada prazdny retezec, znamena to konec objednavani a vypise se celkova cena
def bill():    
    my_sum = 0
    while True:
        jidlo = input("Zadej jidlo: ")
        if not jidlo:
            break
        if jidlo in jidelak1:
            my_sum += jidelak1[jidlo]
            print(f"cena jidla {jidelak1[jidlo]} CZK")
            print(f"dosavadni utrata {my_sum} CZK")
        else:
            print("Toto jidlo neni v nabidce.")
    return f"Celkova cena objednanych jidel: {my_sum} CZK."

print(bill())
print()


print("3------------------------------------------------------------")
# task 3
# napiste funkci, ktera vypise vsechny jidla
def meals(dictionary):
    for key in dictionary.keys():
        print(key)

meals(jidelak1)
print()

print("4------------------------------------------------------------")

# Task 4
# napiste funkci, ktera vypise cele menu, - jidla s cenami
def menu(dictionary):
    for key, value in dictionary.items():
        print(f"Jidlo {key} stoji {value} CZK.")

menu(jidelak1)
print()

print("5------------------------------------------------------------")
# Task 5
# vytvorte slovnik, kde klice jsou uzivatelska jmena a hodnoty jsou hesla
# zeptej se uzivatele na jmeno a heslo a vypiste mu, jestli se uspesne prihlasil
passwords = {"petr": "heslo", "pavel": 1234, "jan": "tajne_heslo", "jana": "kvetinka"}

user_name = input("Zadej uzivatelske jmeno: ")
if user_name in passwords.keys():
    password = input("Zadejte heslo: ")
    if password in passwords.values():
        print("Vyborne, spravne heslo.")
    else:
        print("Spatne heslo.")
else:
    print("Zadany uzivatel neni v databazi.")
print()

print("------------------------------------------------------------")
# Task 6
# definuj slovnik, kde klice jsou data v pristim tydnu( vyjadrena stringem nebo jednim cislem) a hodnoty jsou teploty
# pro zadani data program vypise, jak bude, pripadne jak bude den potom, dva dny potom.
# tezsi verze - hodnoty jsou dalsi slovniky, kde je ulozena nejen teplota, ale i slovni popis pocasi
weather = {
1: {"den": "Pondeli", "stupne": 30, "popis": "vedro"}, 
2: {"den": "Utery", "stupne": 20,  "popis": "prsi"}, 
3: {"den": "Streda", "stupne": 10, "popis": "osklivo"}, 
4: {"den": "Ctvrtek", "stupne": 0, "popis": "zima"}, 
5: {"den": "Patek", "stupne": -10, "popis": "jeste vetsi zima"}, 
6: {"den": "Sobota", "stupne": 20, "popis": "konecne trochu teplo"}, 
7: {"den": "Nedele", "stupne": 35, "popis": "pekelne vedro"}
}

day = int(input("Zadej cislo dne (1 po, 2 ut, 3 st, ...) pro info o pocasi: "))
for i in range(3):
    den = weather[day]["den"]
    stupne = weather[day]["stupne"]
    popis = weather[day]["popis"]
    print(f"Vybrany den: {den}, stupne: {stupne}, popis: {popis}")
    day += 1
    if day > 7:
        day = 1
print()

print("7------------------------------------------------------------")
# Task 7
# nadefinujte slovnik, kde klice jsou jmena lidi od vas z rodiny a hodnoty data jejich narozeni. (vyguglit, jak Python definuje datum)
# nechte uzivatele zadat jmeno nekoho z rodiny a vypocitejtejte jak je stary

from datetime import datetime as dt

now = dt.now()   

dates = {
"tata": "19.4.1978",
"mama": "24.9.1979",
"David": "18.5.2006",
"Julie": "16.12.2007",
"Tom": "5.8.2009",
"Elen": "28.9.2015"
}

member = input("Vyber clena rodiny: ")
datum = dt.strptime(dates[member], "%d.%m.%Y")
rozdil = now - datum
print(f"Vek vybraneho clena rodiny: {member} je {rozdil}.")
print()

print("8------------------------------------------------------------")
# Task 8 
# napiste funkci, ktera vezme jako parametr vetu (nejaka slova se ve vete muzou opakovat).
# funkce spocita pocet slov ve vete a vrati ho jako slovnik
# "this is a very nice very very nice test" =>
# {"this": 1, "is": 1, "a": 1, "very": 3, "nice": 2, "test": 1}


def count_words(sentence):
    my_list = sentence.split()
    my_dict = {}
    for i in my_list:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    return my_dict

my_str = "This is a very nice very very nice test"
print(count_words(my_str))
print()

print("9------------------------------------------------------------")
# Task 9
# Napiste program na pocitani deste ve mestech.
# Uzivatel postupne zadava jmeno mesta a dest v milimetrech (nejake mesto se muze zadat vicekrat)
# Program pak vytiskne, kolik v kazdem meste naprselo.
# priklad zadani 
# Brno
# 10
# Bratislava
# 20
# Brno
# 20
# print vysledku
# {Brno: 30, Bratislava: 20}

my_dict = {}
while True:
    town = input("Zadej mesto (pro ukonceni zadej x): ")
    if town == "x":
        break
    rain = int(input("Zadej kolik naprselo v mm: "))
    if town in my_dict:
        my_dict[town] += rain
    else:
        my_dict[town] = rain

print(my_dict)    

print("         ----------------------------------------")
# Tezsi verze dvojky:
# misto celkoveho deste vypocita program prumerny dest podle poctu dni

rainfall = {}
n_days = {}

while True:
    city = input("Zadej mesto: ")
    if not city:
        break
    mm_rain = int(input("Zadej kolik mm naprselo: "))

    old_mm_rain = rainfall.get(city, 0)   # puvodni hodnota
    rainfall[city] = mm_rain + old_mm_rain  # nastavuji novou hodnotu + k ni pridavam tu puvodni pres funkci get

    n_days[city] = n_days.get(city, 0) + 1
    # pocet dni = beru puvodni hodnotu ze slovniku pomoci get a pridavam k tomu jedna

for key, value in rainfall.items():
    print(f"v {key} naprselo prumerne {value/n_days[key]} mm deste.")
# iteruji pres slovnik rainfall - iteruji pres klic a hodnotu, mam tam odkaz i na dalsi slovnik, tak musim uvest jeho jmeno n_days[key] a beru tak hodnoty z druheho slovniku.

print("         ----alternativa-s-jednim-slovnikem-------")
rainfall = {}
while True:
    city = input("Zadej mesto: ")
    if not city:
        break
    actual_rain = int(input("Zadej kolik mm naprselo: "))
    old_value = rainfall.get(city, {"rain": 0, "days": 0})

    rainfall[city] = {
        "rain": actual_rain + old_value["rain"],
        "days": 1 + old_value["days"]
    }
print(rainfall)
for key, value in rainfall.items():
    print(f"V {key} naprselo prumerne \
{value['rain']/value['days']} mm deste.")

#  \ znak v f stringu mi dovoli v kodu to hodit na druhy radek a pak na druhem radku muzu jit bez odsazeni 

print("10-----------------------------------------------------------")
# Task 10
# Mam list, ve kterem jsou dvojice cisel napr. [(1,2), (3,7), (9,5)]
# Napis kod, ktery ten list projde a spocita soucet soucinu
# v danem pripade 1 * 2 + 3 * 7 + 9 * 5

my_list = [(1,2), (3,4), (5,6), (7,8)]
my_sum = 0
for i in my_list:
    my_sum += i[0] * i[1]
print(f"Soucet soucinu tuple je: {my_sum}")