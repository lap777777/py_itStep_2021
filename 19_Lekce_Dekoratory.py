### Decorators ##########################

import time

def obalovaci_funkce(func):
    def obal():

        print("Obalena funkce za chvili zacne")
        func()     # tady beru puvodni funkci a pridavam k ni, to co je pred a za ni
        print("Obalena funkce skoncila")
    return obal  # tady vracim funkci obal

def pozdrav():
    print("Ahoj")

pozdrav = obalovaci_funkce(pozdrav)  
# predavam funkci pozdrav do obalov
# vezmu funkci pozdrav, chci aby delala neco navic (hlasky z obalovaci funkce)

# dekoratory = vezmi funkci a tu jsem odekoroval nejakymi dalsimi parametry (radky 5 a 7)

pozdrav()

print()

# je to dobre napr pro mereni casu - na zacatku si dam start a na konec si dam konec a spostu jak dlouho to trvalo
# misto pozdrav = obalovaci_funkce(pozdrav)

import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        elapsed_time = toc - tic
        print(f"Elapsed time: {elapsed_time:0.4f} seconds")
        return value
    return wrapper_timer

@timer   # decorator na pocitani casu
@obalovaci_funkce  #dekorator
def pozdrav():
    print("Ahoj")

pozdrav()   # tady volam obalenou funkci
print()
