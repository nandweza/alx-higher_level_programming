#!/usr/bin/python3
"""Defines a class Square."""



class Square:
    """Represents a square.
    private instance attribute: size.
    Instatiation with optional size.
    """

    def __init__(self, size=0):
        """Initialize the data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
