# Task 1
# Write a function that prints formatted text given below:
# “Don’t let the noise of others’ opinions
#  drown out your own inner voice.”
#  Steve Jobs

def citat():
    print("\"Don’t let the noise of others’ opinions")
    print("    drown out your own inner voice.\"")
    print("            Steve Jobs")

citat()
print()

# Task 2
# Write a function that takes two numbers as a parameter and displays all odd numbers in between.

def licha_cisla(a, b):
    for i in range(a, b+1):
        if i % 2 != 0:
            print(i, end=" ")

licha_cisla(10, 30)
print()
print()

# Task 3
# Write a function that prints a horizontal or vertical line made out of some symbol. The function takes the following as a parameter: the line’s length, direction, symbol.
def linie(delka, smer, symbol):
    if smer == "h":
        for i in range(delka):
            print(symbol, end="")
        print()
    elif smer == "v":
        for i in range(delka):
            print(symbol)
    else:
        print("chybne zadani")
    
linie(30, "h", "*")
linie(10, "v", "?")
print()

# Task 4
# Write a function that returns the greatest of four numbers. Numbers are passed as parameters.
def maximum(a, b, c, d):
    return max(a, b, c, d)

print(f"Maximum je: {maximum(1, 2, 3, 4)}")
print()

# Task 5
# Write a function that returns the sum of numbers in a specified range. The start and end points of the range are passed as parameters.

def soucet1(a, b):
    soucet = 0
    for i in range(a, b+1):
        soucet += i
    return soucet

my_sum = soucet1(10, 20) 
print(f"Soucet zadanych cisel je: {my_sum}")
print()

# Task 6
# Write a function that checks if a number is prime. The number is passed as a parameter. If the number is prime, return true, otherwise false.
def je_prvocislo(cislo):   # v nazvu je sloveso (is_prime) - cekam, ze budu vracet boolean
    for i in range(2, cislo):
        if cislo % i == 0:
            return False
    return True

print(je_prvocislo(20))
print(je_prvocislo(11))
print(je_prvocislo(1))
print(je_prvocislo(8))
print(je_prvocislo(7))
print()

# Task 7
# Write a function that checks if a six-digit number is lucky. The number is passed as a parameter. If the number is lucky, return true, otherwise false.
# A lucky six-digit number is a number with the sum of its first three digits being equal to the sum of its last three digits. For example, 123420 is a lucky number because 1+2+3 = 4+2+0, and 723422 is not because 7+2+3 != 4+2+2.

def is_lucky_number(cislo):   # is_lucky_number - vraci True/False
    cislo = str(cislo)
    sum1 = int(cislo[0]) + int(cislo[1]) + int(cislo[2])
    sum2 = int(cislo[3]) + int(cislo[4]) + int(cislo[5])
    if sum1 == sum2:
        return True
    else:
        return False
 
def is_lucky_number1(cislo):
    s = str(cislo)
    s1= s[:len(s)//2]
    s2 = s[len(s)//2:]
    i1 = [int(j) for j in s1]
    i2 = [int(j) for j in s2]
    sum1 = sum(i1)
    sum2 = sum(i2)
    if sum1 == sum2:
        return True
    else:
        return False


print(is_lucky_number(123420))
print(is_lucky_number(723422))
print(is_lucky_number(777777))
print("--------alternativa----------------")
print(is_lucky_number1(12345677654321))
print(is_lucky_number1(17234221))
print(is_lucky_number1(97777779))
print()
