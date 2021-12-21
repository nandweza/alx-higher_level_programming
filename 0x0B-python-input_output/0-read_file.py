#!/usr/bin/python3
"""Module 0-read_file.py
creates a function that reads a text file.
"""


def read_file(filename=""):
    """a function that reads a text file(UTF8) and prints it to stdout."""
    with open('my_file_0.txt', encoding='utf-8') as myfile:
        print(myfile.read())
