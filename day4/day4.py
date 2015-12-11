from hashlib import md5

def mine(key, start):
	n = start
	while True:
		hash = md5('%s%d'%(key,n)).hexdigest()
		if hash.startswith('00000'):
			print n
			return
		n += 1

#mine('abcdef', 1)
mine('iwrupvqb', 1)
