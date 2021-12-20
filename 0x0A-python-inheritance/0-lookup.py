#!/usr/bin/python3
def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    ret = dir(obj)
    if hasattr(obj,'__bases__'):
        for base in obj.__bases__:
            ret += lookup(base)
    return ret
