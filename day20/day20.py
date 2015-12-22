from sympy.ntheory import factorint

import sys
import math


def powsum(p, e):
	if p == 1: return 1
	return sum([p**n for n in range(0, e+1)])

def divisor_sum(n):
	r = 1
	for k,v in factorint(n).iteritems():
		r *= powsum(k, v)

	return r

def num_presents(house_num):
	return 10 * divisor_sum(house_num)

def find_upper_limit():
	i = 1
	while num_presents(i) < 36000000:
		i *= 2
	return i

def find_upper_limit2():
	i = 1
	n = 1
	best = None
	while best is None:
		i+=1
		n *= i
		if num_presents(n) >= 36000000:
			best = n
	return best

# check samples:
#for i in range(1, 10):
#	print i, num_presents(i)

#print find_upper_limit()
#print find_upper_limit2()

for i in range(1, find_upper_limit()):
	if i%10000 == 0: print i
	if num_presents(i) > 36000000:
		print i
		sys.exit(1)
