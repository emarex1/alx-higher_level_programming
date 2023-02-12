#!/usr/bin/python3
""" defines save_to_json_file functions. """
import json


def save_to_json_file(my_obj, filename):
    """ Write an object to a text file using JSON representation. """
    with open(filename, 'w') as files:
        json.dump(my_obj, files)
