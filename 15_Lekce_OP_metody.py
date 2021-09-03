
class Human():
    def __init__(self, name, surname, site, job):
        self.name = name
        self.surname = surname
        self.site = site
        self.job = job
    
    def get_up(self):
        # metoda uvnitr tridy, tak kazda metoda musi mit prvni parametr self
        print("Dobre rano, cas vstavat.")
    
    def go_to_town(self, city):   
        # zadavam atribut zvenku
        print(f"Jdu do {city}")

    def go_to_work(self):         
        # tady mam atribut definovany v __init__, patri dane instanci
        print(f"Jdu do {self.site}")

karel = Human("Karel", "Novak", "IBM", "programator")

karel.get_up()
karel.go_to_town("Prahy")
karel.go_to_work()

