#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    arge = arg[1:]
    arge = sum([int(it) for it in arge])
    print(arge)