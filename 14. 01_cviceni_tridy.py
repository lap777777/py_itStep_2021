print("1----------------------------------------------")
# Priklad 1
# Vytvorte tridu zmrzlina
# Zmrzlina ma jednu vlastnost, a to je prichut
# Vytvorte nekolik konkretnich instanci s ruznymi prichutemi a ulozte je do listu
# Nakonec je vsechny vytisknete z daneho listu

class Zmrzlina():
    def __init__(self, flavour):
        self.flavour = flavour
    def __str__(self):
        return f"prichut: {self.flavour}"

jahoda = Zmrzlina("jahodova")
citron = Zmrzlina("citronova")
cokolada = Zmrzlina("cokoladova")

prichute = [jahoda, citron, cokolada, Zmrzlina("boruvkova"), Zmrzlina("mrkvova")]
prichute.append(Zmrzlina("pistaciova"))

for i in prichute:
    print(i)

print("2----------------------------------------------")
# Priklad 2
# Vytvor tridu napoj
# Napoj ma dve vlastnosti, jmeno a teplotu
# vytvor nekolik napoju a vytiskni je

class Napoj():
    def __init__(self, jmeno, teplota):
        self.jmeno = jmeno
        self.teplota = teplota
    def __str__(self) -> str:
        return f"Napoj: {self.jmeno}, teplota: {self.teplota}"

voda = Napoj("voda", 10)
pivo = Napoj("pivo", 5)
vino = Napoj("vino", 20)
caj = Napoj("caj", 80)

print(voda)
print(pivo)
print(vino)
print(caj)

print("3----------------------------------------------")
# priklad 3
# stejne jako 2, ale pokud nezadam napoj, bude mit teplotu 20 stupnu

class Napoj1():
    def __init__(self, jmeno, teplota=20):
        self.jmeno = jmeno
        self.teplota = teplota
    def __str__(self) -> str:
        return f"Napoj: {self.jmeno}, teplota: {self.teplota}"

voda = Napoj1("voda", 10)
pivo = Napoj1("pivo", 5)
vino = Napoj1("vino", 20)
caj = Napoj1("caj", 80)
kava = Napoj1("kava")

print(voda)
print(pivo)
print(vino)
print(caj)
print(kava)

print("4----------------------------------------------")
# Priklad 4
# Vytvorte tridu kniha. Kniha ma nekolik vlastnosti:
# - autora
# - jmeno
# - rok vydani
# - cenu
# zaridte aby se kniha dala hezky vytisknout

class Book():
    def __init__(self, author, name, year, price):
        self.author = author
        self.name = name
        self.year = year
        self.price = price
    def __str__(self): 
        return f"kniha: {self.name}\n"\
            f"autor: {self.author}\n"\
            f"rok vydani: {self.year}\n"\
            f"cena: {self.price}\n"

kniha1 = Book("Josef Capek", "RUR", 1925, 234)
kniha2 = Book("Josef Capek", "Bila nemoc", 1926, 321)
kniha3 = Book("Bozena Nemcova", "Babicka", 1850, 400)

print(kniha1)
print(kniha2)
print(kniha3)

