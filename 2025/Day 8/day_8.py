import math

NUMBER_OF_CONNECTIONS = 1000

def get_positions(lines):
  return [(int(x), int(y), int(z)) for x, y, z in [line.split(',') for line in lines]]

def calculate_distance(position1, position2):
  return math.sqrt((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2 + (position1[2] - position2[2]) ** 2)

def get_distances(lines):
  distances = []
  positions = get_positions(lines)
  for i, position1 in enumerate(positions):
    for position2 in positions[i+1:]:
      distances.append((calculate_distance(position1, position2), position1, position2))
  return distances

def distances_sorted(lines):
  return sorted(get_distances(lines), key=lambda distance: distance[0])

def get_adjacencies(lines, num_connections):
  connections = distances_sorted(lines)[:num_connections]
  adjacencies = dict()
  for connection in connections:
    adjacencies[connection[1]] = adjacencies.get(connection[1], []) + [connection[2]]
    adjacencies[connection[2]] = adjacencies.get(connection[2], []) + [connection[1]]
  return adjacencies

def get_circuits(lines, num_connections):
  adjacencies = get_adjacencies(lines, num_connections)
  visited = set()
  circuits = []
  for adjacency in adjacencies:
    if adjacency in visited:
      continue
    visited.add(adjacency)
    circuit = [adjacency]
    queue = adjacencies[adjacency]
    while len(queue) > 0:
      curr = queue.pop()
      if curr in visited:
        continue
      visited.add(curr)
      circuit.append(curr)
      queue = queue + adjacencies[curr]
    circuits.append(circuit)
  return circuits

def longest_three_circuits(lines, num_connections):
  return sorted([len(l) for l in get_circuits(lines, num_connections)], reverse=True)[:3]
      
def prod(nums):
  ret = 1
  for num in nums:
    ret *= num
  return ret

def get_last_connection(lines):
  num_points = len(lines)
  connections = distances_sorted(lines)
  circuits = []
  circuit_map = dict()
  for connection in connections:
    if connection[1] not in circuit_map and connection[2] in circuit_map:
      circuit_map[connection[1]] = circuit_map[connection[2]]
      circuits[circuit_map[connection[1]]].add(connection[1])
    elif connection[2] not in circuit_map and connection[1] in circuit_map:
      circuit_map[connection[2]] = circuit_map[connection[1]]
      circuits[circuit_map[connection[2]]].add(connection[2])
    elif connection[1] in circuit_map and connection[2] in circuit_map:
      circuits[circuit_map[connection[1]]] = circuits[circuit_map[connection[1]]].union(circuits[circuit_map[connection[2]]])
      for position in circuits[circuit_map[connection[2]]]:
        circuit_map[position] = circuit_map[connection[1]]
    else:
      circuit_map[connection[1]] = len(circuits)
      circuit_map[connection[2]] = len(circuits)
      circuits.append(set([connection[1], connection[2]]))
    if len(circuits[circuit_map[connection[1]]]) == num_points:
      return connection[1][0] * connection[2][0]
  return -1
      


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {prod(longest_three_circuits(test_lines, 10))}")
  print(f"Part 2 with test data: {get_last_connection(test_lines)}\n")
  
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with full data: {prod(longest_three_circuits(full_lines, 1000))}")
  print(f"Part 2 with full data: {get_last_connection(full_lines)}")