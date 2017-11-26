#!/usr/bin/env python3

def pandigital(*nums):
	numstr = ''.join(map(str,nums))
	return '0' not in numstr and len(numstr) == len(set(numstr)) and int(max(numstr)) == len(numstr)

def pandigital9(*nums):
	return len(''.join(map(str,nums))) == 9 and pandigital(*nums)

	
pandigital9_products = set()
for i in range(1,9999):
	for j in range(i,9999):
		if len(''.join(map(str,[i,j,i*j]))) > 9:
			break
		if pandigital9(i,j,i*j):
			pandigital9_products.add(i*j)

print(sum(pandigital9_products))
