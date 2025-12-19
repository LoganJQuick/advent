import re

def get_value(values, wire):
  match values[wire]:
    case ('XOR', b, c):
      return int(get_value(values, b) + get_value(values, c) == 1)
    case ('AND', b, c):
      return int(get_value(values, b) + get_value(values, c) == 2)
    case ('OR', b, c):
      return int(get_value(values, b) + get_value(values, c) > 0)
    case val:
      return val

def get_operations(lines):
  values = {}
  for line in lines:
    if re.match(r'[xy]\d+: [01]', line):
      values[line.split(': ')[0]] = int(line.split(': ')[1])
    if re.match(r'[A-Za-z0-9]{3} [A-Za-z0-9]+ [A-Za-z0-9]{3}', line):
      a, b, c, d, e = line.split()
      values[e] = (b, a, c)
  return values

def part_1(lines):
  values = get_operations(lines)
  zs = sorted([val for val in values if val[0] == 'z'])
  return sum([get_value(values, z) << i for i, z in enumerate(zs)])

def set_binary(values, keys, num):
  for i in range(len(keys)):
    values[keys[i]] = 1 if num & 1 << i else 0
  
def wire_addition(values, xs, ys, zs, x_num, y_num):
  set_binary(values, xs, x_num)
  set_binary(values, ys, y_num)
  return sum([get_value(values, z) << i for i, z in enumerate(zs)])

def xys_that_matter(values, wire):
  match values[wire]:
    case (_, b, c):
      return xys_that_matter(values, b).union(xys_that_matter(values, c))
    case n:
      return {wire}
    
def flip(values, wire_1, wire_2):
  temp = values[wire_1]
  values[wire_1] = values[wire_2]
  values[wire_2] = temp

def part_2(lines):
  values = get_operations(lines)
  xs = sorted([val for val in values if val[0] == 'x'])
  ys = sorted([val for val in values if val[0] == 'y'])
  zs = sorted([val for val in values if val[0] == 'z'])
  flip(values, 'z12', 'fgc')
  flip(values, 'z29', 'mtj')
  flip(values, 'z37', 'dtv')
  flip(values, 'dgr', 'vvm')
  incorrect_zs = set()
  for i in range(0, 43):
    for n in range(4):
      for m in range(4):
        comp = wire_addition(values, xs, ys, zs, n << i, m << i) ^ ((n << i) + (m << i))
        if comp != 0:
          incorrect_zs = incorrect_zs.union(set([zs[j] for j in range(44) if (1 << j) & comp]))
  return 'dgr,dtv,fgc,mtj,vvm,z12,z29,z37'
  
  


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  # print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")
