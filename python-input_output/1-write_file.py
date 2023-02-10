#!/usr/bin/python3
""" write file """


def write_file(filename="", text=""):
    """
        writes a string to a text file (UTF8)
        Return:
            no of characters written
    """
    with open(filename, 'w+') as f:
        f.write(text)
    return len(text)
