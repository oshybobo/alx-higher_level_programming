#!/usr/bin/python3
for k in range(0, 9):
    for j in range(k + 1, 10):
        if k * 10 + j < 89:
            print("{:d}{:d}".format(k, j), end=", ")
print("{:d}".format(89))
