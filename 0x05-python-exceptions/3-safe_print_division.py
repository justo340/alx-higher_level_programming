#!/usr/bin/python3


def safe_print_division(a, b):
    # divides two integers and prints the result
    # catches divide by zero exception 
    try:
        res = a / b
        print("Inside result: {}".format(res))
    except:
        res = None
        print("Inside result: {}".format(res))
    finally:
        return res
        print("Inside result: {}".format(res))
