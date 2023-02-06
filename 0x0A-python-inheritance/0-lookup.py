#!/usr/bin/python3
""" Defines lookup function. """


def lookup(obj):
    """ Returns list of methods and attrinutes. """
    return list(dir(obj))
