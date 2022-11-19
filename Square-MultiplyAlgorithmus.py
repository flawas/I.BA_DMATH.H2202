#Author Joel Kessler
def square_and_multiply_algorithm(basis, exponent, modulo):
    x = basis
    ex_bin = str(bin(exponent))[2:].replace("1", "QM").replace("0", "Q")[2:]
    y_step = x
    print(str(y_step), end=" -> ")
    for letter in ex_bin:
        if y_step >= modulo:
            print(str(y_step) + " mod " + str(modulo), end=" -> ")
            y_step = y_step % modulo
        if letter == "Q":
            y_step = y_step ** 2
            print(str(y_step) + " Q ", end=" -> ")
        if letter == "M":
            y_step = y_step * x
            print(str(y_step) + " M ", end=" -> ")
    print(str(y_step) + " mod " + str(modulo))
    if y_step >= modulo:
        y_step = y_step % modulo
    return y_step
basis, exponent, modulo = int(input("basis = ")), int(input("exponent = ")), int(input("modulo = "))
mod_val = square_and_multiply_algorithm(basis, exponent, modulo)
print("{}^{} mod {} = {}".format(basis, exponent, modulo, mod_val))