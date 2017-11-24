#!/usr/bin/env python3
print(sum(i if sum(map(lambda x: int(x)**5, str(i))) == i else 0 for i in range(2,(5*9**5+1))))
