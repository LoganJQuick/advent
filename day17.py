from heapq import heappop, heappush
import time

dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    
def djikstra(lines: list[str], min_dist, max_dist):
    visited = set()
    distances = {}
    pq = []
    heappush(pq, (0,0,0,-1))
    while pq:
        dist,i,j,wrong_dir = heappop(pq)
        if (i,j,wrong_dir) in visited:
            continue
        if i == len(lines)-1 and j == len(lines[0])-1:
            return dist
        visited.add((i,j,wrong_dir))
        for dir_i, dir in enumerate(dirs):
            if dir_i == wrong_dir or (dir_i+2) % 4 == wrong_dir:
                continue
            di,dj = dir
            new_dist = dist
            for x in range(1,max_dist+1):
                new_i, new_j = i+di*x, j+dj*x
                if new_i in range(len(lines)) and new_j in range(len(lines[0])):
                    new_dist += int(lines[new_i][new_j])
                    if x < min_dist:
                        continue
                    if new_dist < distances.get((new_i,new_j,dir,i), 1e10):
                        heappush(pq, (new_dist, new_i, new_j, dir_i))
                        distances[(new_i,new_j,dir,i)] = new_dist
    return distances
            
        
    



## Main ##  
if __name__ == "__main__":
    lines = [line.strip() for line in open('inputs/day17.txt').readlines()]
    start_time = time.time()
    print("Part 1 Answer")
    print(djikstra(lines, 0, 3))
    print("Part 2 Answer")
    print(djikstra(lines, 4, 10))
    print("--- %s seconds ---" % (time.time() - start_time))
    
    