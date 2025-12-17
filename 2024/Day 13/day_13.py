import re
import numpy as np
from scipy.optimize import linprog


def get_optimal_presses(button_1, button_2, goal):
  det = button_1[0] * button_2[1] - button_1[1] * button_2[0]
  if det == 0:
      return 0
  a_num = goal[0] * button_2[1] - goal[1] * button_2[0]
  b_num = goal[1] * button_1[0] - goal[0] * button_1[1]
  if a_num % det != 0 or b_num % det != 0:
      return 0
  a = a_num // det
  b = b_num // det
  if a < 0 or b < 0:
      return 0
  return 3 * a + b



def part_1(lines):
  total = 0
  for i in range(0, len(lines), 4):
    button_1 = [int(n) for n in re.findall(r'\d+', lines[i])]
    button_2 = [int(n) for n in re.findall(r'\d+', lines[i+1])]
    goal = [int(n) for n in re.findall(r'\d+', lines[i+2])]
    total += get_optimal_presses(button_1, button_2, goal)
  return total

def part_2(lines):
  total = 0
  for i in range(0, len(lines), 4):
    button_1 = [int(n) for n in re.findall(r'\d+', lines[i])]
    button_2 = [int(n) for n in re.findall(r'\d+', lines[i+1])]
    goal = [int(n) + 10000000000000 for n in re.findall(r'\d+', lines[i+2])]
    total += get_optimal_presses(button_1, button_2, goal)
  return total



if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")

