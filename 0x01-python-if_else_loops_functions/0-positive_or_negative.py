#!/usr/bin/python3
import random
number = random.randint(-10, 10)
print("{} ".format(number), end="")
if number > 0:
    print("is positive")
if number == 0:
    print("is zero")
if number < 0:
    print("is negetive")
