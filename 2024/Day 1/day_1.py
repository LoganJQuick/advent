def part_1(lines):
  left = sorted([int(line.split()[0]) for line in lines])
  right = sorted([int(line.split()[1]) for line in lines])
  return sum([abs(right[i] - left[i]) for i in range(len(left))])

def part_2(lines):
  left = [int(line.split()[0]) for line in lines]
  right = [int(line.split()[1]) for line in lines]
  right_counts = {n:right.count(n) for n in right}
  return sum([l*right_counts.get(l, 0) for l in left])


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")