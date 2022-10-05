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
    

if __name__ == '__main__':
    main()
