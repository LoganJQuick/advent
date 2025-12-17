import re
def quadrant(x, y, height, width):
  if x == width // 2 or y == height // 2:
    return 0
  return (2 if x > width // 2 else 1) + (2 if y > height // 2 else 0)

def get_counts(list):
  counts = dict()
  for n in list:
    counts[n] = counts.get(n, 0) + 1
  return counts

def part_1(lines, height, width):
  robots = [[int(n) for n in re.findall(r'-*\d+', line)] for line in lines]
  robots = [((a + c*100) % width, (b + d*100) % height) for (a,b,c,d) in robots]
  counts = get_counts([quadrant(i, j, height, width) for i, j in robots])
  return counts[1] * counts[2] * counts[3] * counts[4]


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines, 7, 11)}")
  # print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines, 103, 101)}")
  # print(f"Part 2 with full data: {part_2(full_lines)}")

