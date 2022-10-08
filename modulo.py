# Author Flavio waser

from operator import mod


def modulo(number, modulo):
    number, modulo = number, modulo
    return number % modulo

in_number = int(input("Zahl = "))
in_modulo = int(input("Modulo = "))
modulo1 = modulo(in_number, in_modulo)
print("Modulo:", modulo1)
