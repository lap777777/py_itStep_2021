# https://github.com/trohat/python1-kurz/blob/main/OOP1/OOP-1.txt

# Úkol - flexibilní slovník

# Vytvořte třídu FlexibilniSlovnik, která nerozlišuje mezi inty a stringy v rolích klíčů.

# Pokud ve slovníku vytvořím položku s klíčem 1 (číslo), je to něco jiného, než když vytvořím položku s klíčem '1' (string).
# Pro vaši novou třídu to ale bude stejný klíč. Takže když se pokusím přečíst hodnotu s klíčem 1, slovník zkusí najít všechny možnosti (jedna jako int, i jedna jako string), než se vzdá a ohlásí, že klíč neexistuje.

# Příklad:
# fs = FlexibilniSlovnik()
# fs[1] = "jablko"
# print(fs['1']) -> vytiskne "jablko"  (normálně by byla KeyError)
# fs['2'] = hruška
# print(fs[2]) -> vytiskne "hruška" (normálně by opět byla KeyError)

# Všechno ostatní funguje jako v běžném slovníku.


# resit pres podtrzitokove metody __getitem__
# apak pouzit super
# doplnit si teorii k __setitem__

class MyList(list);
    def __getitem__(self, key):
        print(f"Klic je {key}")
        return "ale stejne mas smulu."
