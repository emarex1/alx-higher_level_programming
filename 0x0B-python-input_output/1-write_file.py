#!/usr/nin/python3
""" Write_file function that writes to text"""


def write_file(filename="", text=""):
    """Opens file for writing"""

    with open(filename, mode='w', encoding='utf-8') as files:
        return files.write(text)
