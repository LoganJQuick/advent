from collections import deque
def get_start_place(lines: list[str]):
    for i in range(len(lines)):
        if 'S' in lines[i]:
            return (i, lines[i].find('S'))

dirs = [(1,0), (0,1), (-1,0), (0,-1)]

def bfs(lines: str, target):
    seen = set()
    si, sj = get_start_place(lines)
    mi, mj = len(lines), len(lines[0])
    q = deque([(si, sj, 0)])
    while q:
        i, j, steps = q.popleft()
        if not (0 <= i < mi and 0 <= j < mj) or lines[i][j] =='#':
            continue
        if (i, j, steps) in seen or steps > target:
            continue
        seen.add((i, j, steps))
        for (di, dj) in dirs:
            q.append((i+di,j+dj,steps+1))
    return len([tile for tile in list(seen) if tile[2] == target])

def bfs2(lines: str, num_steps: int):
    seen = set()
    polarity = num_steps % 2
    si, sj = get_start_place(lines)
    mi, mj = len(lines), len(lines[0])
    q = deque([(si, sj, 0, 0, 0)])
    count = 0
    while q:
        i, j, sqi, sqj, steps = q.popleft()
        sqi += 1 if i >= mi else -1 if i < 0 else 0
        sqj += 1 if j >= mj else -1 if j < 0 else 0
        i = i % mi
        j = j % mj
        if lines[i][j] =='#' or (i, j, sqi, sqj) in seen or steps > num_steps:
            continue
        seen.add((i, j, sqi, sqj))
        count += 1 if steps % 2 == polarity else 0
        for (di, dj) in dirs:
            q.append((i+di,j+dj,sqi, sqj, steps+1))
    return count

def dist_to_edges(lines, start):
    seen = set()
    si, sj = start
    mi, mj = len(lines), len(lines[0])
    dists = [None, None, None, None]
    q = deque([(si, sj, 0)])
    while q:
        i, j, steps = q.popleft()
        if i < 0:
            dists[0] = (i, j, steps) if dists[0] is None else dists[0]
            continue
        if i == mi:
            dists[2] = (i, j, steps) if dists[2] is None else dists[2]
            continue
        if j < 0:
            dists[3] = (i, j, steps) if dists[3] is None else dists[3]
            continue
        if j == mj:
            dists[1] = (i, j, steps) if dists[1] is None else dists[1]
            continue
        if (i, j) in seen:
            continue
        seen.add((i, j))
        for (di, dj) in dirs:
            q.append((i+di,j+dj,steps+1))
    return dists

## Main ##  
if __name__ == "__main__":
    lines = [line.strip() for line in open('inputs/day21.txt').readlines()]
    start = get_start_place(lines)
    print(dist_to_edges(lines, start))