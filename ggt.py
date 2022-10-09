#Author Flavio Waser
import math

def ggt(x, y):
    x,y = x,y
    return math.gcd(x,y)

in_number1 = int(input("Zahl 1 = "))
in_number2 = int(input("Zahl 2 = "))
ggt = ggt(in_number1, in_number2)
print("GGT:", ggt)