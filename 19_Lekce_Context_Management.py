### Context Management

with open("12_Lekce_zzz/soubor1.txt") as file:
    file.readline()

# kdyz otevru file, tak ho musim vzdycky zavrit
# with na to mysli a soubor vzdy zavre

# a nebo lze definovat vlastni context management pro zavreni souboru

class ContextManagement():
    def __enter__(self):   # otevira soubor a vraci ho
        print("spoustim context manager")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_traceback):
        # tato metoda se postara o zpracovani vyjimky a uzavreni vyjimky
        print("ukoncuji context management")

with ContextManagement():
    print("hehe, funguje to")
print()


