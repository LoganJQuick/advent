def biggest_digit(string, start, end):
  pos = 0
  biggest = '/'
  for i in range(start, end):
    c = string[i]
    if c > biggest:
      biggest = c
      pos = i
  return biggest, pos

def biggest_n_digit_number(line, n):
  length = len(line)
  min_pos = 0
  num = ''
  for i in range(n):
    c, pos = biggest_digit(line, min_pos, length-n+i+1)
    min_pos = pos + 1
    num += c
  return int(num)

def part_1(lines):
  return sum([biggest_n_digit_number(line, 2) for line in lines])

def part_2(lines):
  return sum([biggest_n_digit_number(line, 12) for line in lines])
  



if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")