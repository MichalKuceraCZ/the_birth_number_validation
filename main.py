# Napiste funkci validujici rodne cislo, funkce bere jako parameter string s rodnym cislem,
# a vrati True nebo False v zavislosti na vysledku validace. K funkci pridejte positivni a negativni Pytest test case.
# Zkuste použit programování s cyklem.

def rodne_cislo(cislo):
    number_in = []
    for i in cislo:
        if i.isdigit():
            number_in += i
        print(number_in)
    return len(number_in) == 10

def rodne_cislo1(cislo):
    while cislo:
        if cislo == "/":
            break
        return len(cislo) == 11
