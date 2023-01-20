#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    Sum = 0
    num = sys.argv
    if len(num) > 1:
        for i in range(1, len(num)):
            Sum += int(num[i])
    print('{:d}'.format(Sum))
