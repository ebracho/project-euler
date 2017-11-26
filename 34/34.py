#!/usr/bin/env python3

from math import factorial

print(sum(i for i in range(3,999999) if i == sum(map(factorial,map(int,str(i))))))

