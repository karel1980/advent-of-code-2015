
from nose.tools import assert_equals
from day14 import Reindeer, simulate, get_reindeers

def test_samples():
	deers = get_reindeers('day14.sample')

	comet = deers[0]
	dancer = deers[1]

	simulate(1, deers)
	assert_equals(14, comet.distance)
	assert_equals(16, dancer.distance)

	simulate(9, deers)
	assert_equals(140, comet.distance)
	assert_equals(160, dancer.distance)

	simulate(1, deers)
	assert_equals(140, comet.distance)
	assert_equals(176, dancer.distance)

	simulate(1, deers)
	assert_equals(140, comet.distance)
	assert_equals(176, dancer.distance)
