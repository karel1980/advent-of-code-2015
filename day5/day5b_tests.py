
from day5b import *

string1 = 'qjhvhtzxzqqjkmpb'
string2 = 'xxyxx'
string3 = 'uurcxstgmygtbstg'
string4 = 'ieodomkazucvgmuy'

def test_repeating_pair():
	assert repeating_pair(string1)
	assert repeating_pair(string2)
	assert repeating_pair(string3)
	assert not repeating_pair(string4)

def test_xyx():
	assert xyx(string1)
	assert xyx(string2)
	assert not xyx(string3)
	assert xyx(string4)

