#!/usr/bin/python3
def print_last_digit(num):
    if num < 0:
        last_dig = (-num % 10)
    elif num >= 0:
        last_dig = num % 10
    print("{:d}".format(last_dig), end="")
    return last_dig
