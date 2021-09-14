# FUNKCE
# pouziji si pro kod, ktery chci opakovat vickrat v programu
# DRY = don`t repeat yourself

def pozdrav(jmeno):             # parametr funkce - jmeno
    print(f"Ahoj, {jmeno}")
    print("Odloz si obleceni do satniku.")
    print("Obcerstveni je v kuchyni.")
    print("Dobre se bav.")
    print()

pozdrav("Pavle")   # argument - jmeno
pozdrav("Katko")
pozdrav("Karle")


def scitani(a, b):
    print(f"Soucet cisel: {a} + {b} = {a + b}")

scitani(5, 6)
print()

def scitani1(a, b):
    soucet = a + b
    return soucet          # return vraci hodnotu, muzu si ulozit do promenne nebo vytisknout

soucet = scitani1(5, 6)
print(soucet)
print()

# default parameter - kdyz nezadam parametr, tak aby nehodilo chybu
def pozdrav(jmeno="anonymni osobo"):             # parametr funkce - jmeno
    print(f"Ahoj, {jmeno}")
    print("Odloz si obleceni do satniku.")
    print("Obcerstveni je v kuchyni.")
    print("Dobre se bav.")
    print()

pozdrav()
pozdrav("Petre")

def pozdrav(jmeno=""):             # parametr funkce - jmeno
    if jmeno != "":
        print(f"Ahoj, {jmeno}")
    print("Odloz si obleceni do satniku.")
    print("Obcerstveni je v kuchyni.")
    print("Dobre se bav.")
    print()

pozdrav()
pozdrav("Petre")

def scitej(*tuple):    # kdyz dam pres parametru *, tak od udela z argumentu tuple (n-tice)
    return sum(tuple)

soucet = scitej(1,2,3,4,5,6,7,8)
print(f"soucet n-tice: {soucet}")
print()

def scitej(prvni, druhy, *args):    # 1 jde do prvniho, 2 jde do druhe, zbytek cisel se nasypal do args
    print(f"N-tice jmenem args vypada takhle: {args}")

scitej(1,2,3,4,5,6,7,8)
scitej(1, [2, 3, 4], 6,7,8)
print()

def scitej(prvni, druhy, *args, **kwargs):    
    # *args - tam nasyp zbyle pozicni
    # **kwargs - tan nasyp ty, co maji keywords
    # normalni parametry jsou positional - jsou podle pozice
    # *args a *kwargs jsou keywords parameters
    print(f"N-tice jmenem args vypada takhle: {args}")
    print(f"Slovnik jmenem kwargs vypada takhle {kwargs}")

scitej(1, [2, 3, 4], 5, 6, 7, a=5, b=6, c=6)
print()


# sdruzeni funkci - muzu funkce mit jako parametr jine funkce a rozhodovat, ktera se pouzije
def transform_sentence(sentence, transform_fn):
    sentence = sentence.split()
    result = []
    for word in sentence:
        result.append(transform_fn(word))
    return " ".join(result)

def tupa_funkce(word):
    return f"{word}tupa"

def dvakrat(word):
    return word + word

print(transform_sentence("this is a test", tupa_funkce))
print(transform_sentence("this is a test", dvakrat))
print("----------------------------------------------------------")

def funkce():
    return 5

a = funkce     # a prirazuji celou funkci, bude vracet objekt
b = funkce()   # volam funkci, v b bude ulozeny vysledek - 5

class Zvire:
    pass

d = Zvire()   # volam tridu - vytvori instanci
e = Zvire     # vraci tridu / ulozil jsem objekt tridu do e
