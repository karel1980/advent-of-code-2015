
class Assign:
	def __init__(self, name, expr):
		self.name = name
		self.expr = expr

	def eval(self, context):
		context[self.name] = self.expr.eval(context)

class Literal:
	def __init__(self, value):
		self.value = value

	def eval(self, context):
		return self.value

class Var:
	def __init__(self, name):
		self.name = name

	def eval(self, context):
		return context[self.name]
	
class Op:
	def __init__(self, fn, *args):
		self.fn = fn
		self.args = args

	def get_vars(self):
		return [ a for a in args if isinstance(Var, a) ]

	def eval(self, context):
		eval_args = [ arg.eval(context) for arg in self.args ]
		return self.fn(*eval_args)

def parse_instructions(instructions):
	return [ parse_instruction(l.strip()) for l in instructions ]

def parse_instruction(instruction):
	""" 'parse' should be taken with a grain of salt here """
	parts = instruction.split(' -> ')

	if len(parts) != 2:
		raise Exception('not an assignment')
	
	target = parts[1]
	expr = parse_expr(parts[0])
	return Assign(target, expr)

def parse_expr(expr):
	parts = expr.split(' ')

	if len(parts) == 1:
		if parts[0].isdigit():
			return Literal(int(parts[0]))
		return Var(parts[0])
			
	elif len(parts) == 2:
		if parts[0] != 'NOT':
			raise Exception('unhandled expression ' + expr)
		return Op(lambda x: ~ x & 65535, parse_expr(parts[1]))

	elif len(parts) == 3:
		op = parts[1]

		if parts[1] == 'LSHIFT':
			opfn = lambda x,y: x << y
		elif parts[1] == 'RSHIFT':
			opfn = lambda x,y: x >> y
		elif parts[1] == 'OR':
			opfn = lambda x,y: x | y
		elif parts[1] == 'AND':
			opfn = lambda x,y: x & y
		elif parts[1] == 'XOR':
			opfn = lambda x,y: x ^ y

		return Op(opfn, parse_expr(parts[0]), parse_expr(parts[2]))

	raise Exception('unhandled expression ' + expr)

def is_const(value):
	return value.isdigit()

if __name__ == '__main__':
	parsed = parse_instructions(open('day7.input','r').readlines())

	context = {}
	todo = [ p for p in parsed ]
	while True:
		print "TODO:",len(todo)
		next_todo = []

		for instr in todo:
			try:
				instr.eval(context)

			except KeyError:
				next_todo.append(instr)

		if len(next_todo) == 0:
			break

		todo = next_todo

	print "A =" , context['a']
