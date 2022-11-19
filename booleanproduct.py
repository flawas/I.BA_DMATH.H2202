# Author Joel Kessler
def boolean_product(A, B, n_r, m_r):
    res = []
    for row_i in range(0, n_r):
        row = []
        for col_i in range(0, m_r):
            sel_row = A[row_i]
            sel_col = [B_row[col_i] for B_row in B]
            product_row_col = 0
            # (....) or (....)
            for sel_row_e_i in range(0, len(sel_row)):
                sel_row_e = sel_row[sel_row_e_i]
                sel_col_e = sel_col[sel_row_e_i]
                
                if sel_row_e == 1 and sel_col_e == 1:
                    # (a1 and b1) or (....)
                    product_row_col = 1
                    break
            row.append(product_row_col)
        res.append(row)
    return res
    
A = []
B = []
print("Dimension Linke A-Matrix (n x m):")
n_a = int(input("n:"))
m_a = int(input("m:"))
print("Dimension Rechte B-Matrix (n x m):")
n_b = int(input("n:"))
m_b = int(input("m:"))
# (n x m) (n x m)
if m_a != n_b:
    print("Dimensionsfehler.")
else:
    print("Resultierende Matrix: ({},{})".format(n_a, m_b))

    print("Matrix A:")
    for row_i in range(0, n_a):
        row = []
        for pos_i in range(0, m_a):
            row.append(int(input("Position: ({}, {}): ".format(row_i+1, pos_i+1))))
        A.append(row)
    print("Matrix B:")
    for row_i in range(0, n_b):
        row = []
        for pos_i in range(0, m_b):
            row.append(int(input("Position: ({}, {}): ".format(row_i+1, pos_i+1))))
        B.append(row)
        
    print("Matrix A:")
    for row in A:
        print(row)
        
    print("Matrix B:")
    for row in B:
        print(row)
        
res = boolean_product(A, B, n_a, m_b)
print("Boolsches Produkt:")
for row in res:
    print(row)