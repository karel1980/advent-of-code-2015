
from nose.tools import assert_equals
from day13 import get_best_happiness

def test_sample():
	assert_equals(330, get_best_happiness('day13.sample'))
