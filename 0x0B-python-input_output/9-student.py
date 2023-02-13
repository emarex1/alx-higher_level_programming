#!/usr/bin/python3
""" Defines a class Student. """


class Student:
    """ instantiates first_name, last_name and age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """ Returns to_json dictionary. """
    def to_json(self):
        return self.__dict__
