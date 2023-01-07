#!/usr/bin/python3
def islower(c):
    for char in c:
        if (ord(char) >= 90 and ord(char) <= 122):
            return True
        else:
            return False
