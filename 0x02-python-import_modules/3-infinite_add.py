#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    add_tot = 0

    for k in range(len(sys.argv) - 1):
        add_tot += int(sys.argv[k + 1])
    print("{}".format(add_tot))
