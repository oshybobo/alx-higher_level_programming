#!/usr/bin/python
def print_sorted_dictionary(a_dictionary):
    dict_list = sorted(a_dictionary)
    for j in dict_list:
        print("{}: {}".format(j, a_dictionary[j]))
