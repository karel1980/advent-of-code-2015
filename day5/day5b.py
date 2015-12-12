
import re

repeating_pair_pattern = re.compile('.*(..).*\\1.*')
def repeating_pair(text):
	return repeating_pair_pattern.match(text) is not None

xyx_pattern = re.compile('.*(.).\\1.*')
def xyx(text):
	return xyx_pattern.match(text) is not None

def is_nice(text):
	return repeating_pair(text) and xyx(text)

def main():
	nice_count = 0
	for line in open('day5.input','r').readlines():
		if is_nice(line):
			print "good:",line
			nice_count += 1
	print nice_count


if __name__ == '__main__':
	main()
