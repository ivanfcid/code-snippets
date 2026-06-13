import sys


def gcd(a, b):
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    print x


if len(sys.argv) > 2:
    a = int(sys.argv[1])
    b = int(int(sys.argv[2]))
    gcd(a, b)
