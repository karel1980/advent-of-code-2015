
def look_and_say(string,repeat):
	for i in range(repeat):
		next_string = ""
		last = ''
		count = 0
		for c in string:
			if last != c and count > 0:
				next_string += str(count) + last
				count = 0
			count += 1
			last = c
		if count > 0:
			next_string += str(count) + last
		string = next_string

	return string

def main():
	l = open('day10.input','r').readlines()[0].strip()

	print len(look_and_say(l,40))

if __name__ == '__main__':
	main()
