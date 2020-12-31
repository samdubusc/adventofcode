import copy
instructions = []
line_number = 0
nop_jmp = []

with open("input.txt", "r") as fp:
  for line in fp.readlines():
    if line != '\n':
      instr = line.split(' ')
      instructions.append({
        'code': instr[0],
        'value': int(instr[1]),
      })
      if instructions[-1]['code'] != 'acc':
        nop_jmp.append(line_number)
      line_number += 1

def brute_force(instructions):

  loop = False
  visited = {}

  pointer = 0
  accumulator = 0
  while pointer < len(instructions):

    if pointer in visited:
      loop = True
      break
    
    if instructions[pointer]['code'] == 'nop':
      next_instr = pointer + 1
    if instructions[pointer]['code'] == 'jmp':
      next_instr = pointer + instructions[pointer]['value']
    if instructions[pointer]['code'] == 'acc':
      accumulator += instructions[pointer]['value']
      next_instr = pointer + 1

    visited[pointer] = 1

    pointer = next_instr

  if not loop:
    print(accumulator)

for nj in nop_jmp:
  instr = copy.deepcopy(instructions)
  instr[nj]['code'] = 'nop' if instr[nj]['code'] == 'jmp' else 'jmp'
  brute_force(instr)
