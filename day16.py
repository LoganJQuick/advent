from collections import deque
import time
def update_direction(dir, tile):
    match (dir, tile):
        case (1,0), "\\":
            return [(0, 1)]
        case (0,1), "\\":
            return [(1, 0)]
        case (-1,0), "\\":
            return [(0, -1)]
        case (0,-1), "\\":
            return [(-1, 0)]
        case (1,0), "/":
            return [(0, -1)]
        case (0,1), "/":
            return [(-1, 0)]
        case (-1,0), "/":
            return [(0, 1)]
        case (0,-1), "/":
            return [(1, 0)]
        case (_,0), "-":
            return [(0, -1), (0,1)]
        case dir, "-":
            return [dir]
        case (0,_), "|":
            return [(1, 0), (-1,0)]
        case dir, "|":
            return [dir]
        case dir, _:
            return [dir]
              
def sim_lights(lines, start_pos = (0,0), start_dir = (0,1)):
    lines = [line.strip() for line in lines]
    lit_up = set([start_pos])
    visited_dir = set()
    Q = deque([(start_pos, start_dir)])
    while Q:
        pos, dir = Q.popleft()
        i, j = pos
        di, dj = dir
        if 0 <= i+di < len(lines) and 0 <= j+dj < len(lines[0]):
            lit_up.add((i+di,j+dj))
            new_pos = (i+di,j+dj)
            new_dirs = update_direction(dir, lines[i+di][j+dj])
            for new_dir in new_dirs:
                if (new_pos, new_dir) not in visited_dir:
                    Q.append((new_pos, new_dir))
                    visited_dir.add((new_pos, new_dir))
    return len(lit_up)


def part_2(lines):
    result = 0
    imax, jmax = len(lines)-1, len(lines[0])-1
    for i in range(len(lines)):
        result = max(result, sim_lights(lines, (i,0), (0,1)))
        result = max(result, sim_lights(lines, (i,jmax), (0,-1)))
    for j in range(len(lines)):
        result = max(result, sim_lights(lines, (0,j), (1,0)))
        result = max(result, sim_lights(lines, (imax,j), (-1,0)))
    return result



## Main ##  
if __name__ == "__main__":
    lines = open('inputs/day16.txt').readlines()
    print("Answer for Part 1")
    print(sim_lights(lines))
    start_time = time.time()
    print("Answer for Part 2")
    print(part_2(lines))
    print("--- %s seconds ---" % (time.time() - start_time))
