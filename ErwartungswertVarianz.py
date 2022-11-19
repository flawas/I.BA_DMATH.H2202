# Author Joel Kessler V2
def e_randomvar(k_and_ps):
    E_X, VAR_X, SD_X = 0, 0, 0
    # Berechne E(X)
    for k_and_p in k_and_ps:
        k, p = k_and_p
        E_X += k * p
    # Berechne VAR(X)
    for k_and_p in k_and_ps:
        k, p = k_and_p
        VAR_X += ((k - E_X) ** 2) * p
    
    return E_X, VAR_X, VAR_X ** (1/2)

# Based on: https://www.johndcook.com/blog/2010/10/20/best-rational-approximation/
def farey(x, N):
    # y = Ganzzahl faktor
    y = 0
    if x % 1 > 0:
        y = x - (x % 1)
        x = x % 1
    if x == 0:
        return y
    a, b = 0, 1
    c, d = 1, 1
    while (b <= N and d <= N):
        mediant = float(a+c)/(b+d)
        if x == mediant:
            if b + d <= N:
                return "{}/{}".format(int(y * b+d) + a+c, b+d)
            elif d > b:
                return "{}/{}".format(int(y * d) + c, d)
            else:
                return "{}/{}".format(int(y * b) + a, b)
        elif x > mediant:
            a, b = a+c, b+d
        else:
            c, d = a+c, b+d
    if (b > N):
        return "{}/{}".format(int(y * d) + c, d)
    else:
        return "{}/{}".format(int(y * b) + a, b)

more_data = True
print("Abbruch mit allen Werten = esc, BRUECHE UNTERSTUETZT")
print("Ausgabe: E(X) / VAR(X) / SD(X):")
data = []
while more_data:
    print("n-te Variable:", len(data))
    k = input("k:")
    p = input("P(X=k):")
    if k == "esc" and p == "esc":
        more_data = False
        continue
    data.append((float(eval(k)), float(eval(p))))

E_X, VAR_X, SD_X = e_randomvar(data)
print("------------")
print("E(X): ", farey(E_X, 1000), " -> ", round(E_X, 8))
EX_2 = VAR_X + (E_X ** 2)
print("E(X^2): ", farey(EX_2, 1000), " -> ", round(EX_2, 8))
print("VAR(X): ", farey(VAR_X, 1000), " -> ", round(VAR_X, 8))
print("SD(X): ", round(SD_X, 8))