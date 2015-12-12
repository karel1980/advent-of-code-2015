
from day5 import *

string1 = 'ugknbfddgicrmopn'
string2 = 'aaa'
string3 = 'jchzalrnumimnmhp'
string4 = 'haegwjzuvuyypxyu'
string5 = 'dvszwmarrgswjxmb'

def test_threevowels():
	assert threevowels(string1)
	assert threevowels(string2)
	assert threevowels(string3)
	assert threevowels(string4)
	assert not threevowels(string5)

def test_repetition():
	assert repetition(string1)
	assert repetition(string2)
	assert not repetition(string3)
	assert repetition(string4)
	assert repetition(string5)

def test_bad():
	assert not bad(string1)
	assert not bad(string2)
	assert not bad(string3)
	assert bad(string4)
	assert not bad(string5)
