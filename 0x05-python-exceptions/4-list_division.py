#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        list_length = [m/n for m, n in zip(my_list_1, my_list_2)]
    except (TypeError, ValueError):
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    finally:
        print("{}".format(list_length), end="")
    if len(my_list_1) != len(my_list_2):
        print("out of range")
