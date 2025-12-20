def possible_pattern(pattern, towels):
  if pattern == '':
    return True
  for towel in towels:
    if pattern[:len(towel)] == towel and possible_pattern(pattern[len(towel):], towels):
      return True
  return False

def number_of_ways(pattern, towels, cache):
  if pattern in cache:
    return cache[pattern]
  if pattern == '':
    return 1
  total = 0
  for towel in towels:
    if pattern[:len(towel)] == towel:
      total += number_of_ways(pattern[len(towel):], towels, cache)
  cache[pattern] = total
  return total

def part_1(lines):
  towels = [towel for towel in lines[0].split(', ')]
  return sum([possible_pattern(pattern, towels) for pattern in lines[2:]])

def part_2(lines):
  towels = [towel for towel in lines[0].split(', ')]
  cache = {}
  return sum([number_of_ways(pattern, towels, cache) for pattern in lines[2:]])
    

if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  towels = [towel for towel in test_lines[0].split(', ')]
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  towels = [towel for towel in full_lines[0].split(', ')]
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")