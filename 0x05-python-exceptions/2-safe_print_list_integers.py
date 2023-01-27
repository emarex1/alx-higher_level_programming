#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:

        try:
            print("{:d}".format(i[:x]))
        except Exception(ValueError, type):
            continue
        finally:
            print("")
            count += 1
            return count
