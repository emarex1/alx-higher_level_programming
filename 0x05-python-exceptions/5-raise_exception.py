#!/usr/bin/python3
def raise_exception():
    raise TypeError
    try:
        raise_exception()
    except TypeError:
        print("Exception raised")
