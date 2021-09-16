### Lampda funkce

def double(x):
    return x + x

def nadruhou(x):
    return x ** 2

def half3(x):
    return x / 2

def minus_two(x):
    return x - 2

# vytvoril jsem hodne funkci, ktere delaji nejakou jednoduchou operaci
# je to hodne manualni prace
# jde to napsat jednoduseji - pomoci lambda funkce - zkraceny zapis funkce
# syntaxe nazev = lambda parametry: co bude returnova


double = lambda x : x + x
nadruhou = lambda x : x ** 2
half3 = lambda x : x / 2
minus_two = lambda x : x - 2


secti = lambda x, y : x + y

konstanta = lambda : 5
# jednoducha funkce, ktera vraci 5
# stejne jako:
def konstanta():
    return 5

