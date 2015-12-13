
def eval_len(string):
	""" Yeah, so this is totally unsafe. I manually checked the input
	to make sure there are no nasty surprises in there. Let's hope I didn't miss anything """
	return len(eval(string))

def escape_char(c):
	if c == '"':
		return '\\"'
	if c == '\\':
		return '\\\\'
	return c

def escape_string(string):
	return '"' + "".join([ escape_char(c) for c in string]) + '"'

def main():
	str_total = 0
	escape_total = 0
	for l in open('day8.input','r').readlines():
		str_total += len(l.strip())
		escape_total += len(escape_string(l.strip()))
	print escape_total - str_total

if __name__=="__main__":
	main()
