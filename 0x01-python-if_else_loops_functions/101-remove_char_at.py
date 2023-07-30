#!/usr/bin/python3
def remove_char_at(str, n):
    if n < len(str) and n >= 0:
        c = str[n]
        str = str.replace(c, '')
        return ''.join(str)
    else:
        return str
