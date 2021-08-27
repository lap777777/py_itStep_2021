# Task 1
# The user types in the time in seconds since the beginning of the day. Based on the user’s choice, calculate how many hours, minutes, and seconds are left until midnight.
time = int(input("Zadej dobu v sekundach od zacatku dne: "))
day = 24 * 60 * 60
remaining = day - time
hodina = time // 3600
minuta = time % 3600 // 60
sekunda = time % 3600 % 60
hodina1 = remaining // 3600
minuta1 = remaining % 3600 // 60
sekunda1 = remaining % 3600 % 60
print(f"Zadany cas: {hodina}:{minuta}:{sekunda}")
print(f"Zbyva do konce dne: {hodina1}:{minuta1}:{sekunda1}")
print()

# Task 2
# The user types in the diameter of a circle. Based on the user’s choice, calculate the area or perimeter of the circle.
diameter = int(input("Zadej prumer kruhu: "))
choice = int(input("Zadej vypocet ctverce (1 obsah, 2 obvod): "))
if choice == 1:
    area = 3.14 * (diameter / 2) ** 2
    print(f"Obsah kruhu je {area:.2f}")
elif choice == 2:
    perimeter = 2 * 3.14 * (diameter / 2)
    print(f"Obvod ctverce je {perimeter:.2f}")
else:
    print("Chybne zadani")
print()

# Task 3
# The user types in the cost of one gaming console, their quantity, and a discount. Based on the user’s choice, calculate the total amount of the order or the cost of one console, including the discount.
costs = int(input("Zadej cenu konsole: "))
quantity = int(input("Zadej mnozstvi: "))
discount = int(input("Zadej velikost slevy jako cele cislo: "))
choice = int(input("Zadej svoji volbu: (1 - celkova cena, 2 - cena jedne konsole vcetne slevy"))
total_costs = costs * (1 - discount / 100) * quantity
price_with_discount = total_costs / quantity
if choice == 1:
    print(f"Celkova cena je {total_costs}")
elif choice == 2:
    print(f"Cena jedne konsole vcetne slevy je: {price_with_discount}")
print()

# Task 4
# The user types in the file size in gigabytes and the band- width in bits per second. Based on the user’s choice, calcu- late how many hours, or minutes, or seconds it will take to download a file.
giga = int(input("Zadej velikost souboru v gigabitech: "))
download = int(input("Zadej prenosovou rychlost bitech za sekundu:  "))
choice = int(input("Zadej zobrazeni vysledku: (1 - v hodinach, 2 - v minutach, 3 - v sekundach"))
result = (giga / 1000000) / download
if choice == 1:
    print(f"Rychlost stazeni v hodinach: {result / 60 / 60}")
elif choice == 2:
    print(f"Rychlost stazeni v minutach: {result / 60}")
elif choice == 3:
    print(f"Rychlost stazni v sekundach: {result}")
else:
    print("Chybne zadani.")
print()

# Task 5
# The user types in an hour (from 0 to 23). If the received value is in the range from 0 to 6, print Good Night; if from 6 to 13, print Good Morning; if from 13 to 17, print Good Day; if from 17 to 0, print Good Evening. The upper limit of the range is not included. For instance, if 6 is typed in, 6 belongs to the range from 6 to 13.
hour = int(input("Zadej hodinu (cele cislo 0 az 23): "))
if hour <= 6:
    print("Good Night.")
elif hour <= 13:
    print("Good Morning.")
elif hour <= 17: 
    print("Good Day.")
elif hour <= 23:
    print("Good Evening.")
else:
    print("Spatne zadani, priste cislo mezi 0-23")
print()