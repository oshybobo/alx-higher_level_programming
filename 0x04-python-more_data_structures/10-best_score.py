#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    h_score = 0
    for i, j in a_dictionary.items():
        if j > h_score:
            h_score = j
    for i, j in a_dictionary.items():
        if j == h_score:
            return i
