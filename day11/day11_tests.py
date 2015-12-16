
from nose.tools import assert_equals
from day11 import Validator, PasswordTool

def test_contains_iol():
	validator = Validator()
	assert_equals(True, validator._contains_iol("hijklmn"))
	assert_equals(True, validator._contains_iol("aaibb"))
	assert_equals(True, validator._contains_iol("aaobb"))
	assert_equals(True, validator._contains_iol("aalbb"))
	assert_equals(False, validator._contains_iol("aaxbb"))

def test_contains_two_different_pairs():
	validator = Validator()
	assert_equals(True, validator._contains_two_different_pairs("abbceffg"))
	assert_equals(False, validator._contains_two_different_pairs("abbcefg"))

def test_contains_sequence_of_three():
	validator = Validator()
	assert_equals(True, validator._contains_sequence_of_three("xxabcyy"))
	assert_equals(False, validator._contains_sequence_of_three("abdce"))

def test_get_next_password():
	tool = PasswordTool()
	assert_equals("abcdefgi", tool.get_next_password("abcdefgh"))
	assert_equals("aaaa", tool.get_next_password("zzz"))

def test_get_next_valid_password():
	tool = PasswordTool()
	assert_equals("abcdffaa", tool.get_next_valid_password("abcdefgh"))
	assert_equals("ghjaabcc", tool.get_next_valid_password("ghijklmn"))
