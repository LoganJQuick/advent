def get_ranges(lines):
  line = lines[0]
  ranges = [(int(a), int(b)) for a, b in [range.split('-') for range in line.split(',')]]
  return ranges

def find_invalids(lines, invalid_func):
  ranges = get_ranges(lines)
  invalids = 0
  for a,b in ranges:
    for i in range(a, b+1):
      if invalid_func(i):
        invalids += i
  return invalids

def invalid_one(i):
  str_i = str(i)
  length_str = len(str_i)
  return length_str % 2 == 0 and str_i[:length_str // 2] == str_i[length_str // 2:]

def invalid_two(i):
  str_i = str(i)
  length_str = len(str_i)
  for j in range(1, length_str // 2 + 1):
    if length_str % j == 0 and str_i == (str_i[:j]) * (length_str // j):
      return True
  return False


def part_1(lines):
  return find_invalids(lines, invalid_one)

def part_2(lines):
  return find_invalids(lines, invalid_two)


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")