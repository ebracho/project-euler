#!/usr/bin/env python3

def p31():
	denoms = (1,2,5,10,20,50,100,200)
	totals = [1] + [0 for _ in range(200)]
	for d in denoms:
		for i in range(d,201):
			totals[i] += totals[i-d]
	return totals[200]

print(p31())

