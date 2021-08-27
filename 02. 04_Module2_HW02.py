# Task 1
# The user types in a number from 1 to 7 that represents a day of the week. Print its name. For example, if the num-ber is 1, then you should display “Monday”; if 2, display “Tuesday,” etc. 

day = int(input("Zadej cislo pro den v tydnu: (1 Monday .... 7 Sunday): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4: 
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Sathurday")
elif day == 7:
    print("Sunday")
else:
    print("Chyba. Zadej priste cislo mezi 1-7.")
print()


# Task 2
# The user types in a number from 1 to 12 that represents a month. Print its name. For example, if the number is 1, display “January”; if 2, display “February,” etc. 
month = int(input("Zadej cislo pro mesic v roce: (1 January .... 12 December): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4: 
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Chyba. Zadej priste cislo mezi 1-7.")
print()

# Task 3
# The user types in a number. If the number is greater than 0, print “Your number is positive”; if it is less than zero, print “Your number is negative”; if it is equal to 0, print “Your number is equal to zero.”
number = int(input("Zadej libovolne zaporne/kladne cele cislo: "))

if number < 0:
    print(f"Zadane cislo {number} je zaporne.")
elif number > 0:
    print(f"Zadane cislo {number} je kladne.")
elif number == 0:
    print("Bylo zadano cislo 0.")
else:
    print("Chyba")
print()

# Task 4
# The user types in two numbers. Determine if these numbers are equal. If they are not, print them in ascending order.
number1 = int(input("Zadej prvni cislo: "))
number2 = int(input("Zadej druhe cislo: "))

if number1 == number2:
    print("Cisla jsou shodna")
elif number1 < number2:
    print(number1, number2)
elif number1 > number2:
    print(number2, number1)
print()
