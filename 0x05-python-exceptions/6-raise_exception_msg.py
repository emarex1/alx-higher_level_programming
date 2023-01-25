#!/usr/bin/python3
def raise_exception_msg(message=""):
    raise NameError
    try:
        raise_exception_msg(message="C is fun")
    except NameError:
        print(message)
