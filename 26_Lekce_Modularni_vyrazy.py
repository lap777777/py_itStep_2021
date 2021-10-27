### Regularni vyrazy

import re   # knihovna pro regularni vyrazy

str1 = "bye and hello world and Hello universe"
result1 = (re.search("hello", str1)) # hledam na modulu re (co hledam, kde hledam)
print(result1)
print(result1.span())  # vraci poradi znaku, kde nasel hledany retezec
print(result1.group())  # prvni skupina, ktera se nasla, skupina na indexu 0, vraci prvni hello
print()

regexp = re.compile("(h|H)ello")  # vytvarim regularni objekt a na mem pak hledam - hledam male i velke H, | ... nebo
# to co je v kulatych zavorkach uz je skupina, takze uz mi ukaze skupiny, muzu to pak treba nahrazovat - treba nahrad druhou skupinu
print(regexp.search(str1))   # search vraci prvni vyskyt
print(regexp.findall(str1))  # findall vraci vsechny vyskyty v seznamu
print()

regexp = re.compile("[hH]ello") # vycet - hledam ve, co ma na prnvim miste h nebo H
regexp = re.compile("[a-z]ello") # vycet / hledam vse, co ma na prnvim znaku pismena a az z a pak ello
regexp = re.compile("[a-zA-Z0-9 ]ello") # jeste delsi vycet
str2 = "hallo hello 9ello ello"
print(regexp.findall(str2))
print()

# kdyz dam pomlcku jako prvni v rozsahu, tak je to pomlcka [-ABCD], pokud je uvnitr, tak je to rozpeti [A-D]
"""
regex.com
\bHello ... \b znamena boundary - hranice slova, takze najde Helloworld (na zacatku slova), wordHello (na konci slova)
\bhello\b .. hleda pouze presne slovo hello
\B ... vsechno krome, co znamenal puvodni znak ... takze uvnitr slova WoHellorld
\d ... digits ... cisla ... hledam 5mistne cislo \d{5}, \d{5,8} 5 az 8 cisel, \d
\D ... vsechno krome cislice
\s ... whitespace ... mezery, tabulatory, konce radku
\S ... nowhitespace
\w ... word ... jakykoliv pismenko, alfanumericky znak, podtrzitko
\W ... noword (zavorky, tecka, carka, whitespace)
[^] ... negace, co dam za stisku, tak se vynecha
{5} 5x opakovani
{5,8} 5 az 8 znaku
{,5} 0 az 5 opakovani
{5,} 5 az nekonecno
[a-zA-Z]+  plus znamena jedno az nekonecno opakovani = libovolne dlouhe slovo
[a-zA-Z]* hvezdicka - nula az nekonecno opakovani
[a-zA-Z]? otaznik - bud tam je (jednou) nebo tam neni
kvantifikatory jsou hladove, hledaji co nejdelsi vyraz 
pokud za +, * nebo ? dam ?, tak nezere, najde pouze prvni vyskyt a konci
? bere nic nebo jeden, ?? bere nic, znak se preskoci

pokud potrebuji najit lomitko, tak bud musim dat 4 lomitka nebo 2 lomitka a r (row string)
regexp = re.compile(r"\\ten")

^ ... zacatek
$ ... konec
^hello ... na zacatku retezce musi byt hello
hello$ ... na konci reteze musi byt hello
"""

# 1. Napiste regex, ktery najde slova PLOT a PLOD
# varianta 1. (les, led, lev)
regexp = re.compile(r"PLO(T|D)")
regexp = re.compile(r"le(s|d|v)")

# 2. napiste regex, ktery najde slova HAD a HRAD
regexp = re.compile(r"HR?AD")

# 3. napiste regex, ktery najde slova ZAHRADA, OHRADA, PODHRADÍ nebo VÝHRADNĚ
regexp = re.compile(r"(zahrada|ohrada|podhradí|výhradně")

# 4. napiste regex, ktery najde slovko koncici na nost
regexp = re.compile(r"nost\b")

# 5. napiste regex, ktery najde mezeru nasledujici po carce, dvojtecce, tecce nebo stredniku
regexp = re.compile(r"(,|\.|:|;) ")

# 6. napiste regex, ktery najde slovo o delce minimalne 7 znaku
regexp = re.compile(r"[a-zA-z]{7,}")

# 7. napiste regex, ktery najde slovo neobsahuji pismeno o (nebo 0)
regexp = re.compile(r"[a-np-zA-NP-Z]+") 

# 8. Napiste regex, ktery najde telefonni cislo ve formatu 3 cislice, mezera, tri cislice mezer a nakonec znovu tri cislice
regexp = re.compile(r"\d{3} \d{3} \d{3}")

# 9. vylepsete regex ze cviceni 8 o ceskou mezinarodni predvolbu s mezerou
regexp = re.compile(r"\+420 \d{3} \d{3} \d{3}")

# 10. napiste regex, ktery overi email. Zacina na pismeno, pak muzou byt pismena, tecky, cisla, pak je zavinac a pak obet cisla a pismena a jedna tecka a nakonec 2 nebo 3 pismene znaky
regexp = re.compile(r"[a-zA-Z][a-zA-Z\.\d]+@[a-zA-Z\d]|\d+\.[a-zA-Z]{2,3}")

# testovani v prostredi www.debuggex.com




