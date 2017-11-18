#!/usr/bin/env python3
from functools import reduce
l = reversed([list(map(int, input().split())) for _ in range(15)])
print(reduce(lambda r1,r2: list(map(sum,zip(r2,map(max,zip(r1,r1[1:]))))), l, next(l)))
	
