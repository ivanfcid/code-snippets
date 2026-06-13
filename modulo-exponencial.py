import sys


def mod_exp(b, n, m):
    x = 1
    a = "{0:b}".format(n)
    power = b % m
    for j in range(len(a)-1, -1, -1):
        if int(a[j]) == 1: x = (x*power) % m;
        power = (power*power) % m
    print str(b)+"^"+str(n)+" mod "+str(m)+" = "+str(x)

if len(sys.argv) > 3:
    b = int(sys.argv[1])
    n = int(sys.argv[2])
    m = int(sys.argv[3])
    mod_exp(b, n, m)
