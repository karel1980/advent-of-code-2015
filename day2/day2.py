lines = open('day2.input', 'r').readlines()

total = 0
for l in lines:
	a,b,c = [ int(n) for n in l.strip().split('x') ]
	j,k,l = a*b , a*c , b*c

	#print j,k,l
	#print 2*j, 2*k, 2*l

	area = 2*(j+k+l)+min(j,k,l)
	#print area
	total += area

print total



