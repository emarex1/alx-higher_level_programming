#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    summ = sum(map(int, sys.argv[1:]))
    print("{}".format(summ))
