#!/usr/bin/python3
""" Add adjacent elements in two lists """


def list_division(my_list_1, my_list_2, list_length):
    new = []
    idx = 0
    while idx < list_length:
        try:
            new.append(my_list_1[idx] / my_list_2[idx])
        except (ValueError, TypeError):
            new.append(0)
            print('wrong type')
        except IndexError:
            new.append(0)
            print('out of range')
            break
        except ZeroDivisionError:
            new.append(0)
            print('division by 0')
        finally:
            idx += 1
            continue
    return new
