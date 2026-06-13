import sys


def suma(a, b):
    s = ""
    n = len(a)
    c = 0
    print "  "+a
    print "+ "+b
    for j in range(n-1, -1, -1):
        aj = int(a[j])
        bj = int(b[j])
        d = (aj+bj+c)/10
        s = str(aj+bj+c-(10*d)) + s
        c = d
    print "  "+s

if len(sys.argv) > 2:
    a = str(sys.argv[1])
    b = str(sys.argv[2])
    if len(a) > len(b):
        for x in xrange(len(a)-len(b)): b = "0"+b
    elif len(b) > len(a):
        for x in xrange(len(b)-len(a)): a = "0"+a
    suma(a, b)
