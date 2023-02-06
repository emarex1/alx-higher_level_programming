#!/usr/bin/python3
"""Define BaseGeometry class. """


class BaseGeometry():
    """ Defines area which raises an Exception """
    def area(self):
        raise Exception("area() is not implemented")
