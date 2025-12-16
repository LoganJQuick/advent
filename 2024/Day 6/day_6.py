directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def walk_until_out_or_loop(lines):
  for i in range(len(lines)):
    if '^' in lines[i]:
      pos = (i, lines[i].index('^'))
  i, j = pos
  direction = 0
  seen = set()
  place_and_direction = set()
  while 0 <= i < len(lines) and 0 <= j < len(lines[0]) and (i, j, direction) not in place_and_direction:
    seen.add((i,j))
    place_and_direction.add((i, j, direction))
    n,m = directions[direction]
    if 0 <= i+n < len(lines) and 0 <= j+m < len(lines[0]) and lines[i+n][j+m] == '#':
      direction = (direction + 1) % len(directions)
    else:
      i = i+n
      j = j+m
  out = not (0 <= i < len(lines) and 0 <= j < len(lines[0]))
  return seen, out

def part_1(lines):
  seen, _ = walk_until_out_or_loop(lines)
  return len(seen)

def part_2(lines):
  seen, _ = walk_until_out_or_loop(lines)
  count_loops = 0
  for (i, j) in seen:
    if lines[i][j] == '^':
      continue
    lines[i][j] = '#'
    _, out = walk_until_out_or_loop(lines)
    count_loops += not out
    lines[i][j] = '.'
  return count_loops

if __name__ == "__main__":
  test_lines = [list(line.strip()) for line in open('test_data.txt', 'r').readlines()]
  full_lines = [list(line.strip()) for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")