#Author Flavio Waser
import math

def binary(zahl):
    #temp = bin(zahl)
    temp = format(zahl, "b")
    return temp

zahl = int(input("Zahl:"))
binzahl = binary(zahl)
print("Binär:", binzahl)