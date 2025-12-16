import re

def part_1(lines):
  return sum([sum([a*b for a, b in [map(int, re.findall(r"\d+", s)) for s in re.findall(r'mul\([0-9]+,[0-9]+\)', line)]]) for line in lines])

def part_2(lines):
  instructions = [s for line in lines for s in re.findall(r"mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)", line)]
  total = 0
  enabled = True
  for instruction in instructions:
    match instruction:
      case "don't()": enabled = False
      case "do()": enabled = True
      case _: 
        a, b = re.findall(r"\d+", instruction)
        total += enabled*int(a)*int(b)
  return total


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")