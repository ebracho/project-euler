#!/usr/bin/env python3
from itertools import starmap
print(sum(starmap(lambda i,y: (i+1)*sum(map(lambda z: ord(z)-64,y)), enumerate(sorted(x[1:-1] for x in input().split(','))))))

