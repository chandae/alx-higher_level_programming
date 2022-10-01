#!/usr/bin/python3
""" Finds peak element in a given array """


def find_peak(array):
    """ find the peak element in my_list """
    n = len(array)
    if n == 0:
        return

    def findPeakUtil(arr, lower, upper, n):
        mid = lower + (upper - lower) / 2
        mid = int(mid)

        check_1 = (mid == 0 or arr[mid - 1] <= arr[mid])
        check_2 = (mid == n - 1 or arr[mid + 1] <= arr[mid])
        if check_1 and check_2:
            return arr[mid]
        elif (mid > 0 and arr[mid + 1] > arr[mid]):
            return findPeakUtil(arr, (mid + 1), upper, n)
        else:
            return findPeakUtil(arr, lower, (mid - 1), n)

    return findPeakUtil(array, 0, n - 1, n)
