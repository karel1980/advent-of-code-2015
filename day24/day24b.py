
from operator import mul
from itertools import permutations

packages = [ int(n.strip()) for n in open('day24.input').readlines() ]

def generate_valid_part1(remaining, part1, target, total):
	global smallest
	if total > target: return
	
	if total == target:
		if len(part1) < smallest:
			smallest = len(part1)
		yield part1, remaining

	if len(part1) == smallest:
		return

	if total < target:
		for i in range(0, len(remaining)):
			n = remaining[i]
			del remaining[i]
			part1.append(n)
			for t in generate_valid_part1(remaining, part1, target, total+n):
				yield t
			del part1[len(part1)-1]
			remaining.insert(i, n)

def generate_valid_part2(remaining, part2, target, total):
	global smallest
	if total > target: return
	
	if total == target:
		yield part2, packages

	if total < target:
		for i in range(0, len(remaining)):
			n = remaining[i]
			del remaining[i]
			part2.append(n)
			for t in generate_valid_part2(remaining, part2, target, total+n):
				yield t
			del part2[len(part2)-1]
			remaining.insert(i, n)


# Sorting reverse generates smaller 'part1' lists earlier, helps pruning
packages.sort()
packages.reverse()
part_weight = sum(packages)/4

smallest = 4 # Found this through an earlier run, speeds things up
best_q = 100000000000
for part1,remaining in generate_valid_part1(packages, [], part_weight, 0):
	for part2,r2 in generate_valid_part2(remaining, [], part_weight, 0):
		for part3,part4 in generate_valid_part2(r2, [], part_weight, 0):
			q = reduce(mul, part1)
			if q < best_q:
				print q
				best_q = q

print best_q
