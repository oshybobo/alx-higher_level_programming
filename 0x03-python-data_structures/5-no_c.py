#!/usr/bin/python3
def no_c(my_string):
    n_string = ""
    for elm in my_string:
        if elm != 'c' and elm != 'C':
            n_string += elm
    return n_string
