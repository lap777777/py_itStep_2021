# rekurzivni funkce pro factorial:

# 1. iterativni reseni - postupne prochazim range
def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

# 2. rekurzivni reseni - funkce vyuziva predchozich vypoctu
# mam smycku a to musim nejak zastavit - davam podminku pro number == 1:
# funkce vola samu sebe
def factorial_rek(number):
    print(f"pocitam factorial cisla {number}")
    if number == 1:
        return 1
    prubezny_vysledek = factorial_rek(number-1)
    print(f"Spocital jsem faktorial {number-1}, je to {prubezny_vysledek}")
    return number * prubezny_vysledek
# jde to pozpatku 10! = 10 * factorial(9) ... 9 * factorial(8) ... 8 * factorial(7) ... 7 * factorial(6) ...

print(factorial(5))
print(factorial(10))
print()
print(factorial_rek(5))
print(factorial_rek(10))
print()
print()


print("-----------------------------------------------------------------------")

# Fibonaciho rada cisel (1 1 2 3 5 8 13 21 34 55 ...) - rekurzivne:
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)
# ale tohle nepocitat pro velka cisla, zavaril bych program

print(fib(6))
print(fib(10))
print(fib(12))
print()


# rekurzivni funkce dava smysl u stromovych struktur
# napr. pri mazani adresare a jeho podadresaru
