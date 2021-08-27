############# Algoritmy #####################################
# jak jsou programy efektivni a jak to muzeme merit
#   - casova slozitost
#   - pametova slozitost (s kolika daty pracuji apod.)

import random

### Casova slozitost
def one_task():
    """
    tohle je funkce s casovou slozitosti 1
    """
    3 + 4

def five_tasks():
    """
    tohle je funkce s casovou slozitosti 5
    """
    3 + 4
    5 + 7
    5 - 2
    2 * 8
    8 / 2

# predpoklad, ze scitani, nasobeni, odecitani a deleni je priblizne stejne casove narocne, prvni funkce ma casovou narocnost 1 a druha funkce ma casovou narocnost 5
# funkce se vola a pak pocita, tak jsou to priblizne dva ukoly, ale bereme jeden jako jedno scitani

seznam = [1, 3, 4]
for _ in range(random.randint(1,1000)):
# znak _ davam, kdyz tu promennou dal nepouzivam - jasne pro dalsi programatory
    seznam.append(8)
# nevim, jak dlouhy mam seznam - randint vybere nahodne cislo mezi 1 az 1000 a tolikrat se provede cyklus for a tolikrat pridam cislo 8 do seznamu

print(f"Delka seznamu je {len(seznam)}.")
# delka seznamu se meni, je min 4 a max 1003 - jeho delka je N

one_task()   # casova narocnost 1
five_tasks() # casova narocnost 5

for i in seznam:
    one_task()
# casova slozitost je N * 1 = N -> N

for i in seznam:
    five_tasks()
# casova slozitost je N * 5 -> N

for i in seznam:
    five_tasks()
one_task()
# casova slozitost je N * 5 + 1 -> N

for i in seznam:
    one_task()
five_tasks()
# casova slozitost je N * 1 + 5 -> N

for i in seznam:
    one_task()
for n in range(10):
    five_tasks()
# casova slozitost je N * 1 + 10 * 5 = N + 50  -> N

# kdyz resim cas, tak konstanty me nezajimaji (50, 5, 1) - jejich scitani, nasobeni zanedbavam, takze jedno jestli mam 1*10 nebo 1*100, 
# zajima me pouze N a to merim

for i in seznam:
    for j in seznam:
        one_task()
# casova slozitost je N * N = N ** 2 -> N**2
# o tohle uz je zajimave pro mereni casove slozitosti, mam N a tady je N*N

for i in seznam:
    for j in seznam:
        one_task()
for number in seznam:
    five_tasks()
one_task
# casova slozitost je N * N + 5 * N + 1 -> N**2

# zapis - notace velkeho 0 neboli Big 0h notation
# 0(1)       ... konstatni casova slozistost
# 0(log n)   ... logaritmicka casova slozistost
# 0(n)       ... linearni
# 0(n ** 2)  ... kvadraticka (dva vnorene cykly)
# 0(n ** 3)  ... mocninna (3 vnorene cykly)
# 0(n ** 4)  ... mocninna (4 vnorene cykly)
# 0(2 ** n)  ... exponencialni

# 0( n ** 2) == 0( 3 * n ** 2 + 5) ... vlevo je n**2 a vpravo je nejslozitejsi take n**2

# 2 druhy prikladu
#   - vyhledavani prvku
#   - trideni prvku


# BINARTNI DELENI:
def binary_search(list1, item_to_search):
    '''
    This is "docstring" - dokumentacni popisek.
    Searches for item in list.
    Returns True if present, False if absent.
    '''
    low = 0
    high = len(list1) - 1 
    # divam se pouze na prvky v seznamu a tak vyhodi prvky mimo seznam)
    while True:
        mid_index = (high + low) // 2
        mid_item = list1[mid_index]
        if item_to_search > mid_item:
            low = mid_index + 1
        elif item_to_search < mid_item:
            high - mid_index - 1
        elif item_to_search == mid_item:
            return True
    return False

# assert - pro testy - predpokladam, ze neco je pravda, pokud ne, tak vyhodi chybovou hlasku, kterou si zadam
assert binary_search([1,2,3,4,5],1) == True, "1 working incorrectly"
assert binary_search([1,2,3,4,5],2) == True, "2 working incorrectly"
assert binary_search([1,2,3,4,5],3) == True, "3 working incorrectly"
assert binary_search([1,2,3,4,5],4) == True, "4 working incorrectly"
assert binary_search([1,2,3,4,5],5) == True, "5 working incorrectly"
assert binary_search([1,2,3,4,5],2.5) == False, "2.5 working incorrectly"
assert binary_search([1,2,3,4,5],0) == False, "0 working incorrectly"
assert binary_search([1,2,3,4,5],8) == False, "8 working incorrectly"

"""
assert True, "True will never raise an error"
assert False, "False will raise - vyhodi chybu"
raise IndexError    # tohle vyhodi index error
"""
print(binary_search.__doc__)   # vola docstring
