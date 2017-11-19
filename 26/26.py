#!/usr/bin/env python3

from math import gcd

# Returns the mulitiplicative order of base (mod n)
# http://mathworld.wolfram.com/MultiplicativeOrder.html
#
# Ex: 10^6 (mod 7) = 1 so multiplicative order of 10 (mod 7) is 6.
#
# This also hapens to be the length of the period of the base-adic expansion of 1/n
#
def multiplicative_order(n,base=10):
	# ord(n,b) = ord(n/gcd(n,b),b) 
	# https://en.wikipedia.org/wiki/Multiplicative_order
	d = None
	while d != 1:
		d = gcd(n,base)
		n //= d

	r = base % n
	e = 1
	while r > 1:
		r = (r*base) % n
		e += 1
	return e


# Interesting obesrvation: ord_n(b) = n-1 <=> n is prime
def p26():
	def candidates():
		for i in range(1,1000):
			yield (multiplicative_order(i),i)
	return max(candidates())[1]



foo()

