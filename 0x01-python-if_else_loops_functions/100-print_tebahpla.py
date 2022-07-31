#!/usr/bin/python3
eval("""print(''.join(["{:s}".format(chr(i).upper())
if i % 2 != 0 else chr(i)
for i in range(97, 123)][::-1]), end="")""")
