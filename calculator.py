def main():
    print("Hello World")
    print(sub_calc(1, 2, "*"))

def verifyString(input):
    symbol = False
    for c in input:
        if(c == '+' or c == '-' or c == '*'):
            if(symbol == True):
                return False
            else:
                symbol = True
        elif(ord(c) >= ord('0') and ord(c) <= ord('9')):
            symbol = False
        else:
            return False
    if(symbol == False):
        return True
    return False

def precedence(operators):
    if operators == '+' or operators == '-': return 1
    if operators == '*' or operators == '/': return 2
    return 0
    
def sub_calc(a, b, operators):
    if operators == "+": return a + b
    if operators == "-": return a - b
    if operators == "*": return a * b

def appendDigits(i, inputString, values):
    value = 0
    while (i < len(inputString) and inputString[i].isdigit()):
        value = (value * 10) + int(inputString[i])
        i += 1
    values.append(value)
    i-=1
    return i, inputString, values

def evaluateHigherPrecFromStack(i, inputString, values, operators):
    while (len(operators) != 0 and precedence(operators[-1]) >= precedence(inputString[i])): 
        value2 = values.pop()
        value1 = values.pop()
        operator = operators.pop()
        values.append(sub_calc(value1, value2, operator))
    operators.append(inputString[i])
    return i, inputString, values, operators

def evaluateRemainingStack(values, operators):
    while len(operators) != 0:
        value2 = values.pop()
        value1 = values.pop()
        operator = operators.pop()   
        values.append(sub_calc(value1, value2, operator))
    return values

def evaluate(inputString):
    if(verifyString(inputString) == False): return "String is malformed"
    values = []
    operators = []
    i = 0
    while i < len(inputString) - 1:
        if inputString[i].isdigit():
            i, inputString, values = appendDigits(i, inputString, values)
        else:
            i, inputString, values, operators = evaluateHigherPrecFromStack(i, inputString, values, operators)
        i += 1
    values = evaluateRemainingStack(values, operators)
    return values[-1]
    

if __name__ == '__main__':
    main()
