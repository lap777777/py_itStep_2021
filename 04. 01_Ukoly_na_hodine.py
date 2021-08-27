# vytvorit seznam, vytisknout cisla
my_list = [1, 3, 4, 6, 10, 15, 19, 30, 50]
for i in my_list:
    print(i)

# vytvorit seznam cisel, najit maximum
my_max = 0
for i in my_list:
    if i > my_max:
        my_max = i
print(f"Maximum ze seznamu cisel {my_list} je cislo {my_max}.")

# vytvorit seznam, najit minimum
my_min = max(my_list)
for i in my_list:
    if i < my_min:
        my_min = i
print(f"Minimum ze seznamu cisel {my_list} je cislo {my_min}.")

# vytvorit seznam, soucet cisel
my_sum = 0
for i in my_list:
    my_sum += i
print(f"Soucet cisel ze seznamu cisel {my_list} je {my_sum}.")

# vytvorit seznam, vytisknout 1. a posledni prvek
print(f"Prvni prvek: {my_list[0]}")
print(f"Posledni prvek: {my_list[-1]}")

# vytvorit seznam, vypis prostredni prvek, pokud existuje, kdyz neexistuje, vypis oznameni
my_len = len(my_list)
if my_len % 2 == 0:
    print(f"Seznam cisel {my_list} nema prostredni prvek")
else:
    index = int(len(my_list)// 2)
    print(f"Prostredni prvek seznamu cisel {my_list} je {my_list[index]}")
print()



