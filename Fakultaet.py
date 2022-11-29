# Author Flavio Waser
import math

def fakultaet(vara):
    a = math.factorial(vara)
    return a

in_number1 = int(input("Zahl= "))
fak = fakultaet(in_number1)
print("Fakultät:", fak)