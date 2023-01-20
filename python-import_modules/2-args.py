#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg = len(sys.argv)
    if arg == 1:
        print('0 arguments.')
    elif arg == 2:
        print('1 argument:')
        print('1: {}'.format(sys.argv[1]))
    else:
        print('{} arguments:'.format(arg - 1))
        for arg in range(len(sys.argv) - 1):
            print('{}: {}'.format(arg + 1, sys.argv[arg + 1]))
