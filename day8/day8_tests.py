
from nose.tools import assert_equals
from day8 import *
from day8b import escape_string

string1 = '""'
string2 = '"abc"'
string3 = '"aaa\\"aaa"'
string4 = '"\\x27"'

strings = [string1,string2,string3,string4]

def test_eval_len():
	assert_equals(eval_len('""'), 0)
	assert_equals(eval_len('"abc"'), 3)
	assert_equals(eval_len('"aaa\\"aaa"'), 7)
	assert_equals(eval_len('"\\x27"'), 1)

def test_escape_string():
	assert_equals(len(escape_string('""')), 6)
	assert_equals(len(escape_string('"abc"')), 9)
	assert_equals(len(escape_string('"aaa\\"aaa"')), 16)
	assert_equals(len(escape_string('"\\x27"')), 11)


def test_day8b_result():
	total1 = sum([len(s) for s in strings])
	total2 = sum([len(escape_string(s)) for s in strings])

	assert_equals(total2, 42)
	assert_equals(total1, 23)
	assert_equals(total2 - total1, 19)
