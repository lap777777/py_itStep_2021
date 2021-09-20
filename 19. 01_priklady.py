print("1----------------------------------------------------")
# Task 1
# napis vlastni funkci enumerate:
print("### A) #######")
for x in enumerate("chameleon"):
    print(x)
# funkce vraci dva vysledky - index a polozku
print()

print("### B) #######")
[print(x) for x in enumerate("chameleon")]
print()

print("### C) #######")
def my_enumerate1(my_string):
    for i in range(len(my_string)):
        yield f'({i}, "{my_string[i]}")'

for i in my_enumerate1("chameleon"):
    print(i)
print()

print("### D) #######")
def my_enumerate2(my_string):
    index = 0
    while index < len(my_string):
        yield f'({index}, "{my_string[index]}")'
        index += 1

for i in my_enumerate2("chameleon"):
    print(i)
print()


print("2----------------------------------------------------")
# Task 2
# pracuj v samostatnem adresari:
# Napis generatorovou funkci, ktera projde vsechny soubory v danem adresari a z kazdeho vraci postupne radek po radku (tj. v kazde iteraci jeden radek)
# Napoveda: mohla by se vam hodit metoda os.listdir() z modulu os
import os, sys

def read_lines():
    path = "19_Lekce/"
    dirs = os.listdir(path)
    my_file = 0
    my_line = 0
    for file in dirs:
        my_file += 1
        print(f"Tisknu data z {my_file}. souboru:")
        print()
        with open(f"19_Lekce/{file}") as f:
            for line in f:
                my_line += 1
                print(f"Tisknu {my_line}. radek:")
                yield line
                print()
        my_line = 0
        print("******************************")
        print()

for i in read_lines():
    print(i, end="")


print("3----------------------------------------------------")
# Task 3
# pokud si pamatujete, jak se iteruje pomoci tridy
# (podtrzitkove tridy __iter__ a __next__),
# prepiste ukol 1 pomoci tridy.

class MyEnumerator():
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        self.index = -1
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.string):
            raise StopIteration
        return f'({self.index}, {self.string[self.index]}")'

for i in MyEnumerator("chameleon"):
    print(i)
print()

print("4----------------------------------------------------")
# Task 4
# napiste funkci, ktera funguje jako vestavena funkce range
# napoveda: bude to generatorova funkce

def my_range(start, end, step=1):
    index = start
    if step > 0:
        while index < end:
            yield index
            index += step
    elif step < 0:
        while index > end:
            yield index
            index += step

for i in my_range(10, 20):
    print(i)
print()

for i in my_range(20, 10, -1):
    print(i) 
print()
