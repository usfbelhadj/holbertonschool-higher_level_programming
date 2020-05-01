#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    arg = sys.argv
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    arge = arg[1:]
    num1 = int(arge[0])
    num2 = int(arge[2])
    if arge[1] == '+':
        print("{} + {} = {}".format(num1, num2, add(num1, num2)), end="\n")
    elif arge[1] == '-':
        print("{} - {} = {}".format(num1, num2, sub(num1, num2)), end="\n")
    elif arge[1] == '*':
        print("{} * {} = {}".format(num1, num2, mul(num1, num2)), end="\n")
    elif arge[1] == '/':
        print("{} / {} = {}".format(num1, num2, div(num1, num2)), end="\n")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
