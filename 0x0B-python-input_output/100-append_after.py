#!/usr/bin/python3
""" define append after function."""


def append_after(filename="", search_string="", new_string=""):
    """ open file"""
    with open(filename, 'a') as f:
        for i in f:
            if i == search_string:
                new_string.append(i)
        return new_string
