#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list)
    uniq_add = [x for x in my_list]
    return sum(uniq_add)
