from collections import deque
from matplotlib.path import Path
lines = open('inputs/day10.txt').readlines()
lines = [line.strip() for line in lines]
dirs = [(1,0), (0,1), (-1,0), (0,-1)]
pipes = {'|': (0,2), '-': (1,3), 'L': (1,2), 'J': (2,3), '7': (0,3), 'F': (0,1)}
lefts = {(1,0): (0,1), (0,1):(-1,0), (-1,0):(0,-1),(0,-1):(1,0)}

class Node:
    tag = None
    left = None
    right = None
    def __init__(self, tag: str):
        self.tag = tag
    
def valid_neighbor(dir, neighbor):
    if dir == 0:
        return neighbor in ['|', 'L', 'J']
    if dir == 1:
        return neighbor in ['-', 'J', '7']
    if dir == 2:
        return neighbor in ['|', '7', 'F']
    if dir == 3:
        return neighbor in ['-', 'L', 'F']
    
def bfs(starting_pos):
    i, j = starting_pos
    neighbors = []
    for n in range(len(dirs)):
        x,y = dirs[n]
        neighbor = lines[i+x][j+y]
        if valid_neighbor(n, neighbor):
            neighbors.append((i+x, j+y))
    seen = {starting_pos, neighbors[0], neighbors[1]}
    q = deque(neighbors)
    curr = None
    forward_path, back_path = [neighbors[0]], [neighbors[1]]
    forward = True
    while q:
        curr = q.popleft()
        i,j = curr
        next_dirs = [dirs[i] for i in pipes[lines[i][j]]]
        for m,n in next_dirs:
            if (i+m,j+n) not in seen:
                seen.add((i+m,j+n))
                q.append((i+m,j+n))
                if forward:
                    forward_path.append((i+m,j+n))
                else:
                    back_path.append((i+m,j+n))
                forward = not forward
    back_path.reverse()
    path = [starting_pos] + forward_path + back_path
    return path
    
def get_start():
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'S':
                return (i,j)

def get_region(point, loop_points):
    region = set([point])
    neighbors = []
    i, j = point
    for x,y in dirs:
        neighbors.append((i+x,j+y))
    q = deque(neighbors)
    while q:
        curr = q.popleft()
        i,j = curr
        if curr in loop_points or curr in region or i < 0 or j < 0 or i >= len(lines) or j >= len(lines[0]):
            continue
        region.add(curr)
        for x,y in dirs:
            q.append((i+x,j+y))
    return region

starting_pos = get_start()
print("Answer for Part 1")
path = bfs(starting_pos)
print(int((len(path)) / 2))
loop_points = set(path)
outside = set([(i,j) for i in range(len(lines)) for j in range(len(lines[0])) if (i,j) not in loop_points])

p = Path(path)
enclosed = set()
for (i,j) in outside:
        if (i,j) not in loop_points and (i,j) not in enclosed and p.contains_point((i,j)):
            enclosed = enclosed.union(get_region((i,j), loop_points))
print(len(enclosed))


exit()
## Main ##  
if __name__ == "__main__":
    lines = open('inputs/day10.txt').readlines()
    print("Answer for Part 1")
    print("\nAnswer for Part 2")