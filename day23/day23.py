
registers = dict(a=0, b=0)
program = open('day23.input','r').readlines()
offset = 0

def perform_instruction(instr, registers):
	print offset, registers
	global offset
	parts = instr.strip().split(" ")
	cmd = parts[0]
	if cmd == 'hlf':
		r = parts[1]
		registers[r] /= 2
		offset += 1
	elif cmd =='tpl':
		r = parts[1]
		registers[r] *= 3
		offset += 1
	elif cmd=='inc':
		r = parts[1]
		registers[r] += 1
		offset += 1
	elif cmd=='jmp':
		distance = int(parts[1])
		offset += distance
	elif cmd=='jie':
		r = parts[1][0]
		if registers[r] %2 == 0:
			distance = int(parts[2])
			offset += distance
		else:
			offset += 1
	elif cmd=='jio':
		r = parts[1][0]
		if registers[r] == 1:
			distance = int(parts[2])
			offset += distance
		else:
			offset += 1
while offset < len(program):
	perform_instruction(program[offset], registers)

print registers
