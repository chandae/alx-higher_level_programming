#!/usr/bin/python3
""" Finds peak element in a given array """


def find_peak(array):
    """ find the peak element in my_list """
    n =  len(array)
    if n == 0:
        return
    mid = n // 2

    check_1 = (mid == 0 or array[mid - 1] <= array[mid])
    check_2 = (mid == n - 1 or array[mid + 1] < array[mid])
    if check_1 and check_2:
        return array[mid]
    elif (mid > 0 and array[mid - 1] > array[mid]):
        return find_peak(array[:mid])
    else:
        return find_peak(array[mid:])
