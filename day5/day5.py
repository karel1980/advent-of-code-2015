
import re

def threevowels(text):
	return len(re.sub('[^aeiou]','',text)) >= 3

repetition_pattern = re.compile('.*(.)\\1.*')
def repetition(text):
	return repetition_pattern.match(text) != None

bad_pattern = re.compile('.*(ab|cd|pq|xy).*')
def bad(text):
	return bad_pattern.match(text) is not None

def is_nice(text):
	return threevowels(text) and repetition(text) and not bad(text)

def main():
	nice_count = 0
	for line in open('day5.input','r').readlines():
		if is_nice(line):
			print "good:",line
			nice_count += 1
	print nice_count


if __name__ == '__main__':
	main()
