# zadani:
# https://github.com/trohat/python1-ukoly/blob/main/OOP-1.txt

print("1--------------------------------------------------")
# Task 1
# Vytvorte tridu kopecek_zmrzliny. Kopecek bude mit jednu vlastno a to prichut. Zaridte aby se pekne vypisovala
# Vytvorte tridu zmzlinovay_pohar.
# Pohar muze mit libovolne mnozstvi kopecku, pri inicializaci nema ani jeden
# vytvorte uvnitr poharu metodu na pridavani kopecku.
# napr. pohar1.pridej_kopecek(kopecek1)
# zaridte aby se trida zmrzlinovy_pohar pekne vypisovala

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
    def __init__(self):
        self.kopecky = []
    
    def add_kopecek(self, kopecek):
        self.kopecky.append(kopecek)

    def __str__(self) -> str:
        result = f"Pohar obsahuje {len(self.kopecky)} kopecky/u.\n"
        for kopecek in self.kopecky:
            result += f"\tprichut: {kopecek.flavour}\n"
        return result

    def total_price(self):
        total = 0
        for kopecek in self.kopecky:
            total += kopecek.price
        return f"Celkova cena: {total} CZK."

    def get_info1(self):
        result = f"Pohar obsahuje {len(self.kopecky)} kopecky/u:\n"
        result += ", ".join(kopecek.flavour for kopecek in self.kopecky).capitalize()
        result += f".\nZaplat: {self.total_price()}\n" 
        result += f"Dobrou chut!"
        return result

    def get_info(self):
        my_count = 1
        print(f"Pohar ma {len(self.kopecky)} kopecky/u:")
        for i in self.kopecky:
            # vola funkci str z tridy KopecekZmrzliny
            # pokud bych chtel jenom prichut, tak do str musim dat pouze prichut a zadny text kolem
            print(f"{my_count}. {i}")
            my_count += 1

kopecek1 = KopecekZrzliny("jahodovy", 10)
kopecek2 = KopecekZrzliny("citronovy", 12)
kopecek3 = KopecekZrzliny("cokoladovy", 13)
print(kopecek1)
print(kopecek2)
print(kopecek3)
print()

pohar = PoharZmrzliny()
pohar.add_kopecek(kopecek1)
pohar.add_kopecek(kopecek2)
pohar.add_kopecek(kopecek3)
print(pohar)
print()
pohar.get_info()
print()
print(pohar.get_info1())
print()
print(pohar.total_price())
print()

# zeptat se na doctring tridy:
print(PoharZmrzliny.__doc__)

print("2,3,4-----------------------------------------------")
# Task 2
# Vytvorte tridu kniha, kniha ma nazev, authora a cenu.
# vytvorte tridu policka na knihy. Na zacatku je prazdna
# vytvorte metodu pridej knihu
# vytvorte metodu celkova cena, ktera spocte cenu vsech knih v policce

# Task 3
# Na třídě PolickaNaKnihy vytvořte metodu mame_knihu, která vrátí True nebo False, podle toho, zda se daná kniha v poličce nachází.

# Task 4
# (Další pokračování ke 2)
# Ke třídě kniha přidejte vlastnost šířka (knihy).
# Ke třídš PolickaNaKnihy také přidejte vlastnost šířka (poličky).
# Pokaždé, když přidáváte knihu do poličky, zkontrolujte, jestli
# se tam ta kniha vejde. Pokud ne, oznamte to uživateli.

class Book():
    def __init__(self, title, author, price, size):
        self.title = title
        self.author = author
        self.price = price
        self.size = size
    def __str__(self):
        return f"Kniha: {self.title}, autor: {self.author}, cena: {self.price}"

class Bookshelf():
    def __init__(self):
        self.knihovna = []
        self.size = 100
        self.size_occ = 0

    def __str__(self):
        result = "Policka na knihy obsahuje: \n"
        for i in self.knihovna:
            result += f"\t {i} \n"
        result += f"Celkova cena knih: {self.total_price()} CZK."
        return result
    
    def get_info(self):
        result = "Policka obsahuje:\n"
        for i in self.knihovna:
            result += f"\t{i.title}\n"
        return result

    def get_info2(self):
        result = "Policka obsahuje knihy:\n"
        result += ", ".join(i.title for i in self.knihovna)
        result += f"\nCelkova cena knih: {self.total_price()} CZK.\n"
        return result

    def add_book(self, book):
        kapacita = self.size-self.size_occ
        self.size_occ += book.size
        if self.size_occ <= self.size:
            self.knihovna.append(book)
            print(f"Kniha {book.title} uspesne pridana do knihovny")
        else:
            print(f"Knihu {book.title} nelze pridat do knihovny.")
            print("Kapacity knihovny vycerpana")
            print(f"Kniha ma sirku: {book.size} cm")
            print(f"V knihovne zbyva pouze {kapacita} cm mista.")

    def total_price(self):
        my_total = 0
        for i in self.knihovna:
            my_total += i.price
        return my_total
    
    def is_in_bookshelf(self, kniha):
        if kniha in self.knihovna:
            return True
        else:
            return False

    # na tohle se zeptat, jestli to nejde nejak lepe
    def is_in_bookshelf2(self, nazev):
        my_list = [i.title for i in self.knihovna]
        if nazev in my_list:
            return True
        else:
            return False

kniha1 = Book("RUR", "Karel Capek", 199, 30)
kniha2 = Book("Babicka", "Bozena Nemcova", 299, 60)
kniha3 = Book("Kytice", "Karel Jaromir Erben", 99, 10)
print(kniha1)
print(kniha2)
print(kniha3)
print()

knihovna = Bookshelf()
knihovna.add_book(kniha1)
knihovna.add_book(kniha2)
knihovna.add_book(kniha3)
print()
print(knihovna)
print()
print(knihovna.get_info())
print(knihovna.get_info2())

je_tam = knihovna.is_in_bookshelf(kniha1)
print(je_tam)
je_tam2 = knihovna.is_in_bookshelf2("RUR")
print(je_tam2)
print()

kniha4 = Book("Maj", "Karel Hynek Macha", 99, 5)
knihovna.add_book(kniha3)
print()
