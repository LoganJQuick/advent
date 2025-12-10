directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]

def valid_roll(lines, pos):
  count = 0
  x, y = pos
  for a, b in directions:
    if 0 <= x + a < len(lines) and 0 <= y + b < len(lines[0]) and lines[x+a][y+b] == '@':
      count += 1
  return count < 4

def num_valid_rolls(lines):
  count = 0
  for x in range(len(lines)):
    for y in range(len(lines[0])):
      if lines[x][y] == '@' and valid_roll(lines, (x, y)):
        count += 1
  return count
  
def num_valid_rolls_two(lines):
  curr_count = -1
  total_count = 0
  while curr_count != 0:
    curr_count = 0
    for x in range(len(lines)):
      for y in range(len(lines[0])):
        if lines[x][y] == '@' and valid_roll(lines, (x,y)):
          curr_count += 1
          lines[x][y] = '.'
    total_count += curr_count
  return total_count


if __name__ == "__main__":
  test_lines = [list(line.strip()) for line in open('test_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {num_valid_rolls(test_lines)}")
  print(f"Part 2 with test data: {num_valid_rolls_two(test_lines)}\n")
  
  full_lines = [list(line.strip()) for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with full data: {num_valid_rolls(full_lines)}")
  print(f"Part 2 with full data: {num_valid_rolls_two(full_lines)}")