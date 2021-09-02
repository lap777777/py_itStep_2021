print("1---------------------------------------------------------------")
# Task 1
# Implement a class Human. Class fields should store the following: full name, date of birth, contact number, city, country, home address. Implement class methods for data input and output, 
# provide access to individual fields through class methods.

class Human():
    def __init__(self, name, birth, street, city, country, number):
        self.name = name
        self.birth = birth
        self.number = number
        self.city = city
        self.country = country
        self.street = street
    def __str__(self):
        return f"Jmeno: {self.name}\n"\
            f"Datum narozeni: {self.birth}\n"\
            f"Ulice: {self.street}\n"\
            f"Mesto: {self.city}\n"\
            f"Stat: {self.country}\n"\
            f"Telefon: {self.number}\n"\

humans = [
    Human("Petr Novak", "19.04.1978", "U pruhonu 45", "Praha", "CZE", 602435642),
    Human("Josef Skocdopole", "12.12.2000", "Petrklicova 456", "Praha", "CZE",732456566) 
]

for i in humans:
    print(i)

print("2---------------------------------------------------------------")
# Task 2
# Create a class City. Class fields should store the following: city name, region name, country name, number of citizens, zip code, area code. Implement class methods for data input and output, provide access to individual fields through class methods.

class City():
    def __init__(self, name, region, country, population, zip, area_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.zip = zip
        self.area = area_code
    def __str__(self):
        return f"Jmeno mesta: {self.name}\n"\
            f"region: {self.region}\n"\
            f"country: {self.country}\n"\
            f"population: {self.population}\n"\
            f"zip code: {self.zip}\n"\
            f"area code: {self.area}\n"\

praha = City("Praha", "Praha", "CZE", 1500000, 100000, 1)
brno = City("Brno", "Jihomoravsky", "CZE", 500000, 99999, 2)

mesta = [praha, brno]

for i in mesta:
    print(i)

print("3---------------------------------------------------------------")
# Task 3
# Create a class Country. Class fields should store the fol- lowing: country name, continent, population, calling code, capital, city names. Implement class methods for data input and output, provide access to individual fields through class methods.

class Country():
    def __init__(self, name, continent, population, calling_code, capital, city_names):
         self.name = name
         self.continent = continent
         self.population = population
         self.calling_code = calling_code
         self.capital = capital
         self.city_names = city_names
    def __str__(self) -> str:
        return f"Jmeno: {self.name}\n"\
            f"kontinent: {self.continent}\n"\
            f"populace: {self.population:_d}\n"\
            f"volaci kod: {self.calling_code}\n"\
            f"hlavni mesto: {self.capital}\n"\
            f"vyznamna mesta: {self.city_names}\n"

cesko = Country("Ceska Republika", "Evropa", 15000000, "+420", "Praha", ["Brno", "Ostrava"])
slovensko = Country("Slovensko", "Evropa", 5000000, "+421", "Bratislava", ["Kosice", "Nitra"])
usa = Country("USA", "North America", 500000000, "+1", "Washington", ["NY", "LA"])

countries = [cesko, slovensko, usa]
for i in countries:
    print(i)

print("4---------------------------------------------------------------")
# Task 4
# Create a class Fraction. Class fields should store the following: numerator and denominator. Implement class methods for data input and output, provide access to individual fields through class methods. Also, create class methods for arith- metic operations (add, subtract, multiply, divide, etc.).

class Fraction():
    def __init__(self, numerator, denumerator) -> None:
        self.n = numerator
        self.d = denumerator
    def adding(self, n1, d1, n2, d2):
        
        return (self.n[0] / self.d[0]) + (self.n[1] / self.d[1]) 
    def subtract(self, fraction1, fraction2):
        
        return
    def multiply(self):
        return
    def divide(self):
        return