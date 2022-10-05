def main():
    print("Hello World")
    print(sub_calc(1, 2, "*"))

def precedence(operators):
    if operators == '+' or operators == '-': return 1
    if operators == '*' or operators == '/': return 2
    return 0
    
def sub_calc(a, b, operators):
    if operators == "+": return a + b
    if operators == "-": return a - b
    if operators == "*": return a * b
    

if __name__ == '__main__':
    main()
