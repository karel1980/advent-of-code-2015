
class Reindeer:
	def __init__(self, name, fly_speed, fly_duration, rest_duration):
		self.name = name
		self.speeds = dict(flying=fly_speed, resting=0)
		self.durations = dict(flying=fly_duration, resting=rest_duration)
		self.time = 0
		self.score = 0
		self.distance = 0

		self._start_state("flying")

	def tick(self):
		self.distance = self.distance + self._current_speed()

		self.time += 1

		if self.time >= self.state_end:
			if self.state == "flying":
				self._start_state("resting")
			else:
				self._start_state("flying")


	def _start_state(self, state):
		self.state = state
		self.state_end = self.time + self._current_duration()

	def _current_speed(self):
		return self.speeds[self.state]

	def _current_duration(self):
		return self.durations[self.state]

def get_reindeers(input_path):
	deers = []
	for l in open(input_path).readlines():
		parts = l.strip().split(" ")
		name = parts[0]
		fly_speed = int(parts[3])
		fly_duration = int(parts[6])
		rest_duration = int(parts[13])

		deers.append(Reindeer(name, fly_speed, fly_duration, rest_duration))

	return deers

def simulate(duration, deers):
	for i in range(duration):
		for d in deers:
			d.tick()
		max_dist = max([d.distance for d in deers])
		for leader in filter(lambda d:d.distance==max_dist, deers):
			leader.score += 1
		#print max_dist
		#for d in deers:
		#	print d.name, d.distance, d.score

if __name__=="__main__":
	deers = get_reindeers('day14.input')
	simulate(2503, deers)

	for d in deers:
		print d.name, d.distance, d.score


