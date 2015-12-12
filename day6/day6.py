
import re

class Grid:
	def __init__(self, w=1000, h=1000):
		self.w = w
		self.h = h
		self.cells = [0 for i in range(w*h)]

	def on(self, p1, p2):
		self._set_range(p1, p2, lambda value: 1)

	def off(self, p1, p2):
		self._set_range(p1, p2, lambda value: 0)

	def toggle(self, p1, p2):
		self._set_range(p1, p2, lambda value: 1-value)

	def _set_range(self, p1, p2, fn):
		x1,y1 = p1
		x2,y2 = p2
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				self._set_cell(x,y,fn)

	def _set_cell(self, x, y, fn):
		idx = y*self.w + x
		self.cells[idx] = fn(self.cells[idx])

	def count_lit(self):
		return sum(self.cells)

def main():
	grid = Grid()
	cmd_pattern = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
	for l in open('day6.input','r').readlines():
		m = cmd_pattern.match(l.strip())

		if m is None:
			print "no match on line " + l
			continue

		cmd = m.group(1)
		x1,y1,x2,y2 = [int(m.group(n+2)) for n in range(4)]

		#print cmd," - ", x1,x2,y1,y2

		if cmd =='turn on':
			grid.on((x1,y1),(x2,y2))
		elif cmd =='turn off':
			grid.off((x1,y1),(x2,y2))
		elif cmd =='toggle':
			grid.toggle((x1,y1),(x2,y2))

	print grid.count_lit()

if __name__ == '__main__':
	main()
