#!/usr/bin/python3
""" Add adjacent elements in two lists """


def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            new.append(my_list_1[i] / my_list_2[i])
        except (ValueError, TypeError):
            new.append(0)
            print('wrong type')
        except IndexError:
            new.append(0)
            print('out of range')
        except ZeroDivisionError:
            new.append(0)
            print('division by 0')
    return new
