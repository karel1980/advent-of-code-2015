locations = set()
x,y = 0,0

locations.add((0,0))
for c in open('day3.input').read():
	if c == 'v': y+=1
	elif c == '^': y-=1
	elif c == '<': x += 1
	elif c == '>': x -= 1

	locations.add((x,y))

print len(locations)
