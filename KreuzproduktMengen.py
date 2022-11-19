# Author Joel Kessler
def cross_product(A, B):
    res = []
    for b in B:
        for a in A:
            res.append((a, b))
    return res
    
A = []
B = []
print("Abbruch mit allen Werten = esc")
print("Menge A:")
more_data = True
while more_data:
    a = input("a{}:".format(len(A)))
    if a == "esc":
        more_data = False
        continue
    A.append(a)
print("Menge B:")
more_data = True
while more_data:
    b = input("b{}:".format(len(B)))
    if b == "esc":
        more_data = False
        continue
    B.append(b)
A = sorted(set(A))
B = sorted(set(B))
print("--------")
print(sorted(cross_product(A, B)))