#!/usr/bin/env python3
import sys
import math

n = m = l = 0

dss = []
pss = []
first = True

i = 0
for line in sys.stdin:
    if first:
        first = False
        [n, m, l] = line.rstrip().split(' ')
        n = int(n)
        m = int(m)
        l = int(l)
        continue
    i += 1        
    if i < n:
        ds = line.rstrip()
        ds = ds.split(' ')
        dss.append(ds)
    else:
        ps = line.rstrip()
        ps = ps.split(' ')
        pss.append(ps)


print('N: ', n)
print('M: ', m)
print('L: ', l)

for ds in dss:
    for d in ds:
        print('d(i, j): ', d)

