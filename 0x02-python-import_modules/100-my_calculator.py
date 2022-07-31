#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    args = sys.argv

    if len(args) == 4:
        a = int(args[1])
        b = int(args[3])
        func = {'+': add(a, b), '-': sub(a, b), '*': mul(a, b), '/': div(a, b)}
        operator = args[2]
        result = func.get(operator, False)
        if result:
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    elif len(args) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
