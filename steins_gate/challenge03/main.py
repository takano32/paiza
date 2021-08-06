#!/usr/bin/env python3
import sys
import math

n = m = l = 0

ds = []
ps = []
first = True

i = 0
for line in sys.stdin:
    i += 1
    if first:
        first = False
        [n, m, l] = line.rstrip().split(' ')
        n = int(n)
        m = int(m)
        l = int(l)
        continue
    if i < n:
        d = line.rstrip()
        ds.append(d)
    else:
        p = line.rstrip()
        ps.append(p)

