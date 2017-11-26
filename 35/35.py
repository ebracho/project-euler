#!/usr/bin/env python3

from math import sqrt
primes = [2]

def genprimes():
	for i in range(3,10**6,2):
		s = int(sqrt(i))
		for p in primes:
			if i % p == 0:
				break
			elif p > s:
				primes.append(i)
				break

genprimes()
primeset = set(primes)

def is_circular_prime(n):
	ns = str(n)
	for i in range(len(ns)):
		if not int(ns) in primeset:
			return False
		ns = ns[-1] + ns[:-1]
	return True

print(sum(1 for i in range(2,10**6) if is_circular_prime(i)))
		
