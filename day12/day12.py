
import json

def collect_numbers(data, result):
	if type(data) == int:
		result.append(data)
	elif type(data) == dict:
		for k in data:
			collect_numbers(data[k], result)
	elif type(data) == list:
		for v in data:
			collect_numbers(v, result)
	elif type(data) == unicode:
		pass
	else: 
		print "Don't know how to handle",type(data)

if __name__ == "__main__":
	data = json.load(open('day12.input'))

	result = []
	collect_numbers(data, result)
	print sum(result)
