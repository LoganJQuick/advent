import time
import numpy as np
from scipy.optimize import linprog

def get_inputs(lines):
  inputs = []
  for line in lines:
    lights = line[1:].split(']')[0]
    buttons = [frozenset([int(n) for n in txt.split(',')]) for txt in [text[:-1] for text in line.split(']')[1].split(' {')[0].split(' (')[1:]]]
    voltages = [int(n) for n in line.split('{')[1][:-1].split(',')]
    inputs.append((lights, buttons, voltages))
  return inputs
  
def combine_buttons(button_a, button_b):
  return button_a.union(button_b) - button_a.intersection(button_b)

def lights_to_bits(lights):
  return sum([2**(i) for i in range(len(lights)) if lights[i] == '#'])

def button_to_bits(button):
  return sum([2**(i) for i in button])

def part_1(lines):
  inputs = get_inputs(lines)
  presses = 0
  for lights, buttons, _ in inputs:
    lights = lights_to_bits(lights)
    buttons = [button_to_bits(button) for button in buttons]
    press_counts = dict.fromkeys(buttons, 1)
    while True:
      if lights in press_counts:
        presses += press_counts[lights]
        break
      for i, a in enumerate(buttons):
        for b in buttons[i:]:
          new_button = a ^ b
          new_button_presses = press_counts[a] + press_counts[b]
          if new_button not in press_counts:
            buttons.append(new_button)
          press_counts[new_button] = min(press_counts.get(new_button, 10**100), new_button_presses)
  return presses
  
def array_from_buttons(buttons, voltages):
  array = np.zeros((len(voltages), len(buttons)))
  for i, button in enumerate(buttons):
    for digit in button:
      array[digit][i] = 1
  return array

def part_2(lines):
  inputs = get_inputs(lines)
  presses = 0
  for _, buttons, voltages in inputs:
    A = array_from_buttons(buttons, voltages)  
    B = np.array(voltages)
    m = A.shape[1]
    c = np.ones(m)
    bounds = [(0, None)] * m
    res = linprog(c, A_eq=A, b_eq=B, bounds=bounds, method="highs", integrality=1)
    presses += res.x.sum()
    
  return int(presses)

if __name__ == "__main__":
  test_lines = [line.strip() for line in open('test_data.txt', 'r').readlines()]
  full_lines = [line.strip() for line in open('full_data.txt', 'r').readlines()]
  print(f"Part 1 with test data: {part_1(test_lines)}")
  print(f"Part 2 with test data: {part_2(test_lines)}\n")
  
  print(f"Part 1 with full data: {part_1(full_lines)}")
  print(f"Part 2 with full data: {part_2(full_lines)}")


