
import re

def make_alphas(start, end):
    return "".join([chr(c) for c in range(ord(start),ord(end)+1)])

alphabet = make_alphas('a','z')

class Validator:
	def __init__(self):
		sequences = [ alphabet[n:n+3] for n in range(len(alphabet)-2) ]
		self.seq_regex = re.compile("(%s)"%("|".join(sequences)))
		self.iol_regex = re.compile("[iol]")
		self.double_pair_regex = re.compile('([a-z])\\1.*([a-z])\\2')

	def _contains_sequence_of_three(self, password):
		return self.seq_regex.search(password) is not None

	def _contains_iol(self, password):
		return self.iol_regex.search(password) is not None

	def _contains_two_different_pairs(self, password):
		match = self.double_pair_regex.search(password)
		return match is not None and match.group(1) != match.group(2)

	def is_valid_password(self, password):
		return self._contains_sequence_of_three(password) and\
			not self._contains_iol(password) and\
			self._contains_two_different_pairs(password)

class PasswordTool:
	def __init__(self):
		self.validator = Validator()

	def get_next_password(self, password):
		chars = [ c for c in password ]
		n = len(password)-1
		while n >= 0:
			if ord(chars[n]) < ord('z'):
				chars[n] = chr(ord(chars[n])+1)
				break
			else:
				chars[n] = "a"
			n -= 1
		if n < 0:
			return "a"*(len(password)+1)
		return "".join(chars)

	def get_next_valid_password(self, password):
		valid = False
		while not valid:
			password = self.get_next_password(password)
			valid = self.validator.is_valid_password(password)
		return password

if __name__ == '__main__':
	tool = PasswordTool()
	print tool.get_next_valid_password("vzbxxyzz")
