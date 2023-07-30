#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = sum(list(map(int, sys.argv[1:])))
    print("{:d}".format(total))
