def prod(list):
  prod = 1
  for n in list:
    prod *= n
  return prod

def get_problems(lines):
  split_lines = [line.split() for line in lines]
  problems = []
  for i in range(len(split_lines[0])):
    numbers = []
    for split_line in split_lines[:-1]:
      numbers.append(int(split_line[i]))
    problems.append((split_lines[-1][i], numbers))
  return problems

def get_problems_two(lines):
  borders = [n for n in range(len(lines[-1])) if lines[-1][n] != ' '] + [len(lines[0])+1]
  problems = []
  for i in range(len(borders) - 1):
    numbers = []
    for j in range(borders[i], borders[i+1] - 1):
      number = ""
      for line in lines[:-1]:
        number += line[j]
      numbers.append(int(number))
    problems.append((lines[-1][borders[i]], numbers))
  return problems


def solve_problems(problems):
  total = 0
  for problem in problems:
    if problem[0] == '+':
      total += sum(problem[1])
    else:
      total += prod(problem[1])
  return total

def part_1(lines):
  return solve_problems(get_problems(lines))

def part_2(lines):
  return solve_problems(get_problems_two(lines))


if __name__ == "__main__":
  test_lines = [line[:-1] for line in open('test_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  full_lines = [line[:-1] for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")