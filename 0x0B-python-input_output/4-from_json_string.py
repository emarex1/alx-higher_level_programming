#!/usr/bin/python3
""" defines from_json_string functions. """
import json


def from_json_string(my_str):
    """ returns json object. """
    return json.loads(my_str)
