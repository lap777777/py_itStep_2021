
print("---------------------------------------------------------")
print("************************ UKOLY **************************")
print("---------------------------------------------------------")
# DU
# Priklad 1
# vytvor funkci, ktera spocita, kolik je ve slove samohlasek a vrati pocet
# elephant => 3
def vowel(word):
    list1 = [i for i in word if i in "aeiouAEIOU"]
    return len(list1)

word = "elephant"
print(f"Pocet samohlasek v zadanem slove: {vowel(word)}")

print("---------------------------------------------------------")

# Priklad 2 
# vytvor funkci, ktera spocita kolikrat se ve slove vyskytuje sekvece "bob"
# azcbobobegghakl => 2
def sekvence(word):
    my_count = 0
    for i in range(len(word)-2):
        if word[i:i+3] == "bob":
            my_count += 1
    return my_count

word = "azcbobobegghakl"
print(f"Sekvence \"bob\" se nachazi v zadanem slove {sekvence(word)}x.")

print("---------------------------------------------------------")

# Priklad 3
# vytvor funkci, ktera vezme retezec a seradi v nem pismena podle abecedy:
def sort_word(word):
    my_list = list(word)
    my_list.sort()
    return "".join(my_list)

print(sort_word("mlkjihgfedcba"))
print(sort_word("chobotnice"))

print("---------------------------------------------------------")
# Priklad 4
# vytvor funkci, ktera vezme retezec, najde nejdelsi podretezec, ve ktrem jsou pismena serazena podle abecedy
# "azcbobogegghakl" => "beggh"
# ord a chr funkce


def longest1(my_string):
    total_longest_str = ""
    actual_longest_str = ""
    my_string = my_string.lower()
    last_char = "a"                 # ord(a) = 97 - pomocna promenna
    for char in my_string:
        if ord(char) >= ord(last_char):
            actual_longest_str += char
        else:
            if len(actual_longest_str) > len(total_longest_str):
                total_longest_str = actual_longest_str
            actual_longest_str = char
        last_char = char
    if len(actual_longest_str) > len(total_longest_str):
        total_longest_str = actual_longest_str
    return total_longest_str

print("------Alternativa-----------")
def longest2(s):
    f = ""
    for i in range(len(s)):
        r = s[i]
        while len(s) > i + 1 and s[i] <= s[i+1]:
            i += 1
            r += s[i]
        if len(r) > len(f): 
            f = r
    return f

print(longest1("azcbobogbegghz"))
print(longest2("azcbobogbegghz"))

print("---------------------------------------------------------")
# Priklad 5 - Ceasarova sifra
# zadam slovo a kazde pismenko vymenim za pismenko, ktere je v UNICODE o jedno vetsi
# ahoj => bipk (posun o jedna)
# ahoj => dkrm (posun o tri)
# mala i velka pismena, posun o jedna nebo o 3 a pozor na konec abeceny - if osetrit
# prvni funkce na zakodovani, druha funkce na rozkodovani
# a => b
# b => c
# z => a

# zakodovani
def caesar1(word):
    word = word.lower()
    cipher = ""
    for i in word:
        code = ord(i) + 1
        if code > ord("z"):
            code = ord("a")
        cipher += chr(code)
    return cipher

def caesar3(word):
    word = word.lower()
    cipher = ""
    for i in word:
        code = ord(i) + 3
        if code > ord("z"):
            code = ord("c")
        elif code > ord("y"):
            code = ord("b")
        elif code > ord("x"):
            code = ord("a")
        cipher += chr(code)
    return cipher

# odkodovani:
def caesar_1(cipher):
    cipher = cipher.lower()
    word = ""
    for i in cipher:
        code = ord(i) - 1
        if code < ord("a"):
            code = ord("z")
        word += chr(code)
    return word

def caesar_3(cipher):
    cipher = cipher.lower()
    word = ""
    for i in cipher:
        code = ord(i) - 3
        if (code+3) ==  ord("a"):
            code = ord("x")
        elif (code+3) == ord("b"):
            code = ord("y")
        elif (code+3) == ord("c"):
            code = ord("z")
        word += chr(code)
    return word

print(caesar1("ahoj"))
print(caesar3("ahoj"))
print(caesar1("zItra"))
print(caesar3("zitra"))
print()
print(caesar_1("bipk"))
print(caesar_3("dkrm"))
print(caesar_1("ajusb"))
print(caesar_3("clwud"))

print("---------------------------------------------------------")
print()




