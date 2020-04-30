#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    long = len(sys.argv)
    if long - 1 == 0:
        print("{} {}".format(long - 1, "arguments."))
    if long - 1 == 1:
        print("{} {}".format(long - 1, "argument:"))
    if long - 1 > 1:
        print("{} {}".format(long - 1, "arguments:"))
    for a in range(long):
        if a == 0:
            continue
        print("{}: {}".format(a, sys.argv[a]))
