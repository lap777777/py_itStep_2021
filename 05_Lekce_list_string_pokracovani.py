znamky = ["nosorozec", 12, True, 56.0, False, None, "hroch"] 
# list obsahujici ruzne datove typy, normalni listy obsahuji data jednoho datoveho typu
znamky[0]   # prvni prvek
znamky[-1]  # posledni prvek
znamky[1:4]  # vyber prvniho, druheho a tretiho prvku
print()
jine_znamky = znamky  # pozor, pokud zmenim jeden, meni si i druhy
print(znamky)
znamky[0] = "zirafa"
print(znamky)
print(jine_znamky)
# vytisknout se oba listy stejne 
# pokud chci vytvorit novy seznam
jine_znamky1 = znamky[:]
print()

# DOKUMENTACE: sequence types - lists
# operace:
# x in s
# x not in s
print("chobotnice" in znamky)
print("zirafa" in znamky)
print("chobotnice" not in znamky)
print("zira" in znamky)
print()

# metody na listu (funkce, ktere se prirazuji objektu):
znamky.append("57")  # prida na konec listu "57"
print(znamky)
znamky.insert(3, 45)  # insert - vkladani s 2 argumenty (kam ukladat - pred jaky index, co ukladat)
print(znamky)
znamky.extend(jine_znamky)  # prilepi na konec jednoho listu druhy list
print(znamky)
# pokud chci secist dva seznamy pomoci +, tak musim napsat znamky = znamky + jine_znamky
print()


print(znamky.index("hroch")) # .index() hleda, jestli prvek je v seznamu - vrati index, prvniho prvku, ktery najde
try:
    print(znamky.index("hroch", 10))      # hleda dany vyraz od mista, ktere mu stanovim, tady od 11 prvnku
    print(znamky.index("hroch", 6, 17))   # hleda dany prvek v rozsahu, pokud nenajde, tak vyhodi chybu 
    print(znamky.count("hroch"))          # hleda co napisu a vyhodi pocet, kolikrat to tam je
    print(znamky.remove("hroch"))         # odstranit hrocha
except:
    print("chyba")
print(znamky)
print()

# RETEZCE a METODY
# String Methods v dokumentaci
str1 = "ahoj, dnes je hezky"
print(str1)
str2 = str1.upper() # zmeni retezec na velka pismena
print(str2)
str6 = str2.isupper()  # je retezec slozen z velkych pismen
print(str6)
str5 = str2.lower() # zmeni retezec na mala pismena
print(str5)
str7 = str5.islower() # je slozen retezec z malych znaku
print(str7)
str3 = str1.title() # zmeni prvni pismenka ve slovech na velka
print(str3)
str4 = str1.capitalize() # prvni pismeno stringu zmeni na velke
print(str4)
print()

# str.isalpha() ... sklada se z pismen
# str.isdigit() ... sklada se z cislic
# str.isalnum() ... sklada se z cislic a pismen
str8 = "ahoj12-34"
print(str8.isalnum())  # vyhodi false protoze "-" neni cislo ani pismeno
print()

# vyhledavani ve strinzich:
str9 = "ahoj dnes je hezky"
print(str9)
print(str9.index("dnes")) # pokud neni, tak vraci chybu, jinak vraci index, kde hledany retezec zacina
print(str9.find("neni"))  # pokud neni, tak vrati -1, existuje pouze na stringu
print()

str = "Ahoj, dnes je hezky"
str1 = str.replace("hezky", "osklivo")  
# nahrazuje v retezci slovo, retezec je nemenny, tak musim vytvorit novy retezec
# argumenty(co menim, cim to menim, kolikrat to menim - pokud chci vymenit vsechny, tak nic nezadam)
print(str)
print(str1)
print()

# nahrazeni mezer
str = "     Lucka     "
print(str)
print(str.strip())     # strip vyhodi mezervy
print(str.lstrip())    # lstrip vyhodi mezery nalevo od prvniho znaku
print(str.rstrip())    # rstrip vyhodi mezery zprava po prvni znak 
print()
str = "    Lucka a Petr     "
print(str)
str1 = str.replace(" ", "")  # vyhodim vsechny mezervy, i ty uprostred
print(str1)
# pokud zadam do zavorky argument, tak vyhodi znak v argumentu, defaultne vyhodi mezervy
str = "krokodylffaaafff".strip("kaf")  # usekne z kraju vsechna k, a, f
print(str)
print()

str = "www.seznam.cz"
str1 = str.lstrip("w.")  # odsekne zleva vsechny w, .


# rozdeleni stringu do seznamu
str1 = "ahoj, ja se mam dobre"
list1 = list(str1)
print(list1)

list1 = str1.split()   # rozdeluje string do seznamu po slovech, defaultne mezera, muzu do argumentu dat podle ceho to chci rozdelit

rozdelena = "ahoj ja se mam dobre\nco ty".split()
print(rozdelena)
rozdelena[0] = rozdelena[0].title()
rozdelena[3] = rozdelena[3].upper()
print(rozdelena)

veta = " ".join(rozdelena)
veta1 = "---".join(rozdelena)
print(veta)
print(veta1)
veta3 = "slon".join(rozdelena)
print(veta3)
list1 = veta3.split("slon")
print(list1)
print()


# funkce ord() ... vraci poradi v ASCI tabulce
a = ord("a")
print(a)  # vytiskne poradi a v ASCI tabulkce
# funkce chr() ... vraci z poradi v ASCI tabulce pismenko nebo znak
a = chr(97)
print(a)  # 97 v ASCI je a, takze vrati a

print()
print("----------------------------------------------------------------------------------------")
print()

# LIST COMPREHENTION
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
# my_list2 = [slovo.upper() for slovo in my_list1 if slovo in my_list]
# my_list2 = [slovo.upper() if slovo in my_list else slovo for slovo in my_list1]

# GENERATOR EXPRESSSION
#   ■ Count how many times numbers appear in the text;
my_count = sum(cislo.isdigit() for cislo in text)  # generator expression
print(f"V textu je {my_count} numerickych znaku.")
# Podminka meni cislo na radu true/false a pak scita true a false, takze vrati pocet true


# priklad 2 na generator expresion
my_string = "abcd123***"
numbers = sum(c.isdigit() for c in my_string)
letters = sum(c.isalpha() for c in my_string)
others  = len(my_string) - numbers - letters 
print(f"Zadany retezec obsahuje {numbers} cislic, {letters} pismen a {others} ostatnich znaku.")
print()