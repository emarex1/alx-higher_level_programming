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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """defines class rectangle"""
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, height):
        self.__width = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def width(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @width.setter
    def y(self, y):
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes"""
        self.id = id
        Base.__init__(self)
        self.id = id
