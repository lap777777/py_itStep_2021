################################################################
#### OBJEKTOVE ORIENTOVANE PROGRAMOVANI ########################
################################################################

"""
ruzne pristupy k programovani - funkcionalne, objektove, ... kazde ma plusy a minusy

promenna - ulozeni hodnoty
funkce - provadi nejakou cinnost
do ted jsem je mel separatne od sebe

objektove programovani spojuje promennou a a funkci k objektu
misto promenne se pouziva atribut - pouziva se na objektu
metoda - funkce, ktera patri k nejakemu objektu

kontretni objekt se jmenuje instance (konkretni clovek, kniha, ....)

# instance karel - konkretni objekt - 
- ma kontretni atributy (jmeno, prijmeni, vek, telefon) 
- ma konkretni metody (vstavej, najez se, vyspi se, odpocin si)

# - instance knihovna
- atributy - vyska, delka, seznam knih
- metody - otevri se, zavri se, najdi knihu, update seznamu knih

# instance petr
# instance jana
# instance karel
tyto 3 instance maji stejne rysy - nad nimi si vytvorim tridu - formular (vzor)

class - trida - (template, blueprint) - formulare/stavebni plany - podle nich tvorim jednotlive objekty
napr. nadefinuji neco, co umi vstavat, jist, chodit, pracovat apod - jako vzor
kdyz to naplnim daty, tak mi vznikne konkretni objekt = instance

"""

class Clovek1():    # definice tridy, trida zatim nic neumi, zadne atributy, zadne metody
    pass

karel = Clovek1()   # vytvorim intanci karel dle tridy Clovek()
print(f"Karel je: {karel}")       # vytisknu intanci(objekt)

print("------------------------------------------------------------")

class Clovek():
    # dunder == double underscore
    # __init__ inicializacni metoda - nastavuje novou instanci, nastavi jak se budou tvorit jednotlive instance na zaklade zadanych dat
    def __init__(self, jmeno, prijmeni, vek=20):
        # prvni parametr metody v tride je vzdy self
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.kde_zije = "Planeta Zeme"  # tento atribut bude pro vsechny cloveky stejny
        if self.vek >= 18:              
        # muzu definovat novy atribut pres podminky jinych atributu
            self.plnolety = True
        else:
            self.plnolety = False

    def __str__(self):
        # metoda pro tisk objektu, vypis urceny pro uzivatele (prijemny vypis)
        # prevod objektu na string
        # dam print(objekt) a vytiskne mi metodu __str__
        # str ma prednost pred repr u printu objektu 
        return f"Jmenuji se {self.jmeno} {self.prijmeni}"\
            f" a je mi {self.vek}"

    def __repr__(self):
        # metoda pro tisk objektu - reprezentace - vypis pro vyvojare (jednoznacny)
        # prevod objektu 
        return f"Ja jsem velky clovek\n"\
            f"A jmenuji se {self.jmeno}."
    # kdyz zavolam tisk na objektu bez metody print(karel) - 1. jde __str__, 2. jde __repr__ a az pak nejaky print ktery definuji:
    def tisk(self):
        return self.__repr__()
    
    
karel = Clovek("Karel", "Novak", 39)

print(f"Jmeno je {karel.jmeno}.")
print(f"Prijmeni je {karel.prijmeni}.")
print(f"Vek je {karel.vek}.")
print(f"Zije: {karel.kde_zije}")
print(f"Plnolety: {karel.plnolety}.")
print()

aneta = Clovek("Aneta", "Fialova", 29)

print(f"Jmeno je {aneta.jmeno}.")
print(f"Prijmeni je {aneta.prijmeni}.")
print(f"Vek je {aneta.vek}.")
print(f"Zije: {aneta.kde_zije}")
print(f"Plnolety: {aneta.plnolety}.")
print()

# specialni atribut __dict__ - vytiskne slovnik atributu, ktere v instanci jsou
# tohle mi vytahne slovnik, ale lepsi je ve tride si nadefinovat presne podle sebe formu vypisu
print(karel.__dict__)
print()

petra = Clovek(prijmeni="Cervena", jmeno="Petra")   
# nezadavam vek, vyuzivam defaultniho parametru vek = 20
# a misto position arguments pouziji key arguments

print(aneta.tisk())
print(aneta)    # kdyz neni zadana metoda u printu, tak bere 1. __str__, 2. __repr__, 3. nejaka jina definoavana
print(petra)
print()