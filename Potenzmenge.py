def powerset(fullset):
    # See: https://www.delftstack.com/de/howto/python/powerset-python/
    listsub = list(fullset)
    subsets = []
    for i in range(2**len(listsub)):
        subset = []
        for k in range(len(listsub)):            
            if i & 1<<k:
                subset.append(listsub[k])
        subsets.append(sorted(subset))        
    return subsets
print("Abbruch mit allen Werten = esc")
print("Menge:")
more_data = True
A = []
while more_data:
    a = input("a{}:".format(len(A)))
    if a == "esc":
        more_data = False
        continue
    A.append(a)
subsets = powerset(set(A))
print(len(subsets), subsets)