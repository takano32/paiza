#!/usr/bin/env python3

import sys
a = []
for l in sys.stdin:
    a.append(l.rstrip())

a = ';'.join(a)
print(a)

