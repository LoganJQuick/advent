directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(lines, size, bytes):
  barriers = set((int(a), int(b)) for a, b in [line.split(',') for line in lines[:bytes+1]])
  steps = {(0, 0): 0}
  queue = [(0, 0)]
  while len(queue) > 0:
    x, y = queue.pop(0)
    if x < 0 or x > size or y < 0 or y > size or (x, y) in barriers:
      continue
    for i, j in directions:
      if (x+i, y+j) not in steps:
        steps[(x+i, y+j)] = steps[(x, y)] + 1
        queue.append((x+i, y+j))
  return steps[(size, size)] if (size, size) in steps else None


def part_1(lines, size=70, bytes=1024):
  return bfs(lines, size, bytes)

def part_2(lines, size=70):
  barriers = [(int(a), int(b)) for a, b in [line.split(',') for line in lines]]
  bottom, top = 0, len(barriers)
  while bottom < top:
    i = (bottom + top) // 2
    if bfs(lines, size, i) is None:
      top = i
    else:
      bottom = i + 1
  return f"{barriers[bottom][0]},{barriers[bottom][1]}"
    

if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines, size=6, bytes=12)}")
  print(f"Part 2 with test data: {part_2(test_lines, size=6)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")


