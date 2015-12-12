
from nose.tools import assert_equals
from day6 import *

# NOTE: these tests are not very good. Lazy much?

def test_on():
	grid = Grid(10, 10)
	grid.on((0,0), (2,2))
	assert_equals(grid.count_lit(), 9)

def test_off():
	grid = Grid(10, 10)
	grid.on((0,0), (9,9))
	grid.off((1,1), (8,8))
	assert_equals(grid.count_lit(), 36)

def test_toggle():
	grid = Grid(10, 10)
	grid.on((3,3), (6,6))
	grid.toggle((2,2), (7,7))
	assert_equals(grid.count_lit(), 20)

