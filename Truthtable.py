#Author: https://medium.com/street-science/how-to-implement-a-truth-table-generator-in-python-40185e196a5b

def isWellFormed(P):
    bracketLevel = 0
    for c in P:
        if c == "(":
            bracketLevel += 1
        if c == ")":
            if bracketLevel == 0:
                return False
            bracketLevel -= 1
    return bracketLevel == 0

def parseNegation(P, truthValues):
    return not parseProposition(P, truthValues)

def parseConjunction(P, Q, truthValues):
    return parseProposition(P, truthValues) and parseProposition(Q, truthValues)

def parseDisjunction(P, Q, truthValues):
    return parseProposition(P, truthValues) or parseProposition(Q, truthValues)

def parseConditional(P, Q, truthValues):
    return (not parseProposition(P, truthValues)) or parseProposition(Q, truthValues)

def parseBiconditional(P, Q, truthValues):
    return parseProposition(P, truthValues) == parseProposition(Q, truthValues)

def parseProposition(P, truthValues):
    P = P.replace(" ", "")

    if not isWellFormed(P):
        return "Error"

    while P[0] == "(" and P[-1] == ")" and isWellFormed(P[1:len(P) - 1]):
        P = P[1:len(P) - 1]

    if len(P) == 1:
        return truthValues[P]

    bracketLevel = 0
    for i in reversed(range(len(P))):
        if P[i] == "(":
            bracketLevel += 1
        if P[i] == ")":
            bracketLevel -= 1
        if P[i] == "i" and bracketLevel == 0:
            return parseConditional(P[0:i], P[i + 1:], truthValues)
        if P[i] == "b" and bracketLevel == 0:
            return parseBiconditional(P[0:i], P[i + 1:], truthValues)

    bracketLevel = 0
    for i in reversed(range(len(P))):
        if P[i] == "(":
            bracketLevel += 1
        if P[i] == ")":
            bracketLevel -= 1
        if P[i] == "o" and bracketLevel == 0:
            return parseDisjunction(P[0:i], P[i + 1:], truthValues)

    bracketLevel = 0
    for i in reversed(range(len(P))):
        if P[i] == "(":
            bracketLevel += 1
        if P[i] == ")":
            bracketLevel -= 1
        if P[i] == "a" and bracketLevel == 0:
            return parseConjunction(P[0:i], P[i + 1:], truthValues)

    bracketLevel = 0
    for i in reversed(range(len(P))):
        if P[i] == "(":
            bracketLevel += 1
        if P[i] == ")":
            bracketLevel -= 1
        if P[i] == "-" and bracketLevel == 0:
            return parseNegation(P[i + 1:], truthValues)

def writeTruthTable(P):
    truthValues = {}
    for i in range(len(P)):
        if P[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            truthValues[P[i]] = True

    for statement in list(truthValues.keys()):
        print(statement, end=" | ")
    print(P)

    for truthValue in list(truthValues.values()):
        print("T" if truthValue else "F", end=" | ")
    print("T" if parseProposition(P, truthValues) else "F")

    j = len(truthValues.values()) - 1
    while True in truthValues.values():
        variable = list(truthValues.keys())[j]
        truthValues[variable] = not truthValues[variable]

        if not truthValues[variable]:
            for truthValue in list(truthValues.values()):
                print("T" if truthValue else "F", end=" | ")
            print("T" if parseProposition(P, truthValues) else "F")
            j = len(truthValues.values()) - 1
        else:
            j -= 1

print("Example:P V (Q → (R ∧ T))")
print("Operanden: o == OR, a == AND, - == NEGATION")
print("Operanden: i == IMPLIKATION, b == BIKONDITIONAL")
print("Aufgabe eingeben")
table = input()
writeTruthTable(table)