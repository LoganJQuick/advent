directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def part_1(lines):
  starting_pos = [(i, j) for i, line in enumerate(lines) for j, c in enumerate(line) if c == 'S'][0]
  ending_pos = [(i, j) for i, line in enumerate(lines) for j, c in enumerate(line) if c == 'E'][0]
  direction = 3
  queue = [(starting_pos[0], starting_pos[1], direction, 0)]
  costs = {}
  while len(queue) > 0:
    i, j, dir, cost = queue.pop(0)
    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0]) or lines[i][j] == '#' or cost >= costs.get((i, j, dir), 10e13):
      continue
    costs[(i, j, dir)] = cost
    dir_i, dir_j = directions[dir]
    queue.append((i + dir_i, j + dir_j, dir, cost + 1))
    queue.append((i, j, (dir + 1) % 4, cost + 1000))
    queue.append((i, j, (dir - 1) % 4, cost + 1000))
  return min([costs[(ending_pos[0], ending_pos[1], i)] for i in range(4)])

def part_2(lines):
  starting_pos = [(i, j) for i, line in enumerate(lines) for j, c in enumerate(line) if c == 'S'][0]
  ending_pos = [(i, j) for i, line in enumerate(lines) for j, c in enumerate(line) if c == 'E'][0]
  direction = 3
  queue = [(starting_pos[0], starting_pos[1], direction, 0, set([(starting_pos[0], starting_pos[1])]))]
  cheapest_paths = {}
  costs = {}
  while len(queue) > 0:
    i, j, dir, cost, path = queue.pop(0)
    if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[0]) or lines[i][j] == '#' or cost > costs.get((i, j, dir), 10e13):
      continue
    if cost == costs.get((i, j, dir), 10e13) and len(path.intersection(cheapest_paths.get((i, j, dir), set()))) == len(path):
      continue
    if cost == costs.get((i, j, dir), 10e13):
      cheapest_paths[(i, j, dir)] = cheapest_paths[(i, j, dir)].union(path)
    else:
      cheapest_paths[(i, j, dir)] = path.union([(i, j)])
    costs[(i, j, dir)] = cost
    dir_i, dir_j = directions[dir]
    queue.append((i + dir_i, j + dir_j, dir, cost + 1, cheapest_paths[(i, j, dir)]))
    queue.append((i, j, (dir + 1) % 4, cost + 1000, cheapest_paths[(i, j, dir)]))
    queue.append((i, j, (dir - 1) % 4, cost + 1000, cheapest_paths[(i, j, dir)]))
  return sorted([(costs[(ending_pos[0], ending_pos[1], i)], len(cheapest_paths[(ending_pos[0], ending_pos[1], i)])) for i in range(4)])[0][1]

if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")

