def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division par zéro impossible"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Modulo par zéro impossible"
    else:
        return "Opérateur non reconnu"
    
result1 = calcule(10, '+', 5)
result2 = calcule(20, '*', 3)
result3 = calcule(15, '/', 3)

print(result1)  
print(result2)  
print(result3)