locations = {}
x,y = 0,0

locations[(0,0)] = True
for c in open('day3.input').read():
	if c == 'v': y+=1
	elif c == '^': y-=1
	elif c == '<': x += 1
	elif c == '>': x -= 1

	print x,y
	locations[(x,y)] = True

print len(locations)
