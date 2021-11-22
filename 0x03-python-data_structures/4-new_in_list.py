#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific 
       position without modifying the 
       original list (like in C)"""
    copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
