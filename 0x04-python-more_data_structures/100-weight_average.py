#!/usr/bin/python3
""" Returns the weighted average of all integers tuple """


def weight_average(my_list=[]):
    """ Return weighted average of integers in my_list """
    if not my_list:
        return 0
    else:
        average = sum(list(map(lambda t: t[0] * t[1], my_list)))
        total_w = sum(w[1] for w in my_list)
        return average/total_w
