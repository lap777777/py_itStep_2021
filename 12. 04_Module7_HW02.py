# Task 1
# Develop an information system Employees. 
# The app should provide data input, editing the employee’s data, 
# deleting an employee, searching for an employee by last name, 
# outputting information about all employees of the specified age or 
# whose last name begins with the specified letter. 
# Provide the possibility to save the found information to a file. 
# The full list of employees is also saved to a file (automatically 
# when exiting the app, by the user’s command at runtime). 
# The employee list is loaded from the file specified by the user when the app starts.

# application:
#   - input data
#   - editing data
#   - deleting employee
#   - searching by last name
#   - searching by age
#   - search by first letter of last name

# input - employee list loaded when application starts
# output - save found information to file (last name, age, first letter)
# output - full list save to file - automatically when exiting the app, users command at runtime

def my_upload(file):
    """
    upload of data from external file to dictionary
    """
    company = {}
    my_count = 1
    with open(file, encoding="utf-8") as f1:
        for line in f1:
            first, surname, age = line.replace(",","").rstrip("\n").split(" ")
            employee = {
                "first_name": first.strip(),
                "surname": surname.strip(),
                "age": int(age.strip())
            }
            company[f"id{my_count}"] = employee
            my_count += 1
    return company

def employee_application():
    print()
    print("########################################################")
    print("         Welcome to information system Employee")
    print("########################################################")
    print()
    
    # otevreni souboru s daty:
    company = my_upload("12. employee.txt")
    
    # volba uzivatele - zadani vyberu
    choice = 0
    while choice != 8:
        choice = user_choice()
        print("********************************************************")
        print()

        # vytisteni databaze
        if choice == 1:
            print("*** Tisk zaznamu z databaze ****************************")
            for key, employee in company.items():
                print(f'{key}, jmeno: {employee["first_name"]}, prijmeni:   {employee["surname"]}, vek: {employee["age"]} let.')
            print("********************************************************")
            print()

        # pridani noveho zamestnance
        if choice == 2:
            print("*** Pridani noveho zamestnance *************************")
            first_name = ""
            surname = ""
            age = 0
            while first_name == "":
                first_name = input("Zadejte krestni jmeno zamestnance: ")
            while surname == "":
                surname = input("Zadejte prijmeni zamestnance: ")
            while age == 0:
                try:
                    age = int(input("Zadej vek zamestnance: "))
                except ValueError:
                    print("Chybne zadani - zadejte cislo!")
                    continue
            print(add_employee(first_name, surname, age))
            print("********************************************************")
            print()

        # nahrazeni dat
        if choice == 3:
            print("*** Nahrazeni dat **************************************")
            my_id = ""
            while my_id not in company:
                my_id = input("Zadejte id zamestnance (format idx):   ")
            data = user_choice1()
            if data == "age":
                new_value = 0
                while new_value == 0:
                    try:
                        new_value = int(input("Zadej vek zamestnance: "))
                    except ValueError:
                        print("Chybne zadani - zadejte cislo!")
                        continue
            else:
                new_value = ""
                while new_value == "":
                    new_value = input("Zadejte novou hodnotu: ")
            print(replace_data(my_id, data, new_value))
            print("********************************************************")
            print()

        # vymazanani zamestnance:
        if choice == 4:
            print("*** Vymazani zadaneho zamestnance **********************")
            my_id = ""
            while my_id not in company:
                my_id = input("Zadejte id zamestnance na vymaz (format idx):   ")
            print(del_employee(my_id))
            print("********************************************************")
            print()

        # hledani zamestnance dle prijmeni:
        if choice == 5:
            print("*** Vyhledani zamestnance dle prijmeni *****************")
            user_surname = ""
            while user_surname == "":
                user_surname = input("Zadejte prijmeni hledaneho zamestnance:   ")
            print(find_surname(user_surname))
            print("********************************************************")
            print()

        # hledani zamestnance dle veku:
        if choice == 6:
            print("*** Vyhledani zamestnance dle veku *********************")
            user_age = 0
            while user_age == 0:
                try:
                    user_age = int(input("Zadejte vek hledaneho zamestnance:    "))
                except:
                    print("Chybne zadani - zadejte vek jako cislo")
                    continue
            print(find_age(user_age))
            print("********************************************************")
            print()

        # hledani zamestnance dle prvniho pismena prijmeni:
        if choice == 7:
            print("*** Vyhledani dle prvniho znaku prijmeni ***************")
            while True:
                user_letter = input("Zadej prvni pismeno prijmeni hledaneho zamestnance: ")
                user_letter = user_letter.upper()
                if len(user_letter) == 1:
                    break
                else:
                    continue
            print(find_letter(user_letter))
            print("********************************************************")
            print()

        if choice == 8:
            print("********************************************************")
            print("***** Thanks for using information system Employee *****")
            print("********************************************************")
            with open("12. employee.txt", "w", encoding="utf") as f1:
                for employee in company.values():
                    f1.write(f'{employee["first_name"]}, {employee["surname"]}, {employee["age"]}\n')
            print("")
            print("#########################END############################")
            print()

