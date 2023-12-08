#!/ust/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorting = sorted(a_dictionary.keys())
    for key in sorting:
        print("{:s}: {}".format(key, a_dictionary[key]))
