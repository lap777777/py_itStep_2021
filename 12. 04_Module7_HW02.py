
# Task 1
# Develop an information system Employees. The app should provide data input, editing the employee’s data, deleting an employee, searching for an employee by last name, outputting information about all employees of the specified age or whose last name begins with the specified letter. Pro- vide the possibility to save the found information to a file. The full list of employees is also saved to a file (automatically when exiting the app, by the user’s command at runtime). The employee list is loaded from the file specified by the user when the app starts.

# application:
#   - input data
#   - editing data
#   - deleting employee
#   - searching by last name
#   - searching by age
#   - search by first letter of last name

# input - employee list loaded when application starts
# output - save found information to file
# output - full list save to file - automatically when exiting the app, users command at runtime



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


"""
Deletes en employee
employee_id - id of the employee
"""
def del_employee(employee_id: str):    # za dvojtecku davam typ promenne - parametru, co vracim
    deleted_employee = company[employee_id]
    del company[employee_id]
    return deleted_employee

deleted_employee = del_employee("os3")

def find_phone(phone):
    for employee in company.values():
        if phone == employee["phone"]:
            return employee["name"]  
            # return employee - vrati cely podslovnik, 
    return "Employee with this phone not found"

print(find_phone(3456789451))
print(find_phone("zadne cislo"))


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

print("-------------------------------------------------------------")
