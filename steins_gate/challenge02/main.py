#!/usr/bin/env python3
import sys
import math

n = k = 0

x = []
first = True
for l in sys.stdin:
    if first:
        first = False
        [n, k] = l.rstrip().split(' ')
        n = int(n)
        k = float(k)
        continue
    x.append(float(l.rstrip()))

if False: print('n: %d' % n)
if False: print('k: %f' % k)

exp = k

sum = 0.0
for y in x:
    sum += y
    if False: print('exp: %f' % y)

if False: print('sum exp: %f' % sum)
if False: print('sum / exp: %f' % (sum / exp))
if False: print('result: %d' % int(math.ceil(sum / exp)))

print(int(math.ceil(sum / exp)))
