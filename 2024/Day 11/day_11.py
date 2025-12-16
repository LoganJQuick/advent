def sim_splits(lines, num_splits):
  counts = {int(n):1 for n in lines[0].split()}
  for _ in range(num_splits):
    new_counts = dict()
    for num in counts:
      if num == 0:
        new_counts[1] = new_counts.get(1, 0) + counts[num]
      elif len(str(num)) % 2 == 0:
        digits = len(str(num))
        num_1, num_2 = int(str(num)[:digits // 2]), int(str(num)[digits // 2:])
        new_counts[num_1] = new_counts.get(num_1, 0) + counts[num]
        new_counts[num_2] = new_counts.get(num_2, 0) + counts[num]
      else:
        new_counts[num*2024] = new_counts.get(num*2024, 0) + counts[num]
    counts = new_counts
  return sum([counts[n] for n in counts])

def part_1(lines):
  return sim_splits(lines, 25)

def part_2(lines):
  return sim_splits(lines, 75)

if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")
  
