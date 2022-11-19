# Author Flavio waser
def modulo(x, y):
    x, y = x, y
    return x % y

in_number = float(input("Zahl = "))
in_modulo = float(input("Modulo = "))
modulo1 = modulo(in_number, in_modulo)
print("Rest:", modulo1)