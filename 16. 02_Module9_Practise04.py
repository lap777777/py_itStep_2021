print("1---------------------------------------------------")
# Task 1
# Create a class Human that will contain info about a human.
# Use inheritance to create a Builder class (contains info about a builder), a Sailor class (contains info about a sailor), a Pilot class (contains info about a pilot).
# Each class must have the required methods.

class Human():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        return f"Human {self.name} {self.surname} is {self.age} years old"

class Builder(Human):
    def __init__(self, name, surname, age, license):
        super().__init__(name, surname, age)
        self.license = license
    def __str__(self):
        text = super().__str__()
        return text + f"\nHe/she is a builder and has the license: {self.license}."

class Sailor(Human):
    def __init__(self, name, surname, age, license):
        super().__init__(name, surname, age)
        self.license = license
    def __str__(self):
        text = super().__str__()
        return text + f"\nHe/she is a sailor and has the license:: {self.license}."

class Pilot(Human):
    def __init__(self, name, surname, age, license):
        super().__init__(name, surname, age)
        self.license = license
    def __str__(self):
        text = super().__str__()
        return text + f"\nHe/she is a builder and has the license: {self.license}."

builder = Builder("Petr", "Pavel", 45, "Lego")
sailor = Sailor("Josef", "Briza", 35, "Parnik")
pilot = Pilot("Jaromir", "Vlastovka", 56, "APL")
print(builder)
print()
print(sailor)
print()
print(pilot)
print()

print("2---------------------------------------------------")
# Task 2
# Create a class Passport that will contain passport information about a  citizen of a given country.
# Use inheritance to create a ForeignPassport class derived from Passport.
# Recall that a foreign passport has not only passport infor mation but also  data on visas and the number of the foreign passport.
# Each class must have the required methods.

class Passport():
    def __init__(self, name, surname, country) -> None:
        self.name = name
        self.surname = surname
        self.country = country
    def __str__(self):
        return f"{self.name} {self.surname} is a citizen of {self.country}."

class ForeignPassport(Passport):
    def __init__(self, name, surname, country, number):
        super().__init__(name, surname, country)
        self.number = number
        self.visa_dict = {}
        
    def add_visa(self, key, value):
        self.visa_dict[key] = value

    def __str__(self):
        text = super().__str__()
        text += f"\nPassport number: {self.number}.\n"
        for key, value in self.visa_dict.items():
            text += f"visa to: {key}, valid till: {value}\n"
        return text
            
petr = ForeignPassport("Petr", "Pavel", "CZE", "4567582")
petr.add_visa("US", "31.12.2030")
petr.add_visa("AUS", "15.03.2029")

print(petr)

print("3---------------------------------------------------")
# Task 3
# Create a base class Animal and derived classes Tiger, Crocodile, Kangaroo.   
# Use a constructor to set the name of each animal and its characteristics. 
# Create the required methods and fields for each class.

class Animal():
    def __init__(self, name, kind, age, location):
        self.name = name
        self.kind = kind
        self.age = age
        self.location = location
    def __str__(self) -> str:
        return f"{self.name} is a {self.kind}.\n"\
            f'It is {self.age} years old and lives in {self.location}.'

class Tiger(Animal):
    def __init__(self, name, kind, age, location, color, children, food):
        super().__init__(name, kind, age, location)
        self.color = color
        self.children = children
        self.food = food
    def __str__(self) -> str:
        text = super().__str__()
        text += f"\nIt has {self.color} color.\n"
        text += f"It has {self.children} children\n"
        text += f"Its favourite food is {self.food}\n"
        return text

class Crocodile(Animal):
    def __init__(self, name, kind, age, location, no_teeth, food):
        super().__init__(name, kind, age, location)
        self.no_teeth = no_teeth
        self.food = food
    def __str__(self) -> str:
        text = super().__str__()
        text += f"It has {self.no_teeth} teth.\n"
        text += f"Its favourite food is {self.food}\n"
        return text

class Kangaroo(Animal):
    def __init__(self, name, kind, age, location, no_children, food):
        super().__init__(name, kind, age, location)
        self.no_children = no_children
        self.food = food
    def __str__(self) -> str:
        text = super().__str__()
        text += f"It has {self.no_teeth} teth.\n"
        text += f"Its favourite food is {self.food}\n"
        return text

tiger = Tiger("Divocak", "tygr", 10, "Siberia", "white", 2, "polar fox")
print(tiger)
krokodyl = Crocodile("Podvodnik", "crocodile", 5, "Florida", "1000", "fish")
print(krokodyl)
klokan = Crocodile("Skipy", "klokan", 12, "Australia", "1", "grass")
print(klokan)