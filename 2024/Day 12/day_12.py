directions = [(1,0), (-1,0), (0, 1), (0, -1)]

def get_region(x, y, grid):
  char = grid[x][y]
  region = set()
  queue = [(x,y)]
  while len(queue) > 0:
    i, j = queue.pop(0)
    if not (0 <= i < len(grid) and 0 <= j < len(grid[0])) or grid[i][j] != char or (i, j) in region:
      continue
    region.add((i, j))
    for m, n in directions:
      queue.append((i+m, j+n))
  return char, region

def get_regions(lines):
  regions = []
  seen = set()
  for i in range(len(lines)):
    for j in range(len(lines[0])):
      if (i, j) in seen:
        continue
      c, region = get_region(i, j, lines)
      seen = seen.union(region)
      regions.append((c, region))
  return regions

def get_edges(region):
  edges = []
  for x, y in region:
    for i, j in directions:
      if (x+i, y+j) not in region:
        edges.append((x, y, x+i, y+j))
  return edges

def get_adjacents(edge, dist):
  x_a, y_a, x_b, y_b = edge
  if x_a == x_b:
    return (x_a - dist, y_a, x_a - dist, y_b), (x_a + dist, y_a, x_a + dist, y_b)
  else:
    return (x_a, y_a - dist, x_b, y_a - dist), (x_a, y_a + dist, x_b, y_a + dist)

def get_sides(edges):
  seen = set()
  sides = []
  for edge in edges:
    if edge in seen:
      continue
    side = [edge]
    i = 1
    cont_1, cont_2 = True, True
    while cont_1 or cont_2:
      adj_1, adj_2 = get_adjacents(edge, i)
      if adj_1 in edges and cont_1 and adj_2 in edges and cont_2:
        side.append(adj_1)
        side.append(adj_2)
        seen.add(adj_1)
        seen.add(adj_2)
      elif adj_1 in edges and cont_1:
        cont_2 = False
        side.append(adj_1)
        seen.add(adj_1)
      elif adj_2 in edges and cont_2:
        cont_1 = False
        side.append(adj_2)
        seen.add(adj_2)
      else:
        cont_1, cont_2 = False, False
      i += 1
    sides.append(side)
  return sides
      

def get_region_cost(region):
  perimeter = 0
  for x, y in region:
    for i, j in directions:
      if (x+i, y+j) not in region:
        perimeter += 1
  return len(region) * perimeter

def part_1(lines):
  return sum([get_region_cost(region[1]) for region in get_regions(lines)])

def part_2(lines):
  return sum([len(get_sides(get_edges(region[1])))*len(region[1]) for region in get_regions(lines)])


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")
