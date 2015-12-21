
import re

def get_puzzledata(lines):
	""" returns the replacement rules and the initial molecule """
	rules = dict()
	molecule = ""

	for l in lines:
		if " => " in l:
			parts = l.strip().split(" => ")
			rules.setdefault(parts[0], []).append(parts[1])
		elif len(l.strip()) > 0:
			molecule = l.strip()

	return rules, molecule

def generate_solutions(rules, molecule):
	solutions = set()
	for r in rules.keys():
		positions = [m.start() for m in re.finditer(r, molecule)]
		for p in positions:
			for replacement in rules[r]:
				new_molecule = molecule[:p] + replacement + molecule[p+len(r):]
				solutions.add(new_molecule)
	return len(solutions)
		
r,m = get_puzzledata(open('day19.input','r').readlines())
print generate_solutions(r, m)
