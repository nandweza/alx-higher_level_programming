#!/usr/bin/python3
"""Module 2-rectangle
Defines a class Rectangle
"""



class Rectangle:
    """Defines a class rectangle by private instance
    attributes width and height with public instance
    method area and perimeter.
    """

    def __init__(self, width=0, height=0):
        """Initialized Rectangle instance

        Args:
            width: width of the rectangle
            height: height of the rctangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width to a value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height to a value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
