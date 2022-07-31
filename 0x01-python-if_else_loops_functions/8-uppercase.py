#!/usr/bin/python3
def uppercase(str):
    up = ''
    for c in str:
        if ord(c) >= 65 and ord(c) <= 90 or not c.isalpha():
            up += c
        else:
            up += chr(ord(c) - 32)
    print("{:s}".format(up))
