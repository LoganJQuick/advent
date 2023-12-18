from collections import deque
import time
dirs = {'D': (1,0), 'R': (0,1), 'U':(-1,0), 'L': (0,-1)}

def decode_hex(hex):
    match hex[-1]:
        case '0':
            dir = 'R'
        case '1':
            dir = 'D'
        case '2':
            dir = 'L'
        case '3':
            dir = 'U'
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

def add_tuple(t1, t2):
    t11, t12 = t1
    t21, t22 = t2
    return (t11+t21,t12+t22)

def bfs_fill(start, curve):
    seen = set()
    q = deque([start])
    while q:
        curr = q.popleft()
        if curr in seen or curr in curve:
            continue
        i, j = curr
        seen.add(curr)
        for dir in dirs.values():
            di, dj = dir
            q.append((i+di,j+dj))
    return len(seen)

def get_curve(lines):
    point = (0,0)
    curve = set()
    for line in lines:
        dir_symbol, count, _ = line
        dir = dirs[dir_symbol]
        for _ in range(count):
            point = add_tuple(point, dir)
            curve.add(point)
    return curve
        
        
def draw_picture(curve, lower, upper):
    picture = []
    for i in range(lower,upper):
        curr = ""
        for j in range(lower,upper):
            if (i,j) in curve:
                curr += "#"
            else:
                curr += "."
        picture.append(curr)
    for line in picture:
        print(line)

def get_part1_answer(lines):
    curve = get_curve(parse_input(lines))
    return bfs_fill((1,1), curve) + len(curve)

def get_part2_answer(lines):
    new_lines = []
    for line in parse_input(lines):
        _, _, hex = line
        new_lines.append(decode_hex(hex))
    curve = get_curve(new_lines)
    return bfs_fill((1,1), curve) + len(curve)
    

## Main ##  
if __name__ == "__main__":
    lines = [line.strip() for line in open('inputs/day18.txt').readlines()]
    start_time = time.time()
    print("Part 1 Answer")
    print(get_part1_answer(lines))
    print("Part 2 Answer")
    print(get_part2_answer(lines))
    
