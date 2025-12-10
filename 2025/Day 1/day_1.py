def part_1(lines):
  pos = 50
  moves = [(line[0], int(line[1:])) for line in lines]
  zeros = 0
  for dir, amt in moves:
    if dir == 'R':
      pos = (pos + amt) % 100
    else:
      pos = (pos - amt) % 100
    if pos == 0:
      zeros += 1
  return zeros

def part_2(lines):
  pos = 50
  moves = [(line[0], int(line[1:])) for line in lines]
  zeros = 0
  for dir, amt in moves:
    zeros += (amt // 100)
    amt = amt % 100
    if dir == 'R':
      zeros += 1 if pos != 0 and pos + amt > 100 else 0
      pos = (pos + amt) % 100
    else:
      zeros += 1 if pos != 0 and pos - amt < 0 else 0
      pos = (pos - amt) % 100
    if pos == 0:
      zeros += 1
  return zeros



if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")