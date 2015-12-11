data = open('day1.input', 'r').read()

pos = 0
floor = 0
while floor >= 0:
	if data[pos] == '(':
		floor = floor + 1
	else:
		floor = floor - 1
	pos = pos + 1

print pos
