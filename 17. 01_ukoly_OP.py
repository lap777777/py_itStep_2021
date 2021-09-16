# Task 1

# Vytvorte tridu zvire
# trida zvire ma nasledujici atributy: pocet nohou, barvu
# trida zvire ma nasledujici metody: vydej_zvuk - ta nic nedela, obecne zvire zvuk nevydava

class Animal():
    def __init__(self, no_legs, color) -> None:
        self.no_legs = no_legs
        self.color = color
    def __str__(self) -> str:
        return f"Animal has {self.no_legs} legs and {self.color} color."
    def make_sound(self):
        return " "
    def animal_short_export(self):
        text = f" has {self.no_legs} legs and {self.color} color."
        return text

# Vytvor nekolik trid na konkretni zvirata - napr. Pes, Kocka, Zirafa, Tyger, ... hodi se trida Had protote ten ma 0 nohou
# kazda nova trida bude mit neco navic - atribut nebo metodu = napr. pes muze mit atribut rasu nebo metodu hlidej_barak (dohromady vytvorte aspon jednu metodu a aspon jeden atribut)
# Kazdy potomek zvirete zaroven prepise (pretizi) metodu vydej_zvuk po svem (napr. pes zasteka)
# vytvorte nekolik instanci ruznych zvirat.
# dodelejte ke zviratum metodu __str__ nebo __repr__ aby se hezky vypisovaly. Zamyslete se, jestli se hodi vic k predkovi zvire nebo potomkum (obe varianty jsou ok)

class Tiger(Animal):
    def __init__(self, no_legs, color, kind, age, food):
        super().__init__(no_legs, color)
        self.kind = kind
        self.age = age
        self.food = food
    def __str__(self) -> str:
        text = f"Animal is a {self.kind}.\n" 
        text += super().__str__()
        text += f"\n{self.kind.capitalize()} is {self.age} years old.\n"
        text += f"Its favourite food is {self.food}."
        return text
    def make_sound(self):
        return f"Grrrrrrrrrrrrrrrrrrr"
    # definovat funkci vypis kratce - na zvireti - napr ja jsem hneda ovce neb pouzit repr(zvire1)
   
class Crocodile(Animal):
    def __init__(self, no_legs, color, kind, location):
        super().__init__(no_legs, color)
        self.kind = kind
        self.location = location
    def __str__(self) -> str:
        text = f"Animal is a {self.kind}.\n" 
        text += super().__str__()
        text += f"\nIts location is {self.location}."
        return text
    def make_sound(self):
        return f"huaaaaaaaaa"

class Snake(Animal):
    def __init__(self, no_legs, color, kind, type):
        super().__init__(no_legs, color)
        self.kind = kind
        self.type = type
    def __str__(self) -> str:
        text = f"Animal is a {self.kind}.\n" 
        text += super().__str__()
        text += f"\nIt is a {self.type} snake."
        return text
    def make_sound(self):
        return f"sssssssssssssssssss"

class Kangaroo(Animal):
    def __init__(self, no_legs, color, kind, no_children) -> None:
        super().__init__(no_legs, color)
        self.kind = kind
        self.no_children = no_children
    def __str__(self) -> str:
        mother = super().__str__()
        text = f'{self.kind.capitalize()}: {mother}'
        text = text.replace("Animal", "animal")
        # text = f"Animal is a {self.kind}.\n" 
        # text += super().__str__()
        # text += f"\nIt has {self.no_children} child/children."
        return text
    def make_sound(self):
        return f"uab uab uab uab"

tiger1 = Tiger(4, "white", "polar tiger", 10, "polar fox meat")
tiger2 = Tiger(4, "black/white/orange", "bengal tiger", 9, "monkeys")
print(tiger1)
print(tiger1.make_sound())
print(tiger2)
print()

crocodile1 = Crocodile(4, "green", "aligator", "Florida")
crocodile2 = Crocodile(4, "brown", "crocodile", "Egypt")
print(crocodile1)
print(crocodile1.make_sound())
print(crocodile2)
print()
   
snake1 = Snake(0, "green", "snake A", "poisonous")
snake2 = Snake(0, "black", "snake B", "strangler")
print(snake1)
print(snake1.make_sound())
print(snake2)
print()

kangaroo1 = Kangaroo(2, "brown", "kangaroo A", 1)
kangaroo2 = Kangaroo(2, "orange", "kangaroo B", 2)
print(kangaroo1)
print(kangaroo1.make_sound())
print(kangaroo2)
print()

# vytvorte si seznam (list) a ulozte do nej nekolik instanci ruznych zvirat. Pak seznam projdete cyklem a nechte kazde zvire o sobe nahlas vedet (zavolejte metodu vydej_zvuk)
animal_list = [tiger1, kangaroo1, snake1, crocodile1]
for i in animal_list:
    print(f'{i.kind.capitalize()} makes following sound: \n\t"{i.make_sound()}"".')
print()

