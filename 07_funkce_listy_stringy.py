# 1) Vytvorte funkci, ktera vezme slovo a vytvori z nej:
#     - slovo v Pig Latin:
#     zacina samohlaskou dam na konec way:
#         - ear => earway
#         - elephant => elephantway
#     zacina souhlaskou (prvni dam na konec a pridam ay)
#         - computer => omputercay
#         - house => ousehay

def pig_latin(word):

    if word[0] in "aeiou":
        return f"{word}way"
    else:
        return f"{word[1:]}{word[0]}ay"

print(pig_latin("car"))
print(pig_latin("ear"))
print(pig_latin("house"))
print("---------------------------------------------------------")

# 2) tezsi verze
# pokud je v danem slove prvni pismeno velke, bude velke pismeno i ve vysledku

def pig_latin1(word):
    if word[0] in "aeiouAEIOU":
        result = word + "way"
    else:
        if word[0].isupper():
            result = word[1].upper() + word[2:] + word[0].lower() + "ay"
        else:
            result = word[1:] + word[0].lower() + "ay" 
    return result

print(pig_latin1("Car"))
print(pig_latin1("Ear"))
print(pig_latin1("House"))
print(pig_latin1("house"))
print("---------------------------------------------------------")

# 3) jeste tezsi verze
# slovo muze mit na konci textu nebo carku. Pokud tam je, bude na konci i ve vysledku
def pig_latin2(word):
    if word[0] in "aeiouAEIOU":
        if word[-1] in ",.":
            result = word[:-2] + "way" + word[-1]
        else:
            result = word + "way"
    else:
        if word[0].isupper():
            if word[-1] in [".", ","]:
                result = word[1].upper() + word[2:-1] + word[0].lower() + "ay" + word[-1]
            else:
                result = word[1].upper() + word[2:] + word[0].lower() + "ay"
        else:
            if word[-1] in [".", ","]:
                result = word[1:-1] + word[0].lower() + "ay" + word[-1] 
            else:
                result = word[1:] + word[0].lower() + "ay" 
    return result

print(pig_latin2("Car,"))
print(pig_latin2("Ear."))
print(pig_latin2("House,"))
print("---------------------------------------------------------")

# Priklad 4 - to same, ale s celou vetou (veta se nejdrive rozdeli na slova, nakonec se zase spoji. 
# muzete pouzit funkci ze sviceni jedna, nemusite uvazovat diakritiku a velka pismena.

def pig_latin_sentences(sentence):
    list = sentence.split()
    list1 = []
    for i in list:
        list1.append(pig_latin(i))
    return " ".join(list1)

text = "Sla Nanynka do eli atrhla lupeni pak to vsechno asnedla"
print(text)
print(pig_latin_sentences(text))

print("---------------------------------------------------------")

# Priklad 5 
# tajny jazyk Ubbi Dubbi. Napiste funkci, ktera vezme slovo, vytvori z nej nove slovo
# a pred kazdou samohlasku prida slovo "ub"
# octopus => uboctubopubus

def ubbi_dubbi(word):
    result = []
    for char in word:
        if char in "aeiouAEIOU":
            result.append("ub" + char)
        else:
            result.append(char)
    return "".join(result)

print(ubbi_dubbi("octopus"))
print("--------------------------------------------------------")

# sdruzeni funkci
def transform_sentence(sentence, transform_fn):
    sentence = sentence.split()
    result = []
    for word in sentence:
        result.append(transform_fn(word))
    return " ".join(result)

def tupa_funkce(word):
    return f"{word}tupa"

def dvakrat(word):
    return word + word

print(transform_sentence("this is a test", pig_latin))
print(transform_sentence("this is a test", ubbi_dubbi))
print(transform_sentence("this is a test", tupa_funkce))
print(transform_sentence("this is a test", dvakrat))
print("----------------------------------------------------------")

def scitej(a=0, b=0, c=0):   # defaultne nastavene na nulu, tak nemusim zadat vsechny parametry
    print(f"a je {a}")
    print(f"b je {b}")
    print(f"c je {c}")
    return a + b + c

print(scitej(5,7))              # misto c se doplni 0
print(scitej(5,7,8))            # pozicni argumenty
print(scitej(c=5, a=7, b=8))    # keywords arguments

print("---------------------------------------------------------")

# funkce ord() a chr()
print(ord("a"))   # pro znak vraci cislo poradi z ASCI tabulky (128 znaku, co je nove tak je v UNICODE - rozsirena ASCI tabulka)
print(ord("A"))
print("A"<"a")
print(chr(97))    # obracene, zadam poradi z UNICODE a vrati mi pismenko


