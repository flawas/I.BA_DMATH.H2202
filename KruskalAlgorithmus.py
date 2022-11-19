# Author Joel Kessler
def remove_from_list(l1, l2):
    lr = list(l1)
    for e in l2:
        if e in lr:
            lr.remove(e)  
    return lr

def kruskal_algorithm(edges_and_weights):
    V = set()
    edges_grouped = dict()
    for edge_and_weight in edges_and_weights:
        V.add(edge_and_weight[0])
        V.add(edge_and_weight[1])
        
        if edge_and_weight[2] not in edges_grouped:
            edges_grouped[edge_and_weight[2]] = [(edge_and_weight[0], edge_and_weight[1]), ]
        else:
            edges_grouped[edge_and_weight[2]].append((edge_and_weight[0], edge_and_weight[1]))
    edges_sorted_indecies = sorted(edges_grouped)
    V = sorted(list(V))
    R = [[node] for node in V]
    T = []
    w_T = 0
    # Wiederhole bis alle Knoten besucht
    while V != sorted(list(sum(T, ()))):
        # Gewicht, x E R[a], y E R[b]
        selected_edge = None
        # Kante mit minimalem gewicht finden
        for key in edges_sorted_indecies:
            for i in range(0, len(edges_grouped[key])):
                v, w = edges_grouped[key][i]
                # Finde klassen von v und w
                v_class = None
                w_class = None
                for R_class in R:
                    if v in R_class:
                        v_class = R_class
                    elif w in R_class:
                        w_class = R_class   
                if w_class == None or v_class == None:
                    continue
                if v_class != w_class:
                    # Wenn klasse gefunden, fuege alle elemente aus klasse w zu klasse von v hinzu
                    for w_el_i in range(0, len(w_class)):
                        v_class.append(w_class[0])
                        w_class.remove(w_class[0])
                    # Entferne leere klasse
                    if len(w_class) == 0:
                        R.remove(w_class)
                    selected_edge = (key, v, w)
                    # Loesche selektierte kante
                    edges_grouped[key].remove(edges_grouped[key][i])    
                    break
            if selected_edge != None:
                break
        if selected_edge == None:
            return R, T, w_T
        w_T += selected_edge[0]
        T.append((selected_edge[1], selected_edge[2]))
        print("T added: ", (selected_edge[1], selected_edge[2]))
        print("w(T) added: ", selected_edge[0])
        print("R classes: ", R)
        print("------------")

more_data = True
print("Abbruch mit allen Werten = 0")
e_and_w = []
while more_data:
    print("Daten für Punkt:", len(e_and_w))
    a = input("Anfangsknoten:")
    b = input("Endknoten:")
    weight = int(input("Kantengewicht:"))
    if a == "0" and b == "0" and weight == 0:
        more_data = False
        continue
    e_and_w.append((a, b, weight))
R, T, w_T = kruskal_algorithm(e_and_w)
print("------------")
print("R: ", R)
print("T: ", T)
print("w(T): ", w_T)