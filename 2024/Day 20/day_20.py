directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def distances(lines):
  start = [(i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] == 'S'][0]
  end = [(i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] == 'E'][0]
  
  distances_from_start = {}
  queue = [(start, 0)]
  while len(queue) > 0:
    (x, y), dist = queue.pop(0)
    if x < 0 or x >= len(lines) or y < 0 or y > len(lines[0]) or lines[x][y] == '#' or (x, y) in distances_from_start:
      continue
    distances_from_start[(x, y)] = dist
    for (i, j) in directions:
      queue.append(((x+i, y+j), distances_from_start[(x, y)] + 1))
  distances_from_end = {}
  queue = [(end, 0)]
  while len(queue) > 0:
    (x, y), dist = queue.pop(0)
    if x < 0 or x >= len(lines) or y < 0 or y > len(lines[0]) or lines[x][y] == '#' or (x, y) in distances_from_end:
      continue
    distances_from_end[(x, y)] = dist
    for (i, j) in directions:
      queue.append(((x+i, y+j), distances_from_end[(x, y)] + 1))
  return distances_from_start, distances_from_end, distances_from_start[end]

def valid_shortcuts(lines, distances_start, distances_end, shortcut_distance, max_time):
  sorted_from_start = sorted([(i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] != '#'], key=lambda pos: distances_start[(pos[0], pos[1])])
  sorted_from_end = sorted([(i, j) for i in range(len(lines)) for j in range(len(lines[0])) if lines[i][j] != '#'], key=lambda pos: distances_end[(pos[0], pos[1])])
  count = 0
  for (x, y) in sorted_from_start:
    for (m, n) in sorted_from_end:
      if distances_start[(x, y)] + distances_end[(m, n)] > max_time:
        break
      dist = abs(x - m) + abs(y - n)
      if dist <= shortcut_distance and distances_start[(x, y)] + distances_end[(m, n)] + dist <= max_time:
        count += 1
  return count
        

def part_1(lines):
  distances_start, distances_end, time = distances(lines)
  return valid_shortcuts(lines, distances_start, distances_end, 2, time - 100)
  
def part_2(lines):
  distances_start, distances_end, time = distances(lines)
  return valid_shortcuts(lines, distances_start, distances_end, 20, time - 100)


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {part_1(test_lines)}")
  # print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")