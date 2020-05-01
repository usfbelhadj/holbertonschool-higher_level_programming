#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg = sys.argv
    if len(sys.argv) == 1:
        exit(1)
    arge = arg[1:]
    print(arge)
    num1 = int(arge[0])
    num2 = int(arge[2])
    if arge[1] == '+':
        print("{} + {} = {}".format(num1, num2, add(num1, num2)), end="\n")
        exit(0)
    if arge[1] == '-':
        print("{} - {} = {}".format(num1, num2, sub(num1, num2)), end="\n")
        exit(0)
    if arge[1] == '*':
        print("{} * {} = {}".format(num1, num2, mul(num1, num2)), end="\n")
        exit(0)
    if arge[1] == '/':
        print("{} / {} = {}".format(num1, num2, div(num1, num2)), end="\n")
        exit(0)