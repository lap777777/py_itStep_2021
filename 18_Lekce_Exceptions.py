### EXCEPTIONS #########################################

# raise exeption - vyhodit vyjimku
# raise IndexError("zas tak nic hrozneho se nestalo")
# LBYL = look before you leap - osetreni pres if (podminky)
# EAFP = easier to ask forgiveness than persmission - osetreni pres vyjimky

while True:
    try:
        cislo1 = int(input("zadej cislo: "))
        cislo2 = int(input("zadej cislo: "))
        vysledek = cislo1/cislo2
        print(f"{cislo1} / {cislo2} = {vysledek}")
        break
    except ValueError:
        print("Nebylo zadano cislo.")
    except ZeroDivisionError as e:     # ulozeni chyby do promenne
        print(e)                       # vytisknu chybu ZeroDivisionError
    except:
        print("Nejaka necekana chyba.")

print("Program pokracuje.")


# ZeroDivisionError - chyba deleni nulou
# ValueError - chyba pri deleni nulou 


class TooManyEmployersException(Exception):
    pass
# vytvoreni vlastni vyjimky na zaklade tridy Exception
# str je tam automaticky z tridy exception
# takze ji definuji prazdnou

employers = 500

def delej_neco_jineho():
    if employers > 400:
        raise TooManyEmployersException

def delej_neco():
    delej_neco_jineho()

try:
    delej_neco() # pokud chyba, tak spadne tato funkce a vnorena funkce, vyhodi se vyjimka nize a program pokracuje.
    # mam misto, kde chybu kontroluji a jine misto, kde ji vytisknu

except TooManyEmployersException: 
    # a teprve tady mi to vyhodi vyjimku
    print("Hodne lidi, nedostatecna kapacita")

# napr muzu pridat text - moc zamenstancu, nevejdou se do officu
# nahrazuje mi podminky (if)
# vlastni vyjimka pro pripady - napr. do klece uz se nevejdou dalsi zvirata nebo do poharu se nepridaji dalsi kopecky
"""
class PrilisMnohoKopeckuException(Exception):
    def __str__(self):
        return "Pohar je plny, nejdou pridat dalsi kopecky."

if len(pohar1) > 10:
    raise PrilosMnohoKopeckuException

try: 
    pohar1.prodej_kopecek(kopecek)
except PrilosMnohoKopeckuException as e:
    print(e)
"""

