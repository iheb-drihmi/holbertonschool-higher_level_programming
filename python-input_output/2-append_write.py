#!/usr/bin/python3
""" append write """


def append_write(filename="", text=""):
    """
        appends a string to end of a text file (UTF8)
        Return:
            no of characters added
    """
    with open(filename, 'a+') as f:
        f.write(text)
    return len(text)
