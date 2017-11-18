#!/usr/bin/env python3
from math import floor,sqrt
def divisors(n):
	res = set([1])
	for i in range(2,int(sqrt(n))+1):
		if n % i == 0:
			res.add(i)
			res.add(n//i)
	return res
		

def is_abundant(n):
	return sum(divisors(n)) > n

abundant_numbers = [x for x in range(1,28124) if is_abundant(x)]
two_abundant_sums = set()
for i in abundant_numbers:
	for j in abundant_numbers:
		s = i+j
		if s > 28123:
			break
		else:
			two_abundant_sums.add(s)

print(min(abundant_numbers))
print(max(abundant_numbers))
print(sum(x for x in range(1,28124) if x not in two_abundant_sums))

print(28123,divisors(28123),sum(divisors(28123)),is_abundant(28123))
