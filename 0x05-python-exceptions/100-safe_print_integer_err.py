#!/usr/bin/python3
if __name__ == "__main__":
    import os


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        os.write(2, b"")
        return False
