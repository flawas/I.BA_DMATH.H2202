#Author Flavio Waser
def binary(zahl):
    temp = format(zahl, "b")
    return temp

zahl = int(input("Zahl:"))
binzahl = binary(zahl)
print("Binär:", binzahl)