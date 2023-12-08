#!/usr/bin/python3

def uniq_ad(my_list=[]):
    unique_set = set(my_list)
    add_result = sum(unique_set)
    return add_result

    # list comprehension way
    #  return sum(set(my_list))