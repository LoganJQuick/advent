def part_1(lines):
  line = lines[0]
  positions = []
  for i, c in enumerate(line):
    if i % 2 == 0:
      positions += [[i // 2] * int(c)]
    else:
      positions += [[None] * int(c)]
  positions = [c for group in positions for c in group]
  front, back = 0, len(positions) - 1
  while front < back:
    if positions[front] is not None:
      front += 1
    elif positions[back] is None:
      back -= 1
    else:
      positions[front] = positions[back]
      positions[back] = None
  return sum([i*positions[i] for i in range(len(positions)) if positions[i] is not None])

def part_2(lines):
  line = lines[0]
  positions = [(i//2, int(line[i])) if i % 2 == 0 else (None, int(line[i])) for i in range(len(line))]
  i = len(positions) - 1
  while i >= 0:
    value, size = positions[i]
    if value is None:
      i -= 1
      continue
    for j in range(i):
      curr_val, curr_size = positions[j]
      if curr_val is None and curr_size >= size:
        positions[j] = (None, curr_size - size)
        positions[i] = (None, size)
        positions.insert(j, (value, size))
        i += 1
        break
    i -= 1 
  return sum([i*val for i, val in enumerate([c for val, size in positions for c in [val]*size]) if val is not None])




if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")
  
