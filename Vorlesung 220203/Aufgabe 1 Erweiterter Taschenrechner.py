import math


def rechnen(operator, int1, int2):
    global returner
    if operator == "^":
        returner = pow(int1, int2)
    if operator == "+":
        returner = int1 + int2
    elif operator == "-":
        returner = int1 - int2
    elif operator == "*":
        returner = int1 * int2
    elif operator == "/":
        returner = int1 / int2
    else:
        pass
    return returner


def getindexstartcalc(operatorindex, tokens):
    for i in range(1, operatorindex + 1):
        #      print(ord(tokens[operatorindex - i]) - 48)
        if type(tokens[operatorindex - 1]) != float:
            if i == operatorindex:
                return 0
            numberchar = ord(tokens[operatorindex - i])
            if (numberchar <= 47) | (numberchar > 58):
                return operatorindex - i + 1
        elif (i == operatorindex):
            return operatorindex - i


def getindexendcalc(operatorindex, tokens):
    length = len(tokens)
    for i in range(1, length - operatorindex + 1):
        if i == length - operatorindex:
            return operatorindex + i - 1
        if type(tokens[operatorindex + i]) != float:
            numberchar = ord(tokens[operatorindex + i])
            if (numberchar <= 47) | (numberchar > 58) | (i == length - operatorindex):
                return operatorindex + i - 1
        elif (i == operatorindex + i):
            return operatorindex + i


def analyse(tokens):
    if "^" in tokens:
        highestmathgrade = 3
        operatorindex = tokens.index("^")
        indexstartcalc = getindexstartcalc(operatorindex, tokens)
        indexendcalc = getindexendcalc(operatorindex, tokens)
        return [highestmathgrade, indexstartcalc, operatorindex, indexendcalc]
    elif "/" in tokens:
        highestmathgrade = 2
        operatorindex = tokens.index("/")
        indexstartcalc = getindexstartcalc(operatorindex, tokens)
        indexendcalc = getindexendcalc(operatorindex, tokens)
        return [highestmathgrade, indexstartcalc, operatorindex, indexendcalc]
    elif "*" in tokens:
        highestmathgrade = 2
        operatorindex = tokens.index("*")
        indexstartcalc = getindexstartcalc(operatorindex, tokens)
        indexendcalc = getindexendcalc(operatorindex, tokens)
        return [highestmathgrade, indexstartcalc, operatorindex, indexendcalc]
    elif "+" in tokens:
        highestmathgrade = 1
        operatorindex = tokens.index("+")
        indexstartcalc = getindexstartcalc(operatorindex, tokens)
        indexendcalc = getindexendcalc(operatorindex, tokens)
        return [highestmathgrade, indexstartcalc, operatorindex, indexendcalc]
    elif "-" in tokens:
        highestmathgrade = 1
        operatorindex = tokens.index("-")
        indexstartcalc = getindexstartcalc(operatorindex, tokens)
        indexendcalc = getindexendcalc(operatorindex, tokens)
        return [highestmathgrade, indexstartcalc, operatorindex, indexendcalc]
    else:
        return [0, 0, 0, 0]


def berechneint(param):
    sum = 0
    for i in range(0, len(param)):
        if type(param[i]) != float:
            teilprodukt = (ord(param[i]) - 48)
        else:
            teilprodukt = param[i]
        teilprodukthoch10 = teilprodukt * (math.pow(10, len(param) - (i + 1)))
        sum += teilprodukthoch10
    return sum


def complexcalc(tokens):
    i = len(tokens)
    anweisungen = analyse(tokens)
    if anweisungen[0] == 0:
        return tokens[0]
    ergebnis = rechnen(tokens[anweisungen[2]], berechneint(tokens[anweisungen[1]:anweisungen[2]]),
                       berechneint(tokens[anweisungen[2] + 1:anweisungen[3] + 1]))
    neutokens = []
    if anweisungen[1] != 0:
        neutokens = tokens[0:anweisungen[1]]
    neutokens = neutokens + [ergebnis]
    if anweisungen[3] != len(tokens) - 1:
        neutokens = neutokens + tokens[anweisungen[3] + 1:len(tokens)]
    print(neutokens)
    return complexcalc(neutokens)


while True:
    print("Insert eingabe")
    eingabe = input()
    tokens = list(eingabe)
    print(tokens)
    returner = complexcalc(tokens)
    print("Ergebnis: ", returner)
