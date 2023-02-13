#!/usr/bin/python3
""" class bass"""


class Base:
    " intantiates base class"
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes id """
        self.id = id
        if self.id is not None:
            self.id = self.id
        else:
            self.__nb_objects += 1
            self.__nb_objects = self.id
