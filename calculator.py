def main():
    print("Hello World")
    print(calc())

def verifyString(input):
    symbol = False
    for i in range(len(input)):
        c = input[i]
        if(c == '+' or c == '-' or c == '*'):
            if(symbol == True):
                return "Error: Duplicate operation: " + input[i-1] + c
            else:
                symbol = True
        elif(ord(c) >= ord('0') and ord(c) <= ord('9')):
            symbol = False
        else:
            return "Error: Unknown/Disallowed character: " + c
    if(symbol == False):
        return input
    return "Error: Ended on an operator: " + c

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
    inputString = verifyString(inputString)
    if "Error" in inputString: return inputString
    values = []
    operators = []
    i = 0
    while i < len(inputString):
        if inputString[i].isdigit():
            i, inputString, values = appendDigits(i, inputString, values)
        else:
            i, inputString, values, operators = evaluateHigherPrecFromStack(i, inputString, values, operators)
        i += 1
    values = evaluateRemainingStack(values, operators)
    return values[-1]

def calc():
    user_input = input()
    return evaluate(user_input)
    

if __name__ == '__main__':
    main()
