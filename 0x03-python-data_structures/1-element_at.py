#!/usr/bin/python3
def element_at(my_list, idx):
    # If idx is negative, the function should return None
    # If idx is out of range (> of number of element in my_list),
    # the function should return None
    length=len(my_list)
    if idx < 0 or idx >= length:
        return None
    return my_list[idx]
