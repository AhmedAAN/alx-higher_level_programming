#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for i in range(sys.argv - 1):
        sum += int(sys.argv[i + 1])
    if len(sys.argv) != 0:
        print("{}".format(sum))
