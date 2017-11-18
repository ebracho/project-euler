#!/usr/bin/env python3
from math import floor,sqrt

def divisors(n):
	yield 1
	for i in range(2,int(floor(sqrt(n)))+1):
		if n%i==0:
			yield i
			yield n//i

proper_divisors_sum = {}
amicable_numbers = []

for i in range(2,10000):
	pdsi = proper_divisors_sum[i] = sum(divisors(i))
	if 1 < pdsi < i and proper_divisors_sum[pdsi] == i:
		amicable_numbers.append((pdsi, i))

print(sum(map(sum,amicable_numbers)))
	
