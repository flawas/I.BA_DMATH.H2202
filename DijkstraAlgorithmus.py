# Author Joel Kessler 
def remove_from_dict(dict_data, l2):
    for e in l2:
        dict_data.pop(e, None)
        
def remove_from_list(l1, l2):
    lr = list(l1)
    for e in l2:
        if e in lr:
            lr.remove(e)  
    return lr

def dijkstra(edges_and_weight, start_node):
    nodes = set()
    for edge_and_weight in edges_and_weight:
        nodes.add(edge_and_weight[0])
        nodes.add(edge_and_weight[1])
    nodes = sorted(list(nodes))
    if not start_node in nodes:
        print("Ungueltiger start Punk")
        return
    S = []
    # Key: Node, Value: Laenge, Vorgaenger
    columns = [dict.fromkeys(nodes, (None, None))]
    columns[0][start_node] = (0, start_node)
    while len(S) < len(nodes):
        previous_column = columns[-1]
        shortest_l_p = None
        shortest_key = None
        # Finde kleinsten in vorgaeniger liste
        for key in remove_from_list(nodes, S):
            l, p = previous_column[key]
            if l == None:
                continue
            if shortest_l_p == None or l < shortest_l_p[0]:  
                shortest_l_p = (l, p)
                shortest_key = key    
        # Knoten an S hinzufuegen
        S.append(shortest_key)        
        print("Shortest: ", shortest_key, shortest_l_p)
        # Finde verbundene knoten punkte
        neighbours = [ew for ew in edges_and_weight if ew[0] == shortest_key or ew[1] == shortest_key]
        # Entferne benachbarte welche y E (nodes - S)
        neighbours_cleaned = []
        for neighbour in neighbours:
            detected_node = neighbour[0]
            if detected_node == shortest_key:
                detected_node = neighbour[1]
            if detected_node in remove_from_list(nodes, S):
                neighbours_cleaned.append(neighbour)
        print("Neigbours:", neighbours_cleaned)
        
        # Kopiere vorgaenige kolonne
        new_column = previous_column.copy()
        # Entferne abgeschlossene knoten
        remove_from_dict(new_column, S)
        columns.append(new_column)
        print("neighbours_cleaned: " ,neighbours_cleaned)
        # Fuer jeden nachbar
        for v, w, weight in neighbours_cleaned:
            y = v
            s = w
            if v == shortest_key:
                y = w
                s = v 
            y_column_data = previous_column[y]
            if y_column_data[0] == None or y_column_data[0] > shortest_l_p[0] + weight:
                # Setzte kuerzeren weg
                new_column[y] = (shortest_l_p[0] + weight, shortest_key)
        #print("Previous: ", previous_column)
        #print("New: ", new_column)
        print("S:", S)
        print("------------------")
    return columns, S

# Author Flavio Waser
more_data = True
print("Abbruch mit allen Werten = 0")
start_point = input("Start knoten fuer Algorithmus:")
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
cols, diS = dijkstra(e_and_w, start_point)
print("Knoten: (Distanz, Vorgaenger)")
for col in cols:
    print(col)
print("S:", diS)