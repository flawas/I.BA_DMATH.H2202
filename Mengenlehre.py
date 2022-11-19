# Author Joel Kessler
def set_values(A, B):
    AANDB = set([a for a in A if a in B])
    AORB = A.union(B)
    ADIFFB = set([a for a in A if a not in B])
    BDIFFA = set([b for b in B if b not in A])
    return AANDB, AORB, ADIFFB, BDIFFA
print("Abbruch mit allen Werten = esc")
print("A:")
more_data = True
A = []
while more_data:
    a = input("a{}:".format(len(A)))
    if a == "esc":
        more_data = False
        continue
    A.append(a)
more_data = True
B = []
while more_data:
    b = input("b{}:".format(len(B)))
    if b == "esc":
        more_data = False
        continue
    B.append(b)
AANDB, AORB, ADIFFB, BDIFFA = set_values(set(A), set(B))
print("A ∩ B: ", sorted(AANDB))
print("A ∪ B: ", sorted(AORB))
print("A \ B:", sorted(ADIFFB))
print("B \ A:", sorted(BDIFFA))