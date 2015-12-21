
import sys 
import json

class Sue:
	def __init__(self, num, props):
		self.num = num
		self.properties = props

def read_inputs():
	sues = []

	for l in open('day16.input').readlines():
		parts = l.strip().split(" ")

		num = parts[1]
		props = {}

		for i in range(0,len(parts)-3,2):
			prop = parts[i+2].replace(":","")
			value = int(parts[i+3].replace(",",""))
			props[prop] = value

		sues.append(Sue(num, props))

	return sues

class MfcsamChecker:
	def __init__(self, result):
		self.result = result
		self.checkers = {}
		
		self.eq = lambda x,y: x == y
		gt = lambda x,y: x > y
		lt = lambda x,y: x < y

		self.checkers['cats'] = gt
		self.checkers['trees'] = gt
		self.checkers['pomeranians'] = lt
		self.checkers['goldfish'] = lt

	def check_props(self, props):
		for prop, value in mfcsam_result.iteritems():
			current_prop = props.get(prop, None)
			if current_prop is None:
				continue
			if not self.checkers.get(prop, self.eq)(current_prop, value):
				return False
		return True

mfcsam_result = {
	'children': 3,
	'cats': 7,
	'samoyeds': 2,
	'pomeranians': 3,
	'akitas': 0,
	'vizslas': 0,
	'goldfish': 5,
	'trees': 3,
	'cars': 2,
	'perfumes': 1
}

if __name__=='__main__':
	sues = read_inputs()
	checker = MfcsamChecker(mfcsam_result)

	for s in sues:
		if checker.check_props(s.properties):
			print s.num
