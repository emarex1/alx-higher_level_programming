#!/usr/bin/python3
"""Defines a load_from_json_file function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as files:
        return json.load(files)
