with open('day23.txt', 'r') as f:
    lines = f.readlines()

import sys
import copy

dirs = ['N', 'S', 'W', 'E']

elf_pos = {}
positions = set()

k = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        if lines[i][j] == "#":
            elf_pos[k] = tuple([i, j])
            positions.add(tuple([i, j]))
            k += 1
            


def propose_dir(elf):
    pos = elf_pos[elf]
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (tuple([pos[0] + i, pos[1] + j]) in positions):
                count += 1
    if count == 1:
        return tuple([pos[0], pos[1]])
    for dir in dirs:
        if (dir == 'N' and not (tuple([pos[0] - 1, pos[1]]) in positions or tuple([pos[0] - 1, pos[1] - 1]) in positions or tuple([pos[0] - 1, pos[1] + 1]) in positions)):
            return tuple([pos[0] - 1, pos[1]])
        if (dir == 'S' and not (tuple([pos[0] + 1, pos[1]]) in positions or tuple([pos[0] + 1, pos[1] - 1]) in positions or tuple([pos[0] + 1, pos[1] + 1]) in positions)):
            return tuple([pos[0] + 1, pos[1]])
        if (dir == 'W' and not (tuple([pos[0], pos[1] - 1]) in positions or tuple([pos[0] - 1, pos[1] - 1]) in positions or tuple([pos[0] + 1, pos[1] - 1]) in positions)):
            return tuple([pos[0], pos[1] - 1])
        if (dir == 'E' and not (tuple([pos[0], pos[1] + 1]) in positions or tuple([pos[0] - 1, pos[1] + 1]) in positions or tuple([pos[0] + 1, pos[1] + 1]) in positions)):
            return tuple([pos[0], pos[1] + 1])
    return tuple([pos[0], pos[1]])

def propose_dirs():
    global elf_pos
    global positions
    prop_dirs = {}
    elf_prop = {}
    for i in range(0, len(elf_pos)):
        pd = propose_dir(i)
        if not pd in prop_dirs:
            prop_dirs[pd] = i
            elf_prop[i] = pd
        elif prop_dirs[pd] != -1: 
            elf_prop[i] = elf_pos[i]
            elf_prop[prop_dirs[pd]] = elf_pos[prop_dirs[pd]]
            prop_dirs[pd] = -1
        else:
            elf_prop[i] = elf_pos[i]
    elf_pos = {}
    positions = set()
    for i in range(0, len(elf_prop)):
        elf_pos[i] = elf_prop[i]
        positions.add(elf_prop[i])
    dirs.append(dirs.pop(0))


def run():
    global elf_pos
    old_elf_pos = {}
    for i in range(1, 11):
        propose_dirs()
    minx = sys.maxsize
    miny = sys.maxsize
    maxx = -sys.maxsize - 1
    maxy = -sys.maxsize - 1
    
    for elf in elf_pos:
        pos = elf_pos[elf]
        minx = min(minx, pos[0])
        miny = min(miny, pos[1])
        maxx = max(maxx, pos[0])
        maxy = max(maxy, pos[1])
    print(f"part 1: {((1 + maxx - minx) * (1 + maxy - miny)) - len(elf_pos)}")
    while(elf_pos != old_elf_pos):
        i += 1
        old_elf_pos = copy.deepcopy(elf_pos)
        propose_dirs()
    print(f"part 2: {i}")
    
run()
