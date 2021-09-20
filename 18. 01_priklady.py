# https://github.com/trohat/python1-kurz/blob/main/OOP1/OOP-1.txt

# Úkol - flexibilní slovník

# Vytvořte třídu FlexibilniSlovnik, která nerozlišuje mezi inty a stringy v rolích klíčů.

# Pokud ve slovníku vytvořím položku s klíčem 1 (číslo), je to něco jiného, než když vytvořím položku s klíčem '1' (string).
# Pro vaši novou třídu to ale bude stejný klíč. Takže když se pokusím přečíst hodnotu s klíčem 1, slovník zkusí najít všechny možnosti (jedna jako int, i jedna jako string), než se vzdá a ohlásí, že klíč neexistuje.

# resit pres podtrzitokove metody __getitem__
# apak pouzit super

class FlexibilniSlovnik(dict):
    pass
    # def __getitem__(self, key):
    #     if isinstance(key, int):
    #         super().__getitem__(key)
    #     elif key.isalpha():
    #         key = int(key)
    #         if key.isdigit():
    #             super().__getitem__(key)
    #         else:
    #             print("Klic nelze prevest na cislo.")
    #     else:
    #         print("Chybny klic, neni ve slovniku")
    

a = FlexibilniSlovnik({1: "a", 2: "b", 3: "c", 4: "e", 5: "f"})
print(a)
print(f"Co je na klici 5 zadane jako cislo: {a[5]}")
print(a[5])
print()






