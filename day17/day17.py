
class Container:
	def __init__(self, size, cid):
		self.cid = cid
		self.size = size

	def __repr__(self):
		return str((self.cid, self.size))

def solve(containers, remaining=150, used = []):
	#print remaining, containers
	if remaining == 0:
		#print "HIT", used
		yield 1
		return
	if remaining < 0:
		return
	if len(containers) == 0:
		return

	choices = list(filter(lambda x: x <= remaining,containers))
	if len(choices) == 0:
		return
	for c in choices:
		bigger_or_eq = filter(lambda x: x.cid > c.cid, choices)
		yield sum(solve(bigger_or_eq, remaining - c.size, used + [c]))

containers = [ int(l.strip()) for l in open('day17.input').readlines() ]
containers = [ Container(i, sz) for i,sz in zip(containers, range(len(containers))) ]
print sum(solve(containers))

#containers = [20,15,10,5,5]
#containers = [ Container(i, sz) for i,sz in zip(containers, range(len(containers))) ]
#print str(containers)
#print sum(solve(containers, 25))
