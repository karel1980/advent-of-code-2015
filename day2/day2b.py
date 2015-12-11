lines = open('day2.input', 'r').readlines()

total = 0
for l in lines:
	a,b,c = [ int(n) for n in l.strip().split('x') ]
	current = 2 * min(a+b , a+c , b+c) + a*b*c

	total += current

print total



