#!/usr/bin/env python3

def is_palindrome(s):
	return s == s[::-1]

print(sum(i for i in range(1,10**6) if is_palindrome(str(i)) and is_palindrome(str(bin(i))[2:])))

