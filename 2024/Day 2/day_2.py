def safe(list):
  direction = 1 if list[0] < list[1] else -1
  return all([-3 <= (list[i] - list[i+1]) * direction < 0 for i in range(len(list[:-1]))])

def part_1(lines):
  nums = [[int(n) for n in line.split()] for line in lines]
  return sum([safe(line) for line in nums])

def part_2(lines):
  nums = [[int(n) for n in line.split()] for line in lines]
  return sum([safe(line) or any([safe(line[:i] + line[i+1:]) for i in range(len(line))]) for line in nums])



if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")