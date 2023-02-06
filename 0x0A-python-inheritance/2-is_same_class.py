#!/usr/bin/python3
""" Define is_same_class. """


def is_same_class(obj, a_class):
    """ Check if obj is isinstance of a_class. """
    if type(obj) == a_class:
        return True
    else:
        return False
