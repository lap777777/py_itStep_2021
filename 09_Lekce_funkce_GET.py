# priorita u funkci
# LEGB = local (mistni, napr. ve funkci), enclosing (vnorene), global (standardne nastavim v kodu), bult-in (napr. sum)

# definovani promenne a = 5, 

def zmateni():
    global a    # tohle acko se pak pouzije vsude v codu
    a = 10
    print("ve funkci")
    print(a)

a = 5               
print("venku")
print(a)

zmateni()

print("opet venku")
print(a)     # jelikoz jsem nastavil global ve funkci, tak tady budu mit 10 a pak vsude v kodu nize, kde se vola promenna a
# pokud by ve funkci nebyl global a, tak tady by byla 5, protoze volal local promenou
print("----------------------------")

#############################################

slovnik = {"kocka": 1, "pes": 1}

# metoda .get()

slovnik.get("slon", "nic tu neni") 
# ptam se na klic, pokud
# klic neexistuje, tak vrati hlasku "nic tu neni" a slovnik zustane v puvodni podobe
# n_days[city] = n_days.get(city, 0) + 1
# do promenne n_days se secte puvodni hodnota + 1
# pokud ve slovniku nic neni, tak se pricte pouze jedna pod klic city
print(slovnik)
print("-----------------------------------------------")

# metoda .setdefault()

slovnik.setdefault("opice", "nic tu neni")
# ptam se, jestli je ve slovniku opice, pokud neni, tak do slovniku zapise klic opice a prida k nemu hodnotu "nic tu neni"
print(slovnik)
print()
