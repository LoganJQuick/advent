import re

def prod(list):
  product = 1
  for n in list:
    product *= n
  return product

def get_presents(lines):
  presents = []
  for i in range(6):
    box = lines[i*5+1:i*5+4]
    box = [(j,k) for j in range(len(box)) for k in range(len(box[j])) if box[j][k] == '#']
    presents.append(box)
  return presents


def part_1(lines):
  presents = get_presents(lines)
  numbers = [[int(n) for n in re.findall(r'\d+', line)] for line in lines[30:]]
  area = [[line[0], line[1]] for line in numbers]
  present_counts = [line[2:] for line in numbers]
  count = 0
  super_count = 0
  for i in range(len(numbers)):
    super_combined_area = sum([present_counts[i][j]*9 for j in range(len(presents))])
    combined_area = sum([len(presents[j])*present_counts[i][j] for j in range(len(presents))])
    space = area[i][0] * area[i][1]
    if combined_area < space:
      count += 1
    if super_combined_area <= space:
      super_count += 1
  return count, super_count
    


if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {part_1(test_lines)}")
  # print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  # print(f"Part 2 with full data: {part_2(full_lines)}")


