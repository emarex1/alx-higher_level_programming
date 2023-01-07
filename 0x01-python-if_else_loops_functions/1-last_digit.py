#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = int(repr(number)[-1])
if number < 0:
    a = -1 * (a)
if a > 5:
    print(f"Last digit of {number} is {a} and is greater than 5")
if a == 0:
    print(f"Last digit of {number} is {a} and is zero")
if (a < 6) and (a != 0):
    print(f"Last digit of {number} is {a} and is less than 6 and not 0")
