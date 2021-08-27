# Task 1
# The user types in a two-digit number. For example, 26. Display the value of the first and second digit on different lines. In our case, it will be as follows:
#   2
#   6
cifra = input("Zadej dvojciferne cislo: ")
print(cifra[0])
print(cifra[1])
print("----matematicky____")
cifra = int(cifra)
print(cifra // 10)
print(cifra % 10)
print()

# Task 2
# The user types in a three-digit number. For instance, 891. Print the value of the first, second, and third digit each on a new line. Also, print the sum of these numbers on a new line. In our case, it will be as follows:
#   8
#   9
#   1
#   18
cifra1 = input("Zadej trojciferne cislo: ")
prvni = int(cifra1[0])
druhe = int(cifra1[1])
treti = int(cifra1[2])
soucet = prvni + druhe + treti
print(prvni)
print(druhe)
print(treti)
print(soucet)
print("----matematicky----")
cifra1 = int(cifra1)
prvni = cifra1 // 100
druhe = cifra1 % 100 // 10
treti = cifra1 % 100 % 10
soucet = prvni + druhe + treti
print(prvni)
print(druhe)
print(treti)
print(soucet)
print()

# Task 3
# The user types in two digits. Create a number containing these digits. If the typed in digits are 9 and 7, the created number will be 97.
prvni = input("Zadej prvni cislo: ")
druhe = input("Zadej druhe cislo: ")
cifra2 = prvni + druhe
print(cifra2)
print("---matematicky-----")
prvni = int(prvni)
druhe = int(druhe)
print(10 * prvni + druhe)
print()

# Task 4
# The user types in Celsius temperature. Convert it to Fahrenheit and display the result on the screen.
celsius = int(input("Zadej teplotu ve stupnich Celsia: "))
fahrenheit = celsius * 1.8 + 32
print(f"{celsius} stupnu Celsia je {fahrenheit} stupnu Fahrenheita.")
print()



