from functools import reduce
import operator

grid = [list(map(int,input().split())) for _ in range(20)]

def get_products(n,l,i,j):
    if i > l:
        yield reduce(operator.mul, (grid[i][i-k] for k in range(l)), 1)
    if j > l:
        yield reduce(operator.mul, (grid[i][j-k] for k in range(l)), 1)
    if i < n-l:
        yield reduce(operator.mul, (grid[i+k][j] for k in range(l)), 1)
    if j < n-l:
        yield reduce(operator.mul, (grid[i][j+k] for k in range(l)), 1)
    if i > l and j > l:
        yield reduce(operator.mul, (grid[i-k][j-k] for k in range(l)), 1)
    if i > l and j < n-l:
        yield reduce(operator.mul, (grid[i-k][j+k] for k in range(l)), 1)
    if i < l and j > l:
        yield reduce(operator.mul, (grid[i+k][j-k] for k in range(l)), 1)
    if i < l and j < l:
        yield reduce(operator.mul, (grid[i+k][j-k] for k in range(l)), 1)

n = 20
l = 4
max_product = 0
for i in range(20):
    for j in range(20):
        max_product = max(max_product, *get_products(n,l,i,j))
print(max_product)

