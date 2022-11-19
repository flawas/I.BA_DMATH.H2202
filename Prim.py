# Author Joel Kessler 2
def remove_from_list(l1, l2):
    lr = list(l1)
    for e in l2:
        if e in lr:
            lr.remove(e)  
    return lr

def prim_algorithm(edges_and_weights, start_node):
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
    if not start_node in V:
        print("Ungueltiger start Punkt")
        return
    S = [start_node]
    V.remove(start_node)
    T = []
    w_T = 0
    num_nodes = len(V) + 1
    while len(S) < num_nodes:
        # Gewicht, x E S, y E (V - S)
        selected_edge = None
        # Kante mit minimalem gewicht finden
        for key in edges_sorted_indecies:
            for i in range(0, len(edges_grouped[key])):
                v, w = edges_grouped[key][i]
                if (v in S and w in V) or (w in S and v in V):
                    x = v
                    y = w
                    if y in S:
                        x = w
                        y = v
                    selected_edge = (key, x, y)
                    edges_grouped[key].remove(edges_grouped[key][i]) 
                    break
            if selected_edge != None:
                break
        # Menge S hinzuefuegen
        S.append(selected_edge[2])
        V.remove(selected_edge[2])
        T.append((selected_edge[1], selected_edge[2]))
        w_T += selected_edge[0]
        print("S added: ", selected_edge[2])
        print("T added: ", (selected_edge[1], selected_edge[2]))
        print("w(T) added: ", selected_edge[0])
    return S, T, w_T

more_data = True
print("Abbruch mit allen Werten = 0")
start_point = input("Start knoten fuer PRIM Algorithmus:")
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

S, T, w_T = prim_algorithm(e_and_w, start_point)
print("------------")
print("S: ", S)
print("T: ", T)
print("w(T): ", w_T)