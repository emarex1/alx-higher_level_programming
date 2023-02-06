#!/usr/bin/python3
"""Define BaseGeometry class. """


class BaseGeometry():
    """ Defines area which raises an Exception """
    def area(self):
        raise Exception("area() is not implemented")
    """
        Public instance integer_validator that
        validates value
    """

    def integer_validator(self, name, value):

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{}  must be greater than 0".format(name))
