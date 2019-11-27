def Operations(var1, opr, var2):
    if opr == "AND":
        if int(var1 + var2) % 2 == 0:
            return True
        else:
            return False
    if opr == "OR":
        if int(var1 + var2) > 0:
            return True
        else:
            return False
    if opr == "XOR":
        if int(var1 + var2) == 1:
            return True
        else:
            return False
    if opr == "NAND":
        if int(var1 + var2) % 2 == 0:
            return False
        else:
            return True
    if opr == "NOR":
        if int(var1 + var2) > 0:
            return False
        else:
            return True


num1, operation, num2 = input("Enter your logical operation:").split()
operation = operation.upper()
print(Operations(num1, operation, num2))

