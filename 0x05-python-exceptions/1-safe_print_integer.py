#!/usr/bin/python3
def safe_print_integer(value):
    """function that prints an integer with "{:d}".format()."""
    try:
        print("{:d}".format(i), end="")
    except:
        return False
    else:
        return True
