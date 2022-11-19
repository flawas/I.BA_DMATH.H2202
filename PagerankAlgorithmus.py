# Author Joel Kessler
approx_decimal = 100000
def farey(x, N):
    a, b = 0, 1
    c, d = 1, 1
    while (b <= N and d <= N):
        mediant = float(a+c)/(b+d)
        if x == mediant:
            if b + d <= N:
                return a+c, b+d
            elif d > b:
                return c, d
            else:
                return a, b
        elif x > mediant:
            a, b = a+c, b+d
        else:
            c, d = a+c, b+d
    if (b > N):
        return c, d
    else:
        return a, b

def gauss_jordan(a):
    n = len(a)
    x = [0 for _ in range(0, len(a))]
    # Applying Gauss Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            print("Divide by zero detected!")
            return
        for j in range(i+1, n):
            ratio = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]
    # Back Substitution
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = x[i]/a[i][i]
    return x

def pagerank_algorithm(edges, d):
    V = sorted(set(sum(edges, ())))
    N = len(V)
    res = []
    #print(["PR[{}]".format(i) for i in V])
    rhs = []
    for i in V:
        sum_of_pr = []
        res_row = [0 for _ in V]
        res_row[V.index(i)] = 1
        # Endknoten potential_j[1]
        j_to_is = [potential_j for potential_j in edges if potential_j[1] == i]
        #print(i, "->", j_to_is)
        for j_to_i in j_to_is:
            # j = j_to_i[0]
            c_j = len([j_outgoing for j_outgoing in edges if j_outgoing[0] == j_to_i[0]])
            res_row[V.index(j_to_i[0])] += d * (1 / c_j) * -1
            if c_j == 1:
                sum_of_pr.append("PR[{}]".format(j_to_i[0]))
            else:
                sum_of_pr.append("PR[{}] * (1/{})".format(j_to_i[0], c_j))
        sum_of_pr = " + ".join(sum_of_pr)
        if sum_of_pr == "":
            sum_of_pr = "0"
        sum_of_pr = "({})".format(sum_of_pr)
        #d * sum_of_pr + (1 - d) * (1 / N)
        d_approx = farey(d, approx_decimal)
        one_sub_d_approx = farey((1 - d), approx_decimal)
        pr_node = "PR[{}] = ({}/{}) * {} + ({}/{}) * (1/{})".format(i, d_approx[0], d_approx[1], sum_of_pr, one_sub_d_approx[0], one_sub_d_approx[1], N)
        print(pr_node)
        rhs.append((1 - d) * (1 / N))
        res.append(res_row)
    #for row in res:
    #    print(row, rhs[res.index(row)])
    for rhs_index in range(0, len(rhs)):
        res[rhs_index].append(rhs[rhs_index])
    res_eval = gauss_jordan(res)
    # Displaying solution
    print("Loesung: ")
    #sorted_res_eval = dict.fromkeys(res_eval)
    for x_i in range(0, len(res_eval)):
        x = res_eval[x_i]
        approx_x = farey(x, approx_decimal)
        #print("PR[{}] = ({}/{}) = {}".format(V[x_i], approx_x[0], approx_x[1], x))
        #sorted_res_eval[res_eval[x_i]] = ["PR[{}]".format(V[x_i]), "({}/{})".format(approx_x[0], approx_x[1])]
        print("PR[{}] = ({}/{}) = {}".format(str(V[x_i]), approx_x[0], approx_x[1], x))
    """print("Sortierte Loesung: ")
    for key in sorted(sorted_res_eval.keys(), reverse=True):
        print("{} = {} = {}".format(sorted_res_eval[key][0], sorted_res_eval[key][1], key))"""
    return res_eval

more_data = True
edges = []
print("Abbruch mit allen Werten = esc")
d = float(eval(input("Daempfungsfaktor d: ")))
while more_data:
    print("Daten für Punkt:", len(edges))
    a = input("Von Knoten:")
    b = input("Zu Knoten:")
    if a == "esc" and b == "esc":
        more_data = False
        continue
    edges.append((a, b))
R = pagerank_algorithm(edges, d)
#pagerank_algorithm([("1", "3"), ("3", "6"), ("3", "4"), ("3", "2"), ("5", "2"), ("2", "1"), ("4", "2")], 4/5)