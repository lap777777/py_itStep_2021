# Task 1
# Print the multiplication table for the user-defined number. If the user typed in 7, the output should be as follows:
#   7 * 1 = 7
#   7 * 2 = 14
#   7 * 3 = 21
number = int(input("Zadej cislo (0 - 10): "))
print("----Multiplication_table-----")
for i in range (1, 11):
    print(f"{number} * {i} = {number * i}")
print()

# Task 2
# Write a currency converter program. Implement a dialog with the user through a menu.
print("---Prevod z CZK---")
choice = int(input("Vyberte si menu na vymenu (1 pro USD, 2 pro EUR, 3 pro CHF): "))
amount = int(input("Zadejte castku v CZK: "))
fee = 0.01 * amount
print(f"Poplatek z transakce bude {fee:_.2f} CZK.")
amount1 = amount - fee
USD = 22.6
EUR = 25.6
CHF = 20.5
if choice == 1:
    amount2 = amount1 / USD
    print(f"Dostanete {amount2:_.2f} USD.")
elif choice == 2:
    amount2 = amount1 / EUR
    print(f"Dostanete {amount2:_.2f} EUR.")
elif choice == 3:
    amount2 = amount1 / CHF
    print(f"Dostanete {amount2:_.2f} CHF.")
else:
    print("Chyba, spatny vyber")
print()

# Task 3
# The user types in the start and end points of the range and a number. If the number is not in the range, the program asks the user to re-enter the number, and so on until the user enters the number correctly. The program displays all numbers in the range, highlighting the number with exclamation marks. For instance: 1 2 3 !4! 5 6 7.
number1 = int(input("Zadej spodni hranici rozsahu (cele cislo): "))
number2 = int(input("Zadej horni hranici rozsahu (cele cislo): "))
number3 = int(input("Vyber libovolne cislo v rozsahu zadanem vyse: "))
if number1 < number2:
    for i in range(number1, number2+1):
        if i == number3:
            print(f"!{i}! ", end="")
        else:
            print(f"{i} ", end="")
print()
print()

# Task 4
# Develop a game Guess the Number. The program chooses a number in the range from 1 to 500. The user tries to guess it. After each try, the program gives hints on whether the number is greater or less than the guessed number. In the end, the program displays statistics: how many tries it took to guess the number, how long it took. Provide an exit by entering 0 if the user is tired of guessing the number.
import random
import time
los = random.randint(1, 100)
print("_____Vitejte_u_hry:_Hadej_cislo!!!________")
pokus = 0
choice = 0
start_time = time.time()
while choice != los:
    choice = int(input("Vyber libovolne cislo v rozsahu 1 - 100: "))
    if choice == 0:
        break
    pokus = pokus + 1
    if choice > los:
        print("Zadane cislo bylo vyssi nez los.")
    elif choice < los:
        print("Zadane cislo bylo mensi nez los")
    else:
        print("*****************************************")
        print("Gratulace uhadnul jsi.")
        print(f"Vylosovane cislo bylo {los}.")
        print(f"Uhadnout ti trvalo {pokus} pokusu.")
        end_time = (time.time() - start_time)
        print(f"Uhadnout ti trvalo {end_time} sekund.")
        print("*****************************************")

print("Konec hry, diky za hru.")
print("*****************************************")

