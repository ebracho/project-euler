#!/usr/bin/env python3

from math import sqrt
primes = [2]

def genprimes():
	for i in range(3,1000000,2):
		s = int(sqrt(i))
		for p in primes:
			if i % p == 0:
				break
			elif p > s:
				primes.append(i)
				break
					
genprimes()
primeset = set(primes)

RANGE=1000

def p27():
	def consecutive_primes(a,b):
		n = 0
		while (n*n + a*n + b) in primeset:
			n += 1
		return n

	maxa = 0
	maxb = 0
	maxcp = 0
	for a in range(-RANGE, RANGE):
		for b in range(-RANGE-1, RANGE+1):
			cp = consecutive_primes(a,b)
			if cp > maxcp:
				maxcp = cp
				maxa = a
				maxb = b
			
	return (maxa*maxb, maxa, maxb, maxcp)

print(p27())
