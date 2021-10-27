# https://github.com/trohat/python1-kurz/blob/main/OOP1/OOP-1.txt

# Úkol - flexibilní slovník

# Vytvořte třídu FlexibilniSlovnik, která nerozlišuje mezi inty a stringy v rolích klíčů.

# Pokud ve slovníku vytvořím položku s klíčem 1 (číslo), je to něco jiného, než když vytvořím položku s klíčem '1' (string).
# Pro vaši novou třídu to ale bude stejný klíč. Takže když se pokusím přečíst hodnotu s klíčem 1, slovník zkusí najít všechny možnosti (jedna jako int, i jedna jako string), než se vzdá a ohlásí, že klíč neexistuje.

# resit pres podtrzitokove metody __getitem__
# apak pouzit super


class FlexibilniSlovnik(dict):
    def __init__(self):
        self.dict = {}

    def add_dict(self, key, value):
        self.dict[key] = value

    def __str__(self):
        text = "Slovnik obsahuje: \n"
        for key, value in self.dict.items():
            text += f"\tklic: {key}, value: {value},\n"
        text = text.rstrip(",\n") + ".\n"
        return text

    def __getitem__(self, key):
        if isinstance(key, int):
            super().__getitem__(key)
        elif key.isalpha():
            key = int(key)
            if isinstance(key, int):
                super().__getitem__(key)
            else:
                print("Klic nelze prevest na cislo.")
        else:
            print("Chybny klic, neni ve slovniku")
    
a = FlexibilniSlovnik()
a.add_dict(1, "jablko")
a.add_dict(2, "hruska")
a.add_dict(3, "svestka")
print(a.__dict__)
print(a)
print()
# print(a[1])
# print(a[2])
# print(a["1"])
# print(a["2"])

class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif int(key) in self:
                key = int(key)
            elif str(key) in self:
                key = str(key)
        except ValueError:
            pass
        return super().__getitem__(key)
    
b = FlexibleDict({1: "jablko", 2: "hruska", 3: "merunka"})
b[4] = "svestka"

print(b[1])
print(b["1"])
print()
print(b)
print()

### jak dostat slovnik do tridy???



