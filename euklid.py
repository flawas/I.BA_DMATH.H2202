# Author Joel Kessler
def euclidean(a, b):
    x, y = a, b
    if a < b:
        print("a muss grösser als b sein. Vertausche diese.")
        return None
    previous_row = [a, a // b, b, a - (a // b) * b]
    breaker_step = 0
    while breaker_step < 25:
        print("{} = {} * {} + {}".format(previous_row[0],previous_row[1],previous_row[2],previous_row[3]))
        breaker_step += 1
        if previous_row[3] == 0:
            return previous_row[2]
        step_row = [previous_row[2], previous_row[2] // previous_row[3], previous_row[3], previous_row[2] - (previous_row[2] // previous_row[3]) * previous_row[3]]
        if step_row[3] <= 0:
            print("{} = {} * {} + {}".format(step_row[0],step_row[1],step_row[2],step_row[3]))
            return step_row[2]
        previous_row = step_row
    return None

in_a = int(input("a = "))
in_b = int(input("b = "))
ggt = euclidean(in_a, in_b)
print("GGT:", ggt)