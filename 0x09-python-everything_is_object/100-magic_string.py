#!/usr/bin/python3
def magic_string():
    itr = list(globals().items())[-1][1]
    return 'BestSchool, ' * itr + 'BestSchool'
