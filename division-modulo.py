import sys


def division(a, d):
    q = 0
    r = abs(a)
    while r >= d:
        r = r-d
        q = q+1
    if a < 0 and r > 0:
        r = d-r
        q = -(q+1)
    print "quotient: "+str(q)
    print "reminder: "+str(r)


if len(sys.argv) > 2:
    a = int(sys.argv[1])
    d = abs(int(sys.argv[2]))
    division(a, d)
