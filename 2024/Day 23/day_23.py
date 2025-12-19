

def get_neighbors(lines):
  neighbors = {}
  for line in lines:
    neighbor_1, neighbor_2 = line.split('-')
    neighbors[neighbor_1] = neighbors.get(neighbor_1, set()).union(set([neighbor_2]))
    neighbors[neighbor_2] = neighbors.get(neighbor_2, set()).union(set([neighbor_1]))
  return neighbors

def maximal_clique(neighbors, nodes, banned_nodes):
  biggest = set(nodes)
  proposed_nodes = set(neighbors[nodes[0]])
  for node in nodes:
    proposed_nodes &= neighbors[node]
  proposed_nodes -= banned_nodes
  for node in proposed_nodes:
    new_clique = maximal_clique(neighbors, nodes + [node], banned_nodes)
    biggest = new_clique if len(new_clique) > len(biggest) else biggest
    banned_nodes.add(node)
  return biggest
  

def part_1(lines):
  neighbors = get_neighbors(lines)
  triplets = set()
  for node in neighbors:
    for neighbor in neighbors[node]:
      for shared in neighbors[node].intersection(neighbors[neighbor]):
        triplets.add(tuple(sorted([node, neighbor, shared])))
  return len([triplet for triplet in triplets if any([node[0] == 't' for node in triplet])])

def part_2(lines):
  neighbors = get_neighbors(lines)
  max_clique = set()
  for node in neighbors:
    new_clique = maximal_clique(neighbors, [node], set())
    max_clique = new_clique if len(new_clique) > len(max_clique) else max_clique
  return ','.join(sorted(list(max_clique)))


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")