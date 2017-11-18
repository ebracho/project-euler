#!/usr/bin/env python3

# Generates lexicographical permutations of seq_orig in order
#
# How it works:
#
# Say you have a sorted tuple seq = (a,b,c) of length n = 3
#
# The first n-1 permutations can by generated by:
#
#    1. Remove the first element a from seq
#    2. Prepend a to every permutation of seq-a
#    3. Repeat for the second, third, ... nth element of seq
#
# For lexicographical permutations of (a,b,c) given that a < b < c :
#
#    (a,) + (b,c)
#    (a,) + (c,b)
#    (b,) + (a,c)
#    (b,) + (c,a)
#    (c,) + (a,b)
#    (c,) + (b,a)
#
def permutations(seq):
	def _permutations(_seq):
		if len(_seq) == 1:
			yield _seq
		else:
			yield from ((i,) + p_ni for i in _seq for p_ni in permutations(tuple(x for x in _seq if x != i)))    

	return _permutations(tuple(sorted(seq)))


perms = permutations(range(10))
for i in range(999999):
	next(perms)
print(''.join(map(str,next(perms))))

