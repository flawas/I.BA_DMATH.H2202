# Author Flavio Waser

def modulo(number, mod):
    number, mod = number, mod
    print(number % mod)

in_number = int(input("Zahl = "))
in_mod = int(input("Modulo = "))
modulo = modulo(in_number, in_mod)