
import random
import re

def get_puzzledata(lines):
	""" returns the replacement rules and the initial molecule """
	rules = dict()
	molecule = ""

	for l in lines:
		if " => " in l:
			parts = l.strip().split(" => ")
			rules.setdefault(parts[1], []).append(parts[0])
		elif len(l.strip()) > 0:
			molecule = l.strip()

	return rules, molecule

def generate_solutions(rules, current_molecule, depth=1, current_best=10000):
	if depth > current_best:
		return 10000
	#if random.random() > 0.9999: print len(current_molecule)
	if current_molecule == 'e':
		print depth
		return depth

	if len(current_molecule) == 0:
		return 10000

	best = current_best
	rules_longest_first = sorted(rules.keys(), key=lambda n: -len(n))
	for r in rules_longest_first:
		positions = [m.start() for m in re.finditer(r, current_molecule)]
		for p in positions:
			for replacement in rules[r]:
				new_molecule = current_molecule[:p] + replacement + current_molecule[p+len(r):]
				score = generate_solutions(rules, new_molecule, depth+1, best+depth)
				if score < best:
					best = score

	return depth + best
		
r,m = get_puzzledata(open('day19.input','r').readlines())
print generate_solutions(r, m)
