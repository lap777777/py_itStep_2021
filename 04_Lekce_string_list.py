# string - retezce
# list - seznam

# zpusoby tisku - f-string PEP 498
jmeno = "Lada"
vek = "43"
print("jmenuji se %s a je mi %d" % (jmeno, vek))
print("jmenuji se {0} a je mi {1}" .format(jmeno, vek)) # .format pouzit maximalne u n-tic, tuple apod.
print(f"Jmenuji se {jmeno} a je mi {vek}")
print(f"dvakrat sest je {2*2}.")

# string = retezec
# string are immutable - retezce jsou nemenne
# mohu je scitat
retezec = "abcd"
retezec = retezec + retezec
print()

# mohu je nasobit
retezec = "abcd"
retezec = 5 * retezec
print(retezec)

# list - seznamy hodnot
# oproti stringum se hodnoty daji menit, muzu pridavat, ubirat, menit
znamka1 = 1
znamka2 = 2
znamka3 = 1
znamka4 = 1
znamka5 = 5
znamka6 = 3
# mam vice hodnot a chci je ulozit do jedne promenne - pouziji list
znamky = [1, 2, 1, 1, 5, 3, 4, 2, 1]
# do seznamu muzu davat ruzne datove typy - je to sice k nicemu, ale jde to
seznam1 = [True, 1, 1.00, "ahoj", None]
# do listu lze vkladat dalsi listy
znaky = [["po", 1], ["ut", 1]]
# listy maji index = 0,.....
print(znamky[0])  # vytiskne 1. prvek seznamu
print(znamky[-1]) # vytiskne posledni prvek seznamu,  -2 je druhe od zadu
# : muzu dat rozsah - rozsah je n-1, tak pokud chci index 1. az 3., tak musim dat 1:4
print(znamky[1:4])
print(znamky[0]+znamky[2:4])
print(znamky[:5]) # od 0. indexu az do konce
print(znamky[2:]) # od 2. indexu do posledniho
print(znamky[:])  # vytiskne vse
print(znamky[2:8:2]) # stejne jako range(zacatek, konec, kroky)
print()
# v listu lze menit prvky
znamky[0] = 5
print(znamky[0])  # vytiskne 5, ktera prepsala 1, ktera byla puvodne prvni
znamky1 = znamky
znamky[0] = "Ano"
print(znamky)
print(znamky1)
print()
# zmeni se jak puvodni slovnik, tak i novy slovnik - POZOR!!!!!!!!!
# pokud nechci aby se mi seznamy rovnaly, tak musim vytvorit novy seznam
znamky2 = znamky[:]
znamky[1] = "NE"
print(znamky)
print(znamky2)
print()
# muzu delat u cisel v listu i matematicke operace
print(znamky[0])
znamky[0] += 1
print(znamky[0])
print()

# string - index funguje stejne jako u listu
retezec = "Australie"
print(retezec[0])
print(retezec[::-1])  # vytiskne pozpatku string
print()
# ale retezec nejde zmenit, takze nasledujici funkce vyhodi chybu
# retezec[0] = "A"

# prochazeni listu nebo stringu - pomoci cyklu
# funkce len() ... vraci mi delku
for i in range(len(znamky)):
    print(znamky[i])
my_string = "Australie"
for i in my_string:  # ale nemusim tam davat delku
    print(i)
for znamka in znamky:
    print(znamka)


# funkce list() ... vytvori seznam z toho, z ceho lze vytvorit list ... napr. ze stringu
my_string = "pejsek"
my_list = list(my_string)
print(my_list)
# metoda .join() .. obracene - vytvori z listu string
my_string = str(my_list.join())
print()

