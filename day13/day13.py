
import itertools

def get_best_happiness(input_path):
	scores = {}
	names = set()

	for l in open(input_path,'r').readlines():
		parts = l.strip().split()

		name1 = parts[0]
		points = int(parts[3])
		if parts[2] == "lose": points = -points
		name2 = parts[10][:-1]

		names.add(name1)
		names.add(name2)
		scores[(name1,name2)] = points

	best = -999999999999 
	for p in itertools.permutations(names):
		total = 0
		for i in range(len(p)):
			a,b = p[i],p[(i+1)%len(p)]
			total += scores[(a,b)]
			total += scores[(b,a)]

		if total > best:
			best = total

	return best

if __name__=="__main__":
	print get_best_happiness("day13.input")
