#!/usr/bin/python3
"""Define BaseGeometry class. """


class BaseGeometry():
    """ Defines area which raises an Exception """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if self.value != int():
            raise TypeError("""{self.name} must be an integer""")
        elif self.value <= 0:
            raise ValueError("""{self.name}  must be greater than 0""")
