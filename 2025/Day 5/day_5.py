def get_ranges(lines):
  pos = 0
  ranges = []
  while len(lines[pos]) > 0:
    ranges.append([int(n) for n in lines[pos].split('-')])
    pos += 1 
  return ranges, pos

def get_fresh(lines):
  ranges, start_pos = get_ranges(lines)
  pos = start_pos + 1
  fresh = []
  while pos < len(lines):
    curr = int(lines[pos])
    for range in ranges:
      if range[0] <= curr <= range[1]:
        fresh.append(curr)
        break
    pos += 1
  return len(fresh)

def union_ranges(ranges):
  ranges = sorted(ranges, key=lambda range: range[0])
  unioned_ranges = []
  curr_min, curr_max = ranges[0]
  pos = 0
  while pos < len(ranges):
    curr = ranges[pos]
    if curr[0] <= curr_max:
      curr_max = max(curr_max, curr[1])
    else:
      unioned_ranges.append([curr_min, curr_max])
      curr_min, curr_max = curr
    pos += 1
  unioned_ranges.append([curr_min, curr_max])
  return unioned_ranges

def sum_of_ranges(lines):
  ranges, _ = get_ranges(lines)
  ranges = union_ranges(ranges)
  total = 0
  for range in ranges:
    total += range[1] - range[0] + 1
  return total




if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {get_fresh(test_lines)}")
  print(f"Part 2 with test data: {sum_of_ranges(test_lines)}\n")
  
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with full data: {get_fresh(full_lines)}")
  print(f"Part 2 with full data: {sum_of_ranges(full_lines)}")