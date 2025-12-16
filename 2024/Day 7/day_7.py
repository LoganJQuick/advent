import re

def concat(a,b):
  return int(str(a) + str(b))

def add(a,b):
  return a+b

def prod(a,b):
  return a*b

def dp(target, curr, list, operations):
  if len(list) == 0:
    return target == curr
  return any([dp(target, operation(curr, list[0]), list[1:], operations) for operation in operations])

def part_1(lines):
  nums = [[int(n) for n in re.findall(r'\d+', line)] for line in lines]
  return sum([num_line[0] for num_line in nums if dp(num_line[0], num_line[1], num_line[2:], [add, prod])])

def part_2(lines):
  nums = [[int(n) for n in re.findall(r'\d+', line)] for line in lines]
  return sum([num_line[0] for num_line in nums if dp(num_line[0], num_line[1], num_line[2:], [add, prod, concat])])


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")