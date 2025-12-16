directions = [(1,0), (-1,0), (0, 1), (0, -1)]

def peaks_reachable(x, y, grid, cache):
  if grid[x][y] == 9:
    return {(x, y)}
  ret = set()
  for i, j in directions:
    if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]) and grid[x+i][y+j] == grid[x][y] + 1:
      ret = ret.union(cache[x+i][y+j] or peaks_reachable(x+i, y+j, grid, cache))
  cache[x][y] = ret
  return ret

def num_peaks_reachable(x, y, grid, cache):
  if grid[x][y] == 9:
    return 1
  ret = 0
  for i, j in directions:
    if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]) and grid[x+i][y+j] == grid[x][y] + 1:
      ret += cache[x+i][y+j] or num_peaks_reachable(x+i, y+j, grid, cache)
  cache[x][y] = ret
  return ret

def part_2(lines):
  grid = [[int(n) for n in line] for line in lines]
  cache = [[None for _ in range(len(lines[0]))] for _ in range(len(lines))]
  total = 0
  for x in range(len(grid)):
    for y in range(len(grid)):
      num_peaks_reachable(x, y, grid, cache)
      total += cache[x][y] if grid[x][y] == 0 else 0
  return total

def part_1(lines):
  grid = [[int(n) for n in line] for line in lines]
  cache = [[None for _ in range(len(lines[0]))] for _ in range(len(lines))]
  total = 0
  for x in range(len(grid)):
    for y in range(len(grid)):
      peaks_reachable(x, y, grid, cache)
      total += len(cache[x][y]) if grid[x][y] == 0 else 0
  return total


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")
  
