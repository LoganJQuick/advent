def get_adjacencies(lines):
  adjacencies = {}
  for line in lines:
    adjacencies[line.split(': ')[0]] = line.split(': ')[1].split()
  return adjacencies

def num_paths(adj, pos, goal):
  if pos == goal:
    return 1
  total = 0
  for neighbor in adj[pos]:
    total += num_paths(adj, neighbor, goal)
  return total

def num_paths_2(adj, start, goal):
  paths_by_source = {}
  queue = [start]
  paths_by_source[start] = {'start_point': 1}
  while len(queue) > 0:
    pos = queue.pop(0)
    if pos == 'out':
      continue
    ways_to_get = sum([paths_by_source[pos][neighbor] for neighbor in paths_by_source[pos]])
    for neighbor in adj[pos]:
      if paths_by_source.get(neighbor, {}).get(pos, 0) < ways_to_get:
        queue.append(neighbor)
        paths_by_source[neighbor] = paths_by_source.get(neighbor, {})
        paths_by_source[neighbor][pos] = ways_to_get
  if goal in paths_by_source:
    return sum([paths_by_source[goal][neighbor] for neighbor in paths_by_source[goal]])
  else:
    return 0
    

def part_1(lines):
  adj = get_adjacencies(lines)
  return num_paths_2(adj, 'you', 'out')

def part_2(lines):
  adj = get_adjacencies(lines)
  
  one = num_paths_2(adj, 'svr', 'fft') * num_paths_2(adj, 'fft', 'dac') * num_paths_2(adj, 'dac', 'out')
  two = num_paths_2(adj, 'svr', 'dac') * num_paths_2(adj, 'dac', 'fft') * num_paths_2(adj, 'fft', 'out')
  
  return one + two


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  test_lines_2 = [line.strip() for line in open('test_data_2.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines_2)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")