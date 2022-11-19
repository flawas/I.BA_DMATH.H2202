# Author Joel Kessler und Ramon Stoffel
def euler_phi_numbers(n):
    zn = [x for x in range(n)]
    relatives_primes = []
    for i in zn:
        if ggt(n, zn[i])==1:
            relatives_primes.append(zn[i])
        else:
            continue
    return relatives_primes

def ggt(x , y):
    if y == 0:
        return x
    return ggt(y, x % y)

def modular_invers(a, n):
    v = 1
    d = a
    u = (a == 1)
    t = 1-u
    if (t == 1):
        c = n % a
        u = n // a
        while c != 1 and t == 1:
            q = d // c
            d = d % c
            v = v + q*u
            t = (d != 1)
            if (t == 1):
                q = c // d
                c = c % d
                u = u + q*v
        u = v*(1 - t) + t*(n - u)
    return u

def quadratic_remainders(n):
    remainders = []
    Z_n = euler_phi_numbers(n)
    for i in Z_n:
        remainders.append(i ** 2 % n)
    quadratic_remainders_dict = dict.fromkeys(sorted(Z_n))
    # Leere listen erstellen
    for key in quadratic_remainders_dict.keys():
        quadratic_remainders_dict[key] = []
    # Ordne x quadrate den Restklassen zu
    for remainder_index in range(0, len(remainders)):
        quadratic_remainders_dict[remainders[remainder_index]].append(Z_n[remainder_index])
    # Entferne leere Restklassen
    for key in list(quadratic_remainders_dict.keys()):
        if quadratic_remainders_dict[key] == []:
            quadratic_remainders_dict.pop(key)
    return remainders, quadratic_remainders_dict, Z_n

n = int(input("n = "))
r, qrd, Z_n = quadratic_remainders(n)
print("Z({})*: {}".format(n, Z_n))
print("x-Quadrate:", r)
print("Restklassen:", qrd)