def get_locks_and_keys(lines):
  keys = []
  locks = []
  for i in range(0, len(lines), 8):
    if lines[i] == "#####":
      locks.append([len([lines[j][k] for j in range(i+1, i+6) if lines[j][k] == '#']) for k in range(5)])
    else:
      keys.append([len([lines[j][k] for j in range(i+1, i+6) if lines[j][k] == '#']) for k in range(5)])
    
  return locks, keys
    
    
def part_1(lines):
  count = 0
  locks, keys = get_locks_and_keys(lines)
  for lock in locks:
    for key in keys:
      count += all([lock[i] + key[i] < 6 for i in range(5)])
  return count
  

if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  # print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  # print(f"Part 2 with full data: {part_2(full_lines)}")