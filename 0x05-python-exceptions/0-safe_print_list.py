#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ function that prints x elements of a list."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            break
        else:
            count += 1
        print()
        return count
