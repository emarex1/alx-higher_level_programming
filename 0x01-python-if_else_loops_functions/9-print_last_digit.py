#!/usr/bin/python3
def print_last_digit(number):
    last_digits = abs(number) % 10
    print(last_digits, end="")
    return last_digits
