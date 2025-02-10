art = '''
 _____________________
|  _________________  |
| |   CALCULATOR    | |  
| |_________________| |  
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | * | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

'''


print(art)


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        return "Error"
    else:
        return n1 / n2
    
operation = { '+': add, '-': subtract, '*': multiply, '/': divide}

# perform the operation 
# print(operation['*'](4,8))

def calculator():
    print(art)
    should_accumulate = True

    num1 = float(input("What is the first number: "))

    while should_accumulate:
        
        for symbol in operation:
            print(symbol)

        operation_symbol = input("Pick operation symbol: ")

        num2 = float(input("What is the next number: "))

        ans = operation[operation_symbol](num1,num2)

        # print(operation['+'](4,8))  
        # Output: 12.0

        print(f'{num1} {operation_symbol} {num2} = {ans}')

        choice = input(f"Type 'y' to continue with {ans}, or type'n'to start new calculation: ")

        if choice == 'y':
            num1 = ans
        else:
            should_accumulate = False
            print("\n"* 20)
            calculator()

calculator()
