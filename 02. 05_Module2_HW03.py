# Task 1
# The user types in a number from 1 to 100. If the number is a multiple of 3 (divisible by 3 without remainder), print the word Fizz. If the number is a multiple of 5, print the wordBuzz. If the word is a multiple of 3 and 5, print Fizz Buzz. If the word is not a multiple of 3 and 5, print the number.
# If the user typed in a number out of the range, print an error message.
number = int(input("Zadej libovolne cislo od 1 do 100: "))

if number < 1 or number > 100:
    print("Chyba, nebylo zadano cislo v rozmezi 1-100")
elif number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz, delitelne 3 a 5.")
elif number % 3 == 0:
    print("Fizz, delitelne 3.")
elif number % 5 == 0:
    print("wordBuzz, delitelne 5.")
elif number % 3 != 0 and number % 5 != 0:
    print(number, "neni delitelne 5 nebo 3")
print()

# Task 2
# Write a program that, at the user’s choice, raises the typed in number to the power of 0 through 7.
number = int(input("Zadej libovolne kladne cele cislo: "))
choice = int(input("Zadej mocninu od 0 do 7 vcetne: "))
if choice == 0:
    print(f"0. mocnina cisla {number}: {number ** 0}")
elif choice == 1:
    print(f"1. mocnina cisla {number}: {number ** 1}")
elif choice == 2:
    print(f"2. mocnina cisla {number}: {number ** 2}")
elif choice == 3:
    print(f"3. mocnina cisla {number}: {number ** 3}")
elif choice == 4:
    print(f"4. mocnina cisla {number}: {number ** 4}")
elif choice == 5:
    print(f"5. mocnina cisla {number}: {number ** 5}")
elif choice == 6:
    print(f"6. mocnina cisla {number}: {number ** 6}")
elif choice == 7:
    print(f"7. mocnina cisla {number}: {number ** 7}")
print()

# Task 3
# Write a program that calculates the cost of a call for dif-ferent mobile phone operators. The user types in the cost of the call and chooses operators for the outgoing and incoming calls. Print the cost.

# Task 4
# The salary of a salesperson is $200 + percentage of sales as follows: up to $500 — 3%, from 500 to 1000 — 5%, over 1000 — 8%. The user types in the sales for three salespersons. Determine their salary, the best salesperson, give him or her a $200 bonus, print the result.  

salesman1 = int(input("Zadej vysi prodeje 1. prodejce: "))
salesman2 = int(input("Zadej vysi prodeje 2. prodejce: "))
salesman3 = int(input("Zadej vysi prodeje 3. prodejce: "))

if salesman1 <= 500:
    salary1 = 200 + 0.03 * salesman1
elif salesman1 <= 1000:
    salary1 = 200 + 0.03 * 500 + 0.05 * (salesman1 - 500)
elif salesman1 > 1000:
    salary1 = 200 + 0.03 * 500 + 0.05 * 500 + 0.08 * (salesman1 - 1000)
else:
    print("Chyba")

if salesman2 <= 500:
    salary2 = 200 + 0.03 * salesman2
elif salesman2 <= 1000:
    salary2 = 200 + 0.03 * 500 + 0.05 * (salesman2 - 500)
elif salesman2 > 1000:
    salary2 = 200 + 0.03 * 500 + 0.05 * 500 + 0.08 * (salesman2 - 1000)
else:
    print("Chyba")

if salesman3 <= 500:
    salary3 = 200 + 0.03 * salesman3
elif salesman3 <= 1000:
    salary3 = 200 + 0.03 * 500 + 0.05 * (salesman3 - 500)
elif salesman3 > 1000:
    salary3 = 200 + 0.03 * 500 + 0.05 * 500 + 0.08 * (salesman3 - 1000)
else:
    print("Chyba")


if salary1 > salary2:
    if salary1 > salary3:
        salary1 += 200
        print("Nejlepsi prodejce je salesman1.")
    else:
        salary3 += 200
        print("Nejlepsi prodejce je salesman3.")
else:
    if salary2 > salary3:
        salary2 += 200
        print("Nejlepsi prodejce je salesman2.")
    else:
        salary3 += 200
        print("Nejlepsi prodejce je salesman3.")
print(f"Salesperson1 ma plat {salary1} USD.")
print(f"Salesperson2 ma plat {salary2} USD.")
print(f"Salesperson3 ma plat {salary3} USD.")
print()
