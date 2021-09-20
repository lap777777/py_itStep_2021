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
# __str__ je tam automaticky z tridy exception
# takze ji definuji prazdnou

employers = 500

def delej_neco_jineho():
    if employers > 400:
        raise TooManyEmployersException

def delej_neco():
    delej_neco_jineho() 

try:
    delej_neco() # pokud chyba, tak spadne tato funkce a vnorena funkce, vyhodi se vyjimka nize a program pokracuje.
    # tady mam misto, kde chybu kontroluji a dale mam jine misto, kde ji vytisknu

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
print("------------------------------------------------------------------------")
print()

### Collections ####################################################

# 1) Counter - pocitadlo 

from collections  import Counter

# pocita, co do nej vlozim - potrebuje neco, pres co se da iterovat - text, slovnik, seznam, .....

c = Counter("abcdefghaaa")
print(c)
print()

c1 = Counter("abrakadabra")["a"]  # vrati kolikrat je acko v zadanem retezci
print(c1)

cnt = Counter()
text = "Sla nanynka do zeli, natrhala lupeni a pak sla domu a vsechno to snedla."
my_list = text.split(" ")
for word in my_list:
    cnt[word] += 1
print(cnt)
print()
print("------------------------------------------------------------------------")
print()

# 2) defaultDict
# dictionary subclass that calls a factory function to supply missing values
# slovnik ktery vrati factory argument jako hodnotu a nevrati KeyError pro chybejici klic

from collections import defaultdict

# lambda as default_factory argument
d = defaultdict(lambda : 0)   # lambda vyhodi konstantu 0 tam, kde neni klic na ktery se ptam

d["a"] = 1
d["b"] = 2
 
print(d)
print(d["a"])
print(d["b"])
print(d["c"])
print()
print("------------------------------------------------------------------------")
print()

### dalsi podtrzitkove metody #######################################

class Cislo():
    def __init__(self, cislo):
        self.cislo = cislo
    def __add__(self, other):
        print("Scitam: ")
        return self.cislo + other.cislo
    def __mul__(self, other):
        print("bel bych nasobit, ale nechci: ")
        return f"{self.cislo} * {other.cislo} a nevim kolik to je"

c1 = Cislo(5)
c2 = Cislo(6)

try: 
    print(c1 + c2)  
except TypeError:
    print("Nelze scitat dve instance.")
print()

print(c1 * c2)
print()


class  MyList(list):     # dedim z listu - v MyList umim vsechno co je v Pyhtonu
    pass

a = MyList()
print(type(a))

a.append(5)   # na listu je nadefinovana metoda pro pridavani, tak ji muzu vyuzit na me instanci tridy MyList
a.append(6)
print(a)    # na listu je nadefinovana trida str, tak ji muzu vyuzit a muzu tisknout
a.append(8)
a[2] = "Jablko"
print(a[0])
print(a)
print()

class MyList1(list):
    def __getitem__(self, key):    
        # metoda kdyz se ptam na dany prvek seznamu - pokud ji prepisu, mi misto prvku vraci, to cim jsem ji prepsal
        print(f"Klic je {key}")
        return "ale stejne mas smulu."
    def __setitem__(self, key, value): 
        # metoda, ktera zapisuje prvky do seznamu, ale ja jsem si ji tady prepsal
        print(f"Klic je {key}")
        print(f"Hodnota je {value}")
        print("Nic nezapisu")
        print("*******")
        print("Tak ja to teda zapisu: ")
        super().__setitem__(key,value)   # jak jsem si tu metodu prepsal, tak tady si to vracim zpet a taham si z rodice tu funkci

b = MyList1([1, 2, 3, 4, 5, 6])
print(b)      # tady se vola str, ten je v pohode - vytiskne seznam
print(b[0])   # tady se vola getitem a ten nevrati prvek, protoze jsem si defaultni getitem prepsal
print()
b[5] = "hruska"
print(b)
print()
    



print("------------------------------------------------------------------------")
print()