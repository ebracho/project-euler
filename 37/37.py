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

def is_trunctable_prime(n):
	n1 = n2 = n
	while n1 and n2:
		if not (n1 in primeset and n2 in primeset):
			return False
		n1 = n1//10
		n2 = int(str(n2)[1:] or 0)
	return True

print(sum(i for i in range(10,10**6) if is_trunctable_prime(i)))

