#!/usr/bin/env python3

from math import sqrt,ceil
from collections import Counter

def factors(n):
	for i in range(2,min(n,ceil(sqrt(n))+1)):
		if n % i == 0:
			yield from factors(i)
			yield from factors(n//i)
			break
	else:
		yield n

unique_factors = set()
for a in range(2,101):
	f_0 = Counter(factors(a))
	f = Counter(factors(a))
	for b in range(2,101):
		for i in f_0: # multiply by a
			f[i] += f_0[i]
		unique_factors.add(tuple(sorted(f.items())))
		
print(len(unique_factors))

