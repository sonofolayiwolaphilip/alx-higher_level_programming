#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list=[]
    for y in my_list:
        if y == search:
            new_list.append(replace)
        else:
            new_list.append(y)
    return new_list