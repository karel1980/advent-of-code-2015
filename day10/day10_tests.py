
from nose.tools import assert_equals
from day10 import *

def test_look_and_say():
	assert_equals(look_and_say('1',1), '11')
	assert_equals(look_and_say('1',2), '21')
	assert_equals(look_and_say('1',3), '1211')
	assert_equals(look_and_say('1',4), '111221')
	assert_equals(look_and_say('1',5), '312211')
