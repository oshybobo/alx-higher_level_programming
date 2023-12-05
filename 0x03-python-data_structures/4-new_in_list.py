#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mylist_c = my_list.copy()
    if idx < 0:
        return mylist_c
    elif idx >= len(mylist_c):
        return mylist_c
    else:
        mylist_c[idx] = element
        return mylist_c
