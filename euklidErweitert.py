# Author Joel Kessler
def euclidean_extended(a, b):
    x, y = a, b
    if a < b:
        print("a muss grösser als b sein. Vertausche diese.")
        return [None, None, None, None]
    top_rows = [[a, None, 1, 0], [b, a // b, 0, 1]]
    print(top_rows[0])
    print(top_rows[1])
    breaker_step = 0
    while breaker_step < 25:
        step_row = [None, None, None, None]
        breaker_step += 1
        step_row[0] = top_rows[0][0] - top_rows[1][0] * top_rows[1][1]
        if step_row[0] <= 0:
            print(step_row)
            break
        step_row[1] = top_rows[1][0] // step_row[0]
        step_row[2] = top_rows[0][2] - top_rows[1][2] * top_rows[1][1]
        step_row[3] = top_rows[0][3] - top_rows[1][3] * top_rows[1][1]
        print(step_row)
        top_rows[0] = top_rows[1]
        top_rows[1] = step_row
    return top_rows[1]

in_a = int(input("a = "))
in_b = int(input("b = "))
ggt, _, x, y = euclidean_extended(in_a, in_b)
print("GGT:", ggt)
print("x:", x)
print("y:", y)
print("Diophantische Gleichung: " + str(in_a) + " * " + str(x) + " + " + str(in_b) + " * " + str(y) + " = 1")
print("Allgemein (k E N): " + str(in_a) + " * " + "(" + str(x) + " + " + str(in_b) + " * k) + " + str(in_b) + " * " + "(" + str(y) + " - " + str(in_a) + " * k) = 1")