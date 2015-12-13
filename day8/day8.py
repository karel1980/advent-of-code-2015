
def eval_len(string):
	""" Yeah, so this is totally unsafe. I manually checked the input
	to make sure there are no nasty surprises in there. Let's hope I didn't miss anything """
	return len(eval(string))

	
def main():
	str_total = 0
	storage_total = 0
	for l in open('day8.input','r').readlines():
		str_total += len(l.strip())
		storage_total += eval_len(l)
	print str_total - storage_total

if __name__=="__main__":
	main()
