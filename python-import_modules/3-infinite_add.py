#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    sum = 0
    for i in range(1, argc + 1):
        sum += int(sys.argv[i])
    print(sum)
