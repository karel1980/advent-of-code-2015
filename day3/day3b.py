locations = {}
turn=0

class DeliveryPerson:
	def __init__(self):
		self.x, self.y = 0,0

	def up(self):
		self.y += 1

	def down(self):
		self.y -= 1

	def left(self):
		self.x += 1

	def right(self):
		self.x -= 1

santa = DeliveryPerson()
robosanta = DeliveryPerson()
deliverers = [santa,robosanta]
current = 0

locations[(0,0)] = True
for c in open('day3.input').read():
	who = deliverers[current]
	current = 1 - current

	if c == 'v': who.down()
	elif c == '^': who.up()
	elif c == '<': who.left()
	elif c == '>': who.right()

	print current, who.x, who.y
	locations[(who.x,who.y)] = True

print len(locations)
