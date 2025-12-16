def get_nodes(lines):
  nodes = dict()
  for i, line in enumerate(lines):
    for j, c in enumerate(line):
      if c != '.':
        nodes[c] = nodes.get(c, []) + [(i,j)]
  return nodes

def antinodes_in_bounds(antinodes, lines):
  return [(i,j) for (i,j) in antinodes if 0 <= i < len(lines) and 0 <= j < len(lines[0])]

def get_antinodes_one(lines):
  nodes = get_nodes(lines)
  antinodes = set()
  for c in nodes:
    for x, node_a in enumerate(nodes[c]):
      for node_b in nodes[c][x+1:]:
        diff_i, diff_j = node_a[0] - node_b[0], node_a[1] - node_b[1]
        antinodes.add((node_b[0] - diff_i, node_b[1] - diff_j))
        antinodes.add((node_a[0] + diff_i, node_a[1] + diff_j))
  return antinodes_in_bounds(antinodes, lines)

def get_antinodes_two(lines):
  nodes = get_nodes(lines)
  antinodes = set()
  for c in nodes:
    for x, node_a in enumerate(nodes[c]):
      for node_b in nodes[c][x+1:]:
        i = 0
        while 0 <= ((i+1)*node_b[0] - i*node_a[0]) < len(lines) and 0 <= ((i+1)*node_b[1] - i*node_a[1]) < len(lines[0]):
          antinodes.add(((i+1)*node_b[0] - i*node_a[0], (i+1)*node_b[1] - i*node_a[1]))
          i += 1
        i = 0
        while 0 <= ((i+1)*node_a[0] - i*node_b[0]) < len(lines) and 0 <= ((i+1)*node_a[1] - i*node_b[1]) < len(lines[0]):
          antinodes.add(((i+1)*node_a[0] - i*node_b[0], (i+1)*node_a[1] - i*node_b[1]))
          i += 1
  return antinodes


def part_1(lines):
  return len(get_antinodes_one(lines))

def part_2(lines):
  return len(get_antinodes_two(lines))


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")