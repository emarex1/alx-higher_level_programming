#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import sub, add, div, mul
    a = 10
    b = 5
    print("{:d} + {:d} = {:d} ".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d} ".format(a, b, sub(a, b)))
    print("{:d} / {:d} = {:d} ".format(a, b, div(a, b)))
    print("{:d} * {:d} = {:d} ".format(a, b, mul(a, b)))
