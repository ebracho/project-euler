def product(lb,ub):
	res = 1
	for i in range(lb,ub+1):
		res *= i
	return res

def fact(x):
	return product(1,x)

def rising_fact(x,n):
	return product(x,x+n-1)

# Returns the i'th dim-simplex number
def simplex(dim,i):
	return rising_fact(i,dim)//fact(dim)

print(simplex(20,21))
