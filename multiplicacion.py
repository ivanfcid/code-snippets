import sys
from array import array


def multiplicacion(a, b):
    c = [""]*len(a)
    n = len(a)
    print "  "+str(int(a, 2))+"("+a+")"
    print " *"+str(int(b, 2))+"("+b+")"
    for j in range(0, n):
        if int(b[j]) == 1:
            c[j] = a
            for x in range(n-1-j, 0, -1): c[j] = c[j]+"0";
        else: c[j] = "0";
    p = 0
    for j in range(0, n): p = bin(int(str(p), 2)+int(c[j], 2))
    print "  "+str(int(p[2:], 2))+"("+p[2:]+")"
    
if len(sys.argv) > 2:
    a = "{0:b}".format(int(sys.argv[1]))
    b = "{0:b}".format(int(sys.argv[2]))
    if len(a) > len(b):
        for x in xrange(len(a)-len(b)): b = "0"+b
    elif len(b) > len(a):
        for x in xrange(len(b)-len(a)): a = "0"+a
    multiplicacion(a, b)
