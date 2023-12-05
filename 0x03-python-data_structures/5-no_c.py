#!/usr/bin/python3
def no_c(my_string):
    new_S = ""
    for x in my_string:
        if x.lower() not in ['c', 'C']:
            new_S += x
    return new_S
