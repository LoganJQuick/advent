directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def part_1(lines):
  count = 0
  for i in range(len(lines)):
    for j in range(len(lines)):
      for x,y in directions:
        word = ""
        for k in range(4):
          xi = i + x*k
          yj = j + y*k
          if 0 <= xi < len(lines) and 0 <= yj < len(lines[0]):
            word += lines[xi][yj]
        count += 1*(word == 'XMAS')
  return count

def part_2(lines):
  count = 0
  for i in range(len(lines)):
    for j in range(len(lines[0])):
      pos_diag = ""
      neg_diag = ""
      for k in [-1, 0, 1]:
        if 0 <= i+k < len(lines) and 0 <= j+k < len(lines[0]):
          pos_diag += lines[i+k][j+k]
        if 0 <= i+k < len(lines) and 0 <= j-k < len(lines[0]):
          neg_diag += lines[i+k][j-k]
      count += 1*((pos_diag == "SAM" or pos_diag == "MAS") and (neg_diag == "SAM" or neg_diag == "MAS"))
  return count



if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")