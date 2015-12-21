
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

def matches_mfcsam_result(sue, mfcsam_result):
	for prop, value in mfcsam_result.iteritems():
		sue_prop = sue.properties.get(prop, None)
		if sue_prop is None:
			continue
		if sue_prop != value:
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

	for s in sues:
		if matches_mfcsam_result(s, mfcsam_result):
			print s.num
