#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """defines class instance"""

    def __init__(self, size=0):
        """self method
        """
        try:
            self.__size = size

        except TypeError:
            print("TypeError")
        except ValueError:
            print("size must be >= 0")