# vytvorte tridu Klec. Do klece se vejde nekolik zvirat (jako kopecky do poharu)
# zaridte aby se klec hezky vypisovala vcetne zvirat vevnitr (budeme to potrebovat pozdeji)
# vytvorte nekolik instanci kleci a umistete do nich nektere z uz vytvorenych zvirat.
# Vsuvka pro pokrocile: Metoda pridej_zvire muze mit vice parametru (vice ruznych zvirat a prida je vsechny)
class Cage():
    def __init__(self, name):
        self.name = name
        self.cage_list = []

    def add_animal(self, *args):
        for i in args:
            self.cage_list.append(i)
        self.cage_list = [i for i in args]
        text = f"Nasledujici zvirata uspesne pridana:\n"
        for i in args:
            text += f"{i.kind}, "
        text = text.rstrip(", ")
        text += "."
        print(text)

    def __str__(self):
        text = f"Cage {self.name} contains following animals: \n"
        text += "\t"
        for i in self.cage_list:
            text += f"{i.kind}, "
        text = text.rstrip(", ")
        text += "."
        return text

cage1 = Cage("Sever")
cage2 = Cage("Zapad")
cage3 = Cage("Jih")
cage1.add_animal(tiger1, snake1, kangaroo1)
cage2.add_animal(tiger2, snake2)
cage3.add_animal(tiger2, snake2, crocodile1)
print()
# vypis dle tridy cage
print(cage1)
print(cage2)
print(cage3)
print()

# vytvorte tridu Zoo. Do zoo se vejde nekolik kleci. 

class Zoo():
    def __init__(self) -> None:
        self.zoo_list = []

    # vytvorte metodu pridej_klec na pridani klece do zoo.
    # vsuvka pro pokrocile. Metoda prijde_klec umi pridat nekolik kleci najednou)
    def add_cage(self, cage):
        if isinstance(cage, list):
            for i in cage:
                self.zoo_list.append(i)
                print(f"Cage {i.name} added.")
        else:
            self.zoo_list.append(cage)
            print(f"Cage {cage.name} added.")

    # trida zoo se umi hezky vypisovat (vypise klece a zvirata v nich)
    def __str__(self) -> str:
        # a) vypis kleci
        text = f"Zoo contains following cages: \n"
        text += f"\t"
        # b) vypis zvirat v klecich
        for i in self.zoo_list:
            text += f"{i.name}, "
        text = text.rstrip(", ")
        text += ".\n"
        # vypis jednotlivych zirat - pouzivam kratkou funkci pro vypis ze tridy animal
        for i in self.zoo_list:
            text += f"{i}\n"
            for j in i.cage_list:
                text += f"\t\t{j.kind.capitalize()} {j.animal_short_export()}\n"
        return text
    
    # vytvorte metodu vypis_podle_barvy, ktera projde cele zoo (vsechny klece a zvirata v nich) a vypise jen zvirata z urcitou barvou (barvu dostane jako parametr)
    def export_by_color(self, color):
        my_count = 0
        text = f"In the zoo there are following animals with {color} color: \n"
        for i in self.zoo_list:
            for j in i.cage_list:
                if j.color == color:
                    text += f"{j}\n\n"   # vypis dle str pro zvi5e - dlouhy vypis
                    my_count += 1
        if my_count > 0:
            return text
        else:
            return f"There is no animal with {color} color in the zoo."
    
    # vytvorte metodu vypis_podle_nohou, ktera projde celou zoo a vypise jen zvirata se zadanym poctem nohou (ten dostane jako parametr)
    def export_by_legs(self, legs):
        my_count = 0
        text = f"In zoo there are following animals with {legs} legs: \n"
        for i in self.zoo_list:
            for j in i.cage_list:
                if j.no_legs == legs:
                    text += f"\t{j.kind.capitalize()} {j.animal_short_export()}\n"   # vypis dle kratke funkce pro vypis
                    my_count += 1
        text += f"\n"
        if my_count > 0:
            return text
        else:
            return f"There is no animal with {legs} legs in the zoo."

    # do zoo prijel sponzor. chce vsem zviratum koupit ponozky. Vytvorte metodu spocitej nohy, ktera projde vsechny klece a a spocita pocet nohou v cele zoo.
    def count_legs(self):
        my_sum = 0
        for i in self.zoo_list:
            for j in i.cage_list:
                my_sum += j.no_legs
        return f"There are {my_sum} legs in the zoo."

    # vypis zvirat by mel vyuzit funkci pro strucny vypis ze tridy animal. 
    def zoo_short_export(self) -> str:
        text = "Zoo cointains following animals: \n"
        for i in self.zoo_list:
            for j in i.cage_list:
                text += f'\t{j.kind.capitalize()} {j.animal_short_export()}\n'
        return text

    # vypis zvirat by mel vyuzit funkci pro strucny vypis ze tridy animal. 
    def __repr__(self) -> str:
        text = "Zoo cointains following animals: \n"
        for i in self.zoo_list:
            for j in i.cage_list:
                text += f'\t{j.kind.capitalize()}: {Animal.__str__(j).replace("Animal", "animal")}\n'
                #text += f'{j.kind}: {super().__str__().replace("Animal", "animal")}\n'
        return text
        
zoo = Zoo()
cage_list = [cage1, cage2]
zoo.add_cage(cage_list)
# zoo.add_cage(cage1)
# zoo.add_cage(cage2)
zoo.add_cage(cage3)
print()
print(zoo)
print()
print(zoo.export_by_color("green"))
print(zoo.export_by_color("pink"))
print()
print(zoo.export_by_legs(4))
print(zoo.export_by_legs(10))
print()
print(zoo.count_legs())
print()
print(zoo.zoo_short_export())
print()
print(repr(zoo))
print()


# do Zoo doplnit iterovani pres zvire




