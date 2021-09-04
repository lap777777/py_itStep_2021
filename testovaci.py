
class Book():
    def __init__(self, title, author, price, size) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.size = size
    def __str__(self) -> str:
        return f"Kniha {self.title}, autor: {self.author}, cena: {self.price} CZK, sirka {self.size}."

class Bookshelf():
    def __init__(self) -> None:
        self.policka = []
        self.shelf_size = 100
        self.shelf_size_used = 0

    def add_book(self, book):
        zabrano = self.shelf_size - self.shelf_size_used
        self.shelf_size_used += book.size
        if self.shelf_size_used <= self.shelf_size:
            self.policka.append(book)
            print(f"Kniha {book.title} uspesne pridana.")
        else:
            print(f"V knihovne zbyva {zabrano} cm mista\nZadana kniha ma sirku {book.size} cm\nKnihu nelze pridat do knihovny")

    def total_price(self):
        total = sum(i.price for i in self.policka)
        return f"Celkova cena {total} CZK."

    def __str__(self):
        result = "Policka obsahuje nasledujici knihy:\n"
        result += ", ".join(i.title for i in self.policka)
        result += f"\n{self.total_price()}"
        return result

    def is_in_bookshelf(self, nazev):
        for i in self.policka:
            if nazev == i.title:
                return True
        return False


kniha1 = Book("RUR", "Karel Capek", 199, 30)
kniha2 = Book("Babicka", "Bozena Nemcova", 299, 60)
kniha3 = Book("Kytice", "Karel Jaromir Erben", 99, 10)
print(kniha1)
print(kniha2)
print(kniha3)
print()
policka = Bookshelf()
policka.add_book(kniha1)
policka.add_book(kniha2)
policka.add_book(kniha3)
print()
print(policka)
print()

print(policka.is_in_bookshelf("RUR"))
print(policka.is_in_bookshelf("Don Quichot"))
print()

kniha4 = Book("Ostrava", "Ivan Bezruc", 39, 20)
policka.add_book(kniha4)
print()



