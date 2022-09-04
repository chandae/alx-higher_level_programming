#!/usr/bin/python3

def read_file(filename=""):
    """ Reads text file (utg-8) and outputs contents to stdout """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