#### Podpurne funkce  ################################################



def user_choice():
    """
    inputed choice by user - used in application employee for selection of tasks
    """
    print("*** MENU ***********************************************")
    print("Zadejte svoji volbu: ")
    print("  1 - vytistknuti databaze")
    print("  2 - pridani noveho zamestnance")
    print("  3 - zmena zaznamu dle id zamestnance")
    print("  4 - vymazani zadaneho zamestnance")
    print("  5 - vyhledani dle prijmeni")
    print("  6 - vyhledani dle veku")
    print("  7 - vyhledani dle prvniho pismena prijmeni")
    print("  8 - Opusteni aplikace")
    while True:
        try:
            choice = int(input("  vas vyber (volba 1-8) ->  "))
        except ValueError:
            print("  Chybne zadani (vyberte cislo 1-8).")
            continue
        else:
            if choice in [1,2,3,4,5,6,7,8]:
                return choice
            else:
                print("  Chybne zadani, (vyberte cislo 1-8).")

def user_choice1():
    """
    inputed choice by user - used in aaplication choice 3 - change of data
    """
    print("Zadejte svoji volbu: ")
    print("  1 - zmena krestniho jmena")
    print("  2 - zmena prijmeni")
    print("  3 - zmena veku")
    while True:
        try:
            choice1 = int(input("  vas vyber (volba 1-3) ->  "))
        except ValueError:
            print("  Chybne zadani (vyberte cislo 1-3).")
            continue
        else:
            if choice1 in [1,2,3]:
                selection = ()
                if choice1 == 1:
                    selection = "first_name"
                elif choice1 == 2:
                    selection = "surname"
                else:
                    selection = "age"
                return selection
            else:
                print("  Chybne zadani, (vyberte cislo 1-3).")

def count_id(dictionary):
    """
    returns number of employees in dictionary
    """
    number = 0
    for key in dictionary.keys():
        number += 1
    return number

def add_employee(first_name, surname, age):
    """
    adds new employee into dictionary based on input from user
    inputed values(first_name, surname, age)
    """
    employee = {
        "first_name": first_name,
        "surname": surname,
        "age": age
        }
    id = count_id(company)
    id += 1
    company[f"id{id}"] = employee
    return f"Pridan novy zamestnanec: \n{employee}"

def replace_data(employee_id, data, new_value):
    """
    replaces data for inputed key and employee[key]
    """
    company[employee_id][data] = new_value
    return company[employee_id]

def del_employee(employee_id: str): 
    """
    Deletes en employee based on inputed employee_id
    """
    deleted_employee = company[employee_id]
    del company[employee_id]
    with open("12. deleted.txt", "w", encoding="utf-8") as f1:
        f1.write(f'{deleted_employee["first_name"]}, {deleted_employee["surname"]}, {deleted_employee["age"]}')
    return f"Vymazan zamestnanec: \n{deleted_employee}"

def find_surname(user_surname):
    """
    finds employee based on surname inputed by user
    """
    with open("12. surname.txt", "w", encoding="utf-8") as f1:
        print("Nalezeny zaznam: ")
        my_count = 0
        for employee in company.values():
            if user_surname == employee["surname"]:
                f1.write(f'{employee["first_name"]}, {employee["surname"]}, {employee["age"]}\n')
                print(employee)
                my_count += 1
        return f"Pocet nalezenych zaznamu: {my_count}"

def find_age(user_age):
    """
    finds employee based on age inputed by user
    """
    with open("12. age.txt", "w", encoding="utf-8") as f1:
        print("Nalezeny zaznam: ")
        my_count = 0
        for employee in company.values():
            if user_age == employee["age"]:
                f1.write(f'{employee["first_name"]}, {employee["surname"]}, {employee["age"]}\n')
                print(employee)
                my_count += 1
        return f"Pocet nalezenych zaznamu: {my_count}"

def find_letter(user_letter):
    """
    finds employee based on first letter of surname inputed by user
    """
    with open("12. letter.txt", "w", encoding="utf-8") as f1:
        print("Nalezeny zaznam: ")
        my_count = 0
        for employee in company.values():
            if user_letter == employee["surname"][0]:
                f1.write(f'{employee["first_name"]}, {employee["surname"]}, {employee["age"]}\n')
                print(employee)
                my_count += 1
        return f"Pocet nalezenych zaznamu: {my_count}"


### Spusteni aplikace ################################################

# company = my_upload("12. employee.txt")
employee_application()
