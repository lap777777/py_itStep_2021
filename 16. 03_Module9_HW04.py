print("1-------------------------------------------------------")
# Task 1
# Create a Device class containing information about a device.
# Use inheritance to implement a CoffeeMachine class (contains info about a coffee machine), a Blender class (contains info about a blender), a MeatGrinder class (contains info about a meat grinder).
# Each class must have the required methods.


print("2-------------------------------------------------------")
# Task 2
# Create a Ship class containing information about a ship.
# Use inheritance to implement a Frigate class (contains info about a frigate), a Destroyer class (contains info about a destroyer), a Cruiser class (contains info about a cruiser).
# Each class must have the required methods.


print("3-------------------------------------------------------")
# Task 3
# Create a Money class for working with money (the class object operates with one currency).
# The class must provide a field for storing an integer part (dollars, euros, hryvnias, etc.) and a field for storing a fracional part (cents, euro cents, kopecks, etc.)
# Implement methods for printing amounts and setting values for parts (integer and fractioanl).
# Based on the Money class, create a Product class. Implement a method that allows you to decrease the price by a specified number.
# Implement methods and fields required for each class.

class Money():
    def __init__(self, currency, amount, amount_fract) -> None:
        self.currency = currency
        self.amount = amount
        self.amount_fract = amount_fract
        self.price = self.amount + self.amount_fract/100

    def __str__(self) -> str:
        return f"Product price is {self.price} {self.currency}."


class Product(Money):
    def __init__(self, name, color, currency, amount, amount_fract) -> None:
        super().__init__(currency, amount, amount_fract)
        self.name = name
        self.color = color

    def change_price(self, zmena):
        price1 = self.price  # puvodni cena
        self.price += zmena  # cena po sleve, po navyseni
        price2 = self.price                          
        # rozseknuti ceny na cenu pred a po desetinne carce
        self.amount = self.price // 1
        self.amount_fract = price2 - self.amount
        self.zmena = ((price2 - price1)/price1) * 100
        if zmena < 0:
            print(f"Provided discount: {self.zmena * -1:.2f}%.")
        elif zmena > 0:
            print(f"Increased price by: {self.zmena:.2f}%.")
        else:
            return "Chybne zadani"

    def __str__(self) -> str:
        text = f"Product {self.name} has {self.color} color.\n"
        text += super().__str__()
        return text


kavovar = Product("Coffee machine", "red", "EUR", 50, 25)
print(kavovar)
print()
kavovar.change_price(10.56)
print(kavovar)
print()
kavovar.change_price(-20.56)
print(kavovar)
print()

