from collections import deque
import numpy as np
import time
dirs = {'D': (1,0), 'R': (0,1), 'U':(-1,0), 'L': (0,-1)}
dir_symbols = ['R', 'D', 'L', 'U']
def decode_hex(hex):
    dir = dir_symbols[int(hex[-1])]
    count = int(hex[1:6], base=16)
    return [dir, count, '']

def parse_input(lines: list[str]):
    result = []
    for line in lines:
        dir = line.split()[0]
        count = int(line.split()[1])
        serial = line.split()[2][1:-1]
        result.append([dir, count, serial])
    return result

def get_curve(lines):
    i, j = 0, 0
    edges = 0
    area = 0
    for line in lines:
        dir_symbol, count, _ = line
        di, dj = dirs[dir_symbol]
        di, dj = di*count, dj*count
        i, j = i+di, j+dj
        edges += count
        area += j*di
    return int(area + edges/2 + 1)

def get_part1_answer(lines):
    return get_curve(parse_input(lines))

def get_part2_answer(lines):
    new_lines = []
    for line in parse_input(lines):
        _, _, hex = line
        new_lines.append(decode_hex(hex))
    return get_curve(new_lines)
    

## Main ##  
if __name__ == "__main__":
    lines = [line.strip() for line in open('inputs/day18.txt').readlines()]
    start_time = time.time()
    print("Part 1 Answer")
    print(get_part1_answer(lines))
    print("Part 2 Answer")
    print(get_part2_answer(lines))
    
