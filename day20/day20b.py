from sympy.ntheory import factorint

import sys
import math

n = 1000000
houses = [0 for i in range(n)]

for i in range(1, n):
	j = 1
	while i*j < n and j <= 50:
		houses[i*j] += 11*i
		j+=1

print max(houses)
for p in range(len(houses)):
	if houses[p] > 36000000:
		print p
		sys.exit(0)

