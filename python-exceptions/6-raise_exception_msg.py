#!/usr/bin/python3
def raise_exception_msg(msg=""):
    try:
        raise NameError(msg)
    except NameError:
        raise
