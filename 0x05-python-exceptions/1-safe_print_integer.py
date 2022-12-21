#!/usr/bin/python3
def safe_print_integer(value):
    """Prints a list of integer"""
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
