# pocitani instanci v dane tride:

# self.__class__.__name__  ... vrati jmeno tridy

class Clovek:

    my_count = 0   
    # class variable, ktera mi bude pocitat pocet vytvorenych objektu

    def __init__(self, jmeno, prijmeni) -> None:
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        Clovek.my_count +=1  
        # a tady mam pocitadlo pro celou tridu
        # neni moc dobre, ze tam davam nazev tridy, takze to lze napsat lepe
        # self.__class__.pocet += 1 ... self.__class__ se podiva na nazev tridy
    
    def __repr__(self) -> str:
        return f"Jsem {self.jmeno} {self.prijmeni}."\
            f" Ve tride {self.__class__.__name__} byly vytvoreni {self.__class__.my_count} lide/i."
            # tady misto Clovek.my_count taky self.__class__.my_count

    def vstavej(self):
        print("Dobre rano")

    def jdi_do_prace(self):
        print("Vyrazim do prace, za chvili tam budu")
        self.pozdrav()

    def pozdrav(self):
        print("Dobry den")
        

# poradi priorit v objektovem programovani
# ICPO - 1. Instance, 2. Class, 3. Parent, 4. Objekt
# u normalnich funkci je LEGB ... local, enclosed, global, build

class Auto:
    pass

karel = Clovek("Karel", "Novak")
karel.vek = 29

skodovka = Auto()
skodovka.motor = 1.5
skodovka.barva = "modra"

karel.auto = skodovka    
# tady instanci skodovka priradim jako atribut instanci karel

karel.auto.motor = 2.4
print(skodovka.motor)

vw = Auto()
vw.znacka = "Passat"
vw.barva = "bila"

aneta = Clovek("Aneta", "Novakova")

aneta.auto = vw     
# tady instanci vw priradim jako atribut instanci aneta 
print(aneta.auto.znacka)
print(aneta.auto.barva)

print()
print(karel)
print(Clovek.my_count)
print()

petra = Clovek("Petra", "Novakova")
petra.pozdrav()
petra.jdi_do_prace()
print(petra)
print("*****")

### dedicnost ################################################################

class Programator(Clovek):   
    # programator dedi od cloveka a umi vsechny atributy a metody rodicovske tridy clovek
    # pokud mi vyhovuje init rodicovske, tak tady nemusim mit init
    
    def __init__(self, jmeno, prijmeni, jazyk):
        super().__init__(jmeno, prijmeni)  # tady beru nastaveni tridy 
        self.jazyk = jazyk

    def programuj(self):
        print("Programuji bez oblibeneho programovaciho jazyka.")

    def pozdrav(self):
        print("Ahoj")

pepa = Programator("Josef", "Skocdopole", "Python")
print(pepa)
pepa.pozdrav()
pepa.jdi_do_prace()   # tady volam pozdrav a vzdy zdravim ahoj, i kdyz tuto metodu volam z rodicovske tridy. Ale je tam potoda pozdrav u programatora a ta ma vetsi prioritu
pepa.programuj()

print()


"""

is-a ... dedicnost pes je zvire, programator je clovek,...

has-a ... kompozice/skladani = mam instanci a ta ma atributy

"""


