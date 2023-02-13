#!/usr/bin/python3
""" define append after function."""


def append_after(filename="", search_string="", new_string=""):
    """ open file"""
    with open(filename) as f:
        for i in f:
            if i == search_string:
                new_string.append(i)

    with open(filename) as w:
        w.write(new_string)
