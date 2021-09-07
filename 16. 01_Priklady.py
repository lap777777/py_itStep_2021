print("1-------------------------------------------------------")
# Priklad 1
# prav tridu zmrzlinovy pohar z minula, aby umela pridat maximalne 3 kopecky. Pokud pridavam ctvrty nic se nestane, proste tam budou porad jenom 3

class KopecekZrzliny():
    def __init__(self, flavour, price) -> None:
        self.flavour = flavour
        self.price = price
    def __str__(self):
        return f"kopecek ma prichut: {self.flavour} a stoji {self.price} CZK."

class PoharZmrzliny():
    """
    umi pridavat kopecky metodou add_kopecek s atributem kopecek
    """
    my_count = 0  # nastaveni pocitadla na 0

    def __init__(self):
        self.kopecky = []
        
    def add_kopecek(self, kopecek):
        if self.__class__.my_count <3 :
            self.kopecky.append(kopecek)
            self.__class__.my_count += 1  # pocitadlo pro danou tridu
            print(f"Kopecek {kopecek.flavour} uspesne pridan.")
        else:
            print("pohar uz je plny, nejde pridat")

    def __str__(self) -> str:
        result = f"Pohar obsahuje {len(self.kopecky)} kopecky/u.\n"
        for kopecek in self.kopecky:
            result += f"\tprichut: {kopecek.flavour}\n"
        return result

kopecek1 = KopecekZrzliny("jahodovy", 10)
kopecek2 = KopecekZrzliny("citronovy", 12)
kopecek3 = KopecekZrzliny("cokoladovy", 13)
kopecek4 = KopecekZrzliny("malinovy", 15)

print()

pohar = PoharZmrzliny()
pohar.add_kopecek(kopecek1)
pohar.add_kopecek(kopecek2)
pohar.add_kopecek(kopecek3)
pohar.add_kopecek(kopecek4)
print()
print(pohar)
print()

print("2-------------------------------------------------------")
# Priklad 2
# Vytvor tridu VelkyPohar, ktra bude skoro stejna jako ZmzlinovanyPohar, jen s tim rozdilem, ze limit na kopecky bude 5.

class VelkyPohar():

    pocitadlo = 5  # tridni promenna

    def __init__(self):
        self.kopecky = []
        
    def add_kopecek(self, kopecek):
        if len(self.kopecky) < self.__class__.pocitadlo: # volam tridni promennou
            self.kopecky.append(kopecek)
            print(f"Kopecek {kopecek.flavour} uspesne pridan.")
        else:
            print("pohar uz je plny, nejde pridat")

    def __str__(self) -> str:
            result = f"Pohar obsahuje {len(self.kopecky)} kopecky/u.\n"
            for kopecek in self.kopecky:
                result += f"\tprichut: {kopecek.flavour}\n"
            return result


kopecek5 = KopecekZrzliny("smoulovy", 13)
kopecek6 = KopecekZrzliny("svestkovy", 12)
pohar1 = VelkyPohar()
pohar1.add_kopecek(kopecek1)
pohar1.add_kopecek(kopecek2)
pohar1.add_kopecek(kopecek3)
pohar1.add_kopecek(kopecek4)
pohar1.add_kopecek(kopecek5)
pohar1.add_kopecek(kopecek6)

print()
print(pohar1)
print()

print("3-------------------------------------------------------")

class SuperVelkyPohar(VelkyPohar):
    pocitadlo = 7
    # dedim vsechno z Velkeho poharu a menim jenom class variable na novy pocet

kopecek7 = KopecekZrzliny("tresnovy", 12)
kopecek8 = KopecekZrzliny("agrestovy", 13)

pohar2 = SuperVelkyPohar()
pohar2.add_kopecek(kopecek1)
pohar2.add_kopecek(kopecek2)
pohar2.add_kopecek(kopecek3)
pohar2.add_kopecek(kopecek4)
pohar2.add_kopecek(kopecek5)
pohar2.add_kopecek(kopecek6)
pohar2.add_kopecek(kopecek7)
pohar2.add_kopecek(kopecek8)

print(pohar2)