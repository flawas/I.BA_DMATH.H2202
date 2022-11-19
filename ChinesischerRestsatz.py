# Author Flavio Waser
def calc_residual(h, a, d):
    if a <= d:
        raise ValueError("a must be larger than d")
    for i in range(1, a+1):
        if (h * i) % a == d:
            return i
    assert False, "not possible"

def chinesischer_restesatz(a, b, c, d, e, f):
    h1 = b * c
    solution1 = calc_residual(h1, a, d)
    h2 = a * c
    solution2 = calc_residual(h2, b, e)
    h3 = a * b
    solution3 = calc_residual(h3, c, f)
    return (solution1*h1 + solution2*h2 + solution3*h3) - a*b*c