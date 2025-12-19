import itertools as it
from functools import cache
import re
import time
import sys
sys.setrecursionlimit(2000)

number_keypad = {
  '7': (0, 0),
  '8': (0, 1),
  '9': (0, 2),
  '4': (1, 0),
  '5': (1, 1),
  '6': (1, 2),
  '1': (2, 0),
  '2': (2, 1),
  '3': (2, 2),
  None: (3, 0),
  '0': (3, 1),
  'A': (3, 2),
}

arrow_keypad = {
  None: (0, 0),
  '^': (0, 1),
  'A': (0, 2),
  '<': (1, 0),
  'v': (1, 1),
  '>': (1, 2)
}

directions_to_arrows = {
  (-1, 0): '^',
  (1, 0):  'v',
  (0, 1):  '>',
  (0, -1): '<'
}

global counter
counter = 0

def get_paths(key_1, key_2, keypad):
  keypad = arrow_keypad if keypad == 0 else number_keypad
  x_dist = keypad[key_2][0] - keypad[key_1][0]
  y_dist = keypad[key_2][1] - keypad[key_1][1]
  dir_x = -1 if x_dist < 0 else 0 if x_dist == 0 else 1
  dir_y = -1 if y_dist < 0 else 0 if y_dist == 0 else 1
  paths = [[(dir_x, 0)] * abs(x_dist) + [(0, dir_y)] * abs(y_dist), [(0, dir_y)] * abs(y_dist) + [(dir_x, 0)] * abs(x_dist)]
  return paths

@cache
def get_paths_minus_none(key_1, key_2, keypad):
  paths = get_paths(key_1, key_2, keypad)
  paths_to_none = get_paths(key_1, None, keypad)
  length = len(list(paths_to_none)[0])
  return list([path for path in paths if path[:length] not in paths_to_none])

@cache
def key_presses_two_keys(char_1, char_2, level, keypad):
  if level == 0:
    return len(''.join([directions_to_arrows[direction] for direction in get_paths_minus_none(char_1, char_2, keypad)[0]] + ['A']))
  paths = get_paths_minus_none(char_1, char_2, keypad)
  path_strings = ['A' + ''.join([directions_to_arrows[key] for key in path]) + 'A' for path in paths]
  best_pattern = 10e100
  for path in path_strings:
    kkey_presses = 0
    for i in range(len(path) - 1):
      kkey_presses += key_presses_two_keys(path[i], path[i+1], level - 1, 0)
    best_pattern = min(best_pattern, kkey_presses)
  return best_pattern

def key_presses(string, level):
  pattern = 0
  for i in range(len(string) - 1):
    pattern += key_presses_two_keys(string[i], string[i+1], level, 1)
  return pattern
  

def part_1(lines):
  return sum([int(re.search(r'\d+', line).group()) * key_presses('A' + line, 2) for line in lines])

def part_2(lines, level = 21):
  return sum([int(re.search(r'\d+', line).group()) * key_presses('A' + line, 25) for line in lines])




if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")