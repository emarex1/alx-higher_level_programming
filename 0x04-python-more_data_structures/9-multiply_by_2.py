#!/usr/bin/python3
def multiply_by_2(a_dictionary):
        for keys, values in sorted(a_dictionary.items()):
            print(keys, values * 2, sep=": ")
        return multiply_by_2
