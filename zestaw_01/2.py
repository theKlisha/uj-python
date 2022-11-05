from math import sqrt, ceil
import sys

def factorize(n):
    i = 2
    while True:
        found = False
        for j in range(i, ceil(sqrt(n)) + 1):
            if n % j == 0:
                i = j; n //= j; found = True;
                yield j; break
        if not found:
            yield n; return

def formatter(l):
    d = {}
    s = []
    for f in l:
        d[f] = 1 if d.get(f) == None else d[f] + 1
    for f, k in d.items():
        s.append("{}".format(f) if k == 1 else "{}^{}".format(f, k))
    return "*".join(s)

argv = sys.argv[1:]
for arg in argv:
    s = formatter(factorize(int(arg)))
    print("{} = {}".format(arg, s))
