
### ITEROVANI ####################################################################

# daji se oba dole prochazet - iterovat - prochazet for cyklem
my_string = "abcdefgh"
my_list = ["a", "b", "c", "d", "e", "f", "g", "h"]

[print(i) for i in my_list]

print()
# co nelze iterovat - pres cislo
# try:
#     for x in 8:
# except TypeError as e:
#     print("nelze iterovat pres cislo")
#     print(e)
# print()

for x in range(8):
    print(x)
# pres range se da iterovat - je to class range(start, stop[,step])
print()

### Iterovani pres funkci - pomoci yield

def my_iterrable():
    print("Ja jsem generator (generuji hodnoty pres ktere se da iterovat)")
    print("neto taky iterovatelna,")
    print("coz neni uplne synonymum")
    yield 5
    print("po prvnim returnu/yieldu")
    yield 6
    print("po druhem yieldu")
    yield 7
    print("funkce konci")
    # diky yield se da iterovat funkce - vraci vice hodnot 

for x in my_iterrable():
    print("ted jsem ve for cyklu - zacatek")
    print(f"z iterace se vratilo: {x}")
    print("ted jsem ve for cyklu - konec")

### Iterovani pres tridu

class MyIterator():
    """
    trida iteruje pres retezec pozpatku
    """
    def __init__(self, string):
        self.string = string
    
    def __iter__(self):    # podtrzitkova metoda ktera urci zacatek iterace a co se bude prochazet
        self.index = len(self.string)
        return self
    
    def __next__(self):  # pres tuto metodu se spusti iterace
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.string[self.index]

for x in MyIterator("jablko"):
    print(x)
print()


class NekonecnyCyklus():
    def __iter__(self):     # zacatek iterace - prvni for se pta umis iterovat - metoda iter rika, umim
        return self

    def __next__(self):    # next se spousti, kdyz for cyklus chce dalsi hodnotu a zastavi to vyjimka a ta tady neni
        return None

# for x in NekonecnyCyklus():
#     print(x)

# vlastni pocitadlo
class Pocitadlo():
    def __iter__(self):
        self.pocitadlo = 11
        return self

    def __next__(self):
        self.pocitadlo -= 1
        if self.pocitadlo == 0:
            raise StopIteration
        return self.pocitadlo

for x in Pocitadlo():
    print(x)
print()

def retezec_pozadu(my_string):
    index = len(my_string)
    while index >0:
        index -= 1
        yield my_string[index]

for x in retezec_pozadu("hruska"):     # generator function
    print(x)
print()

### Funkce enumarate

for x in enumerate("chameleon"):
    print(x)
# funkce vraci dva vysledky - index a polozku
print()