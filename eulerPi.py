# Author Ramon Stoffel
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
n = int(input("Geben Sie Z-n ein:  "))
print("------------")
res = euler_phi_numbers(n)
print("EULERISCHE PHI FUNKTION: ",len(res))
print("------------")
print("TEILERFREMDE-ELEMENTE / Z-STERN: ",res)
mod_inv_list = []
for i in range(len(res)):
    inv_mod = modular_invers(res[i],n)
    if inv_mod == True:
        mod_inv_list.append(1)
    else:
        mod_inv_list.append(inv_mod)
print("------------")
print("INVERSE VON TEILERFREMDEN_ELEMENTEN AUS Z-STERN: ",mod_inv_list)