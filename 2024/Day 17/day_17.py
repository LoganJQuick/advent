def get_registers(lines):
  registers = {}
  for i in range(3):
    _, b, c = lines[i].split()
    registers[b[0]] = int(c)
  return registers

def get_instructions(lines):
  return [int(n) for n in lines[-1].split()[1].split(',')]

def combo_operand(registers, operand):
  if operand in range(4):
    return operand
  elif operand == 4:
    return registers['A']
  elif operand == 5:
    return registers['B']
  elif operand == 6:
    return registers['C']
  else:
    raise Exception()
  
def run_program(registers, instructions):
  pointer = 0
  out = ""
  while pointer < len(instructions) - 1:
    match instructions[pointer]:
      case 0:
        op = combo_operand(registers, instructions[pointer+1])
        registers['A'] = registers['A'] // (2 ** op)
        pointer += 2
      case 1:
        registers['B'] = registers['B'] ^ instructions[pointer+1]
        pointer += 2
      case 2:
        op = combo_operand(registers, instructions[pointer+1])
        registers['B'] = op % 8
        pointer += 2
      case 3:
        if registers['A'] == 0:
          pointer += 2
        else:
          pointer = instructions[pointer+1]
      case 4:
        registers['B'] = registers['B'] ^ registers['C']
        pointer += 2
      case 5:
        op = combo_operand(registers, instructions[pointer+1])
        out += str(op % 8) + ','
        pointer += 2
      case 6:
        op = combo_operand(registers, instructions[pointer+1])
        registers['B'] = registers['A'] // (2 ** op)
        pointer += 2
      case 7:
        op = combo_operand(registers, instructions[pointer+1])
        registers['C'] = registers['A'] // (2 ** op)
        pointer += 2
  return out[:-1]

def part_1(lines):
  registers = get_registers(lines)
  instructions = get_instructions(lines)
  return run_program(registers, instructions)

def part_2(lines):
  registers = get_registers(lines)
  instructions = get_instructions(lines)
  instruction_str = lines[-1].split()[1]
  out = ""
  i = 0
  digits = 1
  while True:
    registers['A'] = i
    out = run_program(registers, instructions)
    if instruction_str == out:
      return i
    elif instruction_str[(-2*digits+1):] == out[-2*digits+1:]:
      i *= 8
      digits += 1
    else:
      i += 1
  return i
    
  
        
  

if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")



"""
47910079998866
1461985568
"""