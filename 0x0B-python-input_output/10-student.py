class Student:
    """ instantiates first_name, last_name and age"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    """ Returns to_json dictionary. """
    def to_json(self, attr=None):
        """ retrieves a dictionary representation of Student attr(list)"""
        if attr != None:
            res = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return res
        else:
            return self.__dict__
