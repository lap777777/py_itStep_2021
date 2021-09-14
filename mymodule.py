"""
Muj vlastni modul s konstantou 20 a funkci pro kriceni a scitani
"""

print("Modul se prave nacita")

konstanta = 20

def scream():
    return "Hurrraaaa"

def scitani(a, b):
    return a + b


# pokud modul spustim jako hlavni program, tak se provede to co je pod if - ze se spusti jako hlavni program, tzn. ze ho napisu do prikazoveho radku: python mymodule.py
# pouziva se napr. pro testovani modulu, ktere pak vyuzivam v nejake svoji aplikaci

if __name__ == "__main__":
    print("modul bezi jako hlavni program")
    print(scream())
    print(scitani(100, 200))