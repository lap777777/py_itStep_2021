print("1-------------------------------------------------------------")
# Task 1
# Create an app that stores information about great basketball players. Store the player’s full name and height. Provide the possibility to add, delete, search, and replace data. Use a dictionary to store information.
players = {}

# add data
while True:
    player = input("Zadej jmeno hrace: ")
    if not player:
        break
    height = int(input("Zadej vysku: "))
    players[player] = height

print(players)

# delete data
player = input("Zadej jmeno hrace na vymaz: ")
if player in players:
    players.pop(player)
else:
    print("Zadany hrac neni ve slovniku")
print(players)

# search data:
player = input("Zadej jmeno hledaneho hrace: ")
if player in players:
    print("Zadany hrac je ve slovniku.")
    print(f"Jeho vyska je {players[player]}")
else:
    print("Zadany hrac neni ve slovniku.")

# replace data
print("Vymena klice: ")
player = input("Zadej jakeho hrace chces vymenit: ")
player1 = input("Zadej nove jmeno hrace: ")
players[player1] = players.pop(player)
print(players)

print("Vymena hodnoty:")
player = input("Zadej hrace u ktereho chces vymenit hodnotu: ")
height = int(input("Zaden novou vysku: "))
players[player] = height
print(players)
print()

print("2-------------------------------------------------------------")

# Task 2
# Create an app English-French Dictionary. Store a word in English and its French translation. Provide the possibility to add, delete, search, and replace data. Use a dictionary to store information.

my_dict = {}

# add data
while True:
    key = input("Zadej slovo v EN: ")
    if not key:
        break
    value = input("Zadej preklad v CZ: ")
    my_dict[key] = value
print(my_dict)

# delete
key = input("Zadej slovo v EN, pro ktere chces vymazat zaznam: ")
my_dict.pop(key)
print(my_dict)

# search
key = input("Zadej hledane slovo v EN: ")
if key in my_dict:
    print(f"Zadane slovo je ve slovniku a preklad je {my_dict[key]}.")
else:
    print("Zadane slovo neni ve slovniku.")

# vymena celeho zaznamu
key = input("Zadej klic, ktery chces nahradit: ")
key1 = input("Zadej nove slovo v EN: ")
value1 = input("Zadej preklad v CZ: ")
my_dict[key1] = my_dict.pop(key)
my_dict[key1] = value1
print(my_dict)
print()

print("3-------------------------------------------------------------")
# Task 3
# Create an app Company. Store the following information about a person: full name, phone number, corporate email, job title, room number, skype. Provide the possibility to add, delete, search, and replace data. Use a dictionary to store information.

company = {
    "os1": {
        "name": "Petr Pavel",
         "phone": 456754354,
          "email": "petr@jo.cz",
          'job': "konstrukter", 
          "room": 456, 
          "skype": 357859}, 
    "os2": {
        "name": "Josef Skoc", 
        "phone": 357856412, 
        "email": "josef@jo.cz", 
        'job': "uklizec", 
        "room": 352, 
        "skype": 364789}, 
    "os3": {
        "name": "Tom Kyval", 
        "phone": 356754456, 
        "email": "tom@jo.cz", 
        'job': "obchodik", 
        "room": 395, 
        "skype": 346754}, 
}

id = 3

# pridani zamenstance:
def add_employee(full_name, phone, email, job, room, skype):
    employee = {
        "name": full_name, 
        "phone": phone, 
        "email": email, 
        'job': job, 
        "room": room, 
        "skype": skype}
    global id      # nastavit globalni, vychazim z promenne nastavene mimo funkci
    id += 1         # pridavam cislo id pro dalsi zaznam do slovniku
    company[f"os{id}"] = employee       # pridavam klic do slovniku a jeho hodnotu
    return employee   # funkce vraci zadane hodnoty

new_employee = add_employee("Dan Moravek", 3456789451, "dan@jo.cz", "obchodnik", 355, 3567456)
# ukladam noveho zamestnance do promenne a uz ho mam ulozeneho i do slovniku diky radku 123


# vymazanani zamestnance:
def del_employee(employee_id: str):    # za dvojtecku davam typ promenne - parametru, co vracim
    """
    Deletes en employee
    employee_id - id of the employee
    """
    deleted_employee = company[employee_id]
    del company[employee_id]
    return deleted_employee

deleted_employee = del_employee("os3")

# hledani podklice
def find_phone(phone):
    for employee in company.values():
        if phone == employee["phone"]:
            return employee["name"]  
            # return employee - vrati cely podslovnik, 
    return "Employee with this phone not found"

print(find_phone(3456789451))
print(find_phone("zadne cislo"))

# nahrazeni dat
def replace_employee_data(employee_id, data, new_value):
    if employee_id not in company:
        return False
    if data not in company[employee_id]:   # in se pta na klice, takze hledam klic v podslovniku company[employee_id]
        return False
    company[employee_id][data] = new_value
    return company[employee_id]

replace_employee_data("os3", "room", 111)
replace_employee_data("os1", "job", "vedouci konstrukce")

print(company)

print("4-------------------------------------------------------------")
# Task 4
# Create an app Book Collection. Store the following information about books: author, title, genre, year of release, publisher. Provide the possibility to add, delete, search, and replace data. Use a dictionary to store information.

books = {
    "id1": {
        "author": "Josef Capek",
        "title": "RUR",
        "year": 1920,
        "pages": 359},
    "id2": {
        "author": "Ernest Hemingway",
        "title": "Starec a more",
        "year": 1935,
        "pages": 150},
    "id3": {
        "author": "Ota Pavel",
        "title": "Zlati uhori",
        "year": 1950,
        "pages": 256}
}

id = 3

# pridani
def add_book(author, title, year, pages):
    book = {
        "author": author,
        "title": title,
        "year": year,
        "pages": pages
    }
    global id
    id += 1
    books[f"id{id}"] = book
    return book

print(add_book("Jaromir Erben", "Kytice", 1960, 120))
print(add_book("Petr Bezruc", "Ostrava", 1970, 5))
print()

# mazani
def del_book(book_id: str):
    deleted_book = books[book_id]
    del books[book_id]
    return deleted_book

print(del_book("id2"))
print()

# hledani
def search_book(book_id: str):
    for key in books.keys():
        if book_id == key:
            return books[book_id]
        return f"Zadana kniha neni v databazi"

def search_author(author: str):
    for book in books.values():
        if author == book["author"]:
            return f'{book["author"]}, kniha: {book["title"]}.'
        else:
            return "Dany autor nenalezen."

print(search_book("id1"))
print(search_author("Josef Capek"))
print(search_book("id3"))
print(search_author("Ota Pavel"))
print()
print(books["id3"])
print(books["id3"]["author"])
print()

# nahrazeni
def replace_book(book_id, my_key, new_value):
    if book_id not in books:
        return False
    if my_key not in books[book_id]:
        return False
    books[book_id][my_key] = new_value
    return books[book_id]
    
print(replace_book("id1", "title", "Bila nemoc"))
print()

print(books)
print("-------------------------------------------------------------")

