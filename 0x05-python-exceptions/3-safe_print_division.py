#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides two integers and prints the result
    Catches divide by zero exception
    """
    try:
        res = a / b
    except:
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
