#!/usr/bin/python3
import sys

def main():

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(count))
        for i in range(1, count + 1):
            print("{}: {}".format(i, sys.argv[i]))

            if __name__ == "__main__":
                main()
