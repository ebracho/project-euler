#!/usr/bin/env python3

from math import factorial

# Returns the factoradic representatin of decimal n
# Ex: factoradic(11) => [1,2,1,0] 
# ie [1*3! + 2*2! + 1*1! + 0*0!]
def factoradic(n,pad=0):
	res = []
	radices = [1]
	while radices[-1] < n:
		radices.append(radices[-1] * (len(radices) + 1))
	while radices:
		radix = radices.pop()
		res.append(n//radix)
		n = n % radix
	if not res[0]:
		res = res[1:]
	res = res + [0]
	while factorial(len(res)) < pad:
		res = [0] + res
	return res

# Returns the nth lexicographic permutation of seq
def permutation(seq,n):
	if n >= factorial(len(seq)):
		return None
	seq = list(seq)
	f = factoradic(n, pad=factorial(len(seq)))
	res = []
	while f:
		res.append(seq.pop(f.pop(0)))
	return res


print(''.join(map(str,permutation(range(10),999999))))
