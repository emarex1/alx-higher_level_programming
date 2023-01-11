#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for keys, values in sorted(my_dict.items()):
        print(keys, values, sep=": ")
