for i in range(10):
    print("Insert Value 1")
    int1 = int(input())
    print("Insert Operator")
    operator = input()
    print("Insert Value 2")
    int2 = int(input())
    if operator == "+":
        returner = int1 + int2
    elif operator == "-":
        returner = int1 - int2
    elif operator == "*":
        returner = int1 * int2
    elif operator == "/":
        returner = int1 / int2
    else:
        returner = "Operator not found"
    print(returner)