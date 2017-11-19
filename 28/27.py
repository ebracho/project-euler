#!/usr/bin/env python3

SPIRAL=1001
RINGS=(SPIRAL-1)//2

s = 1
for i in range(1,RINGS+1):
	side = 2*i+1
	topright    = side**2
	topleft     = topright - side + 1
	bottomleft  = topleft - side + 1
	bottomright = bottomleft - side + 1
	s += topright + topleft + bottomleft + bottomright

print(s)

"""
43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31
"""
