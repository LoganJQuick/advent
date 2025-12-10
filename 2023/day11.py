def get_empty_rows_cols(lines):
    empty_cols = set()
    empty_rows = set()  
    for i in range(len(lines)):
        empty = True
        for j in range(len(lines[0])-1):
            if lines[i][j] != '.':
                empty = False
                break
        if empty:
            empty_rows.add(i)

    for j in range(len(lines[0])):
        empty = True
        for i in range(len(lines)):
            if lines[i][j] != '.':
                empty = False
                break
        if empty:
            empty_cols.add(j)
    return (empty_rows, empty_cols)

def calculate_distance(start, end, expansion_ratio, empty_rows, empty_cols):
    y1, x1 = start
    y2, x2 = end
    dist = 0
    for i in range(min(y1,y2), max(y1,y2)):
        dist += expansion_ratio if i in empty_rows else 1
    for i in range(min(x1,x2), max(x1,x2)):
        dist += expansion_ratio if i in empty_cols else 1
    return dist

def get_galaxies(lines):
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i][j] == '#':
                galaxies.append((i,j))
    return galaxies

def get_total_dist(expansion_ratio, galaxies, empty_rows, empty_cols):
    total_dist = 0
    count = 0
    for i in range(len(galaxies)):
        for g2 in galaxies[i+1:]:
            count += 1
            dist = calculate_distance(galaxies[i], g2, expansion_ratio, empty_rows, empty_cols)
            total_dist += dist
    return total_dist

def get_answer(lines, part2=False):
    galaxies = get_galaxies(lines)
    empty_rows, empty_cols = get_empty_rows_cols(lines)
    return get_total_dist(2 if not part2 else 1000000, galaxies, empty_rows, empty_cols)




## Main ##  
if __name__ == "__main__":
    lines = open('inputs\day11.txt', 'r').readlines()
    print("Answer for Part 1")
    print(get_answer(lines))
    print("Answer for Part 2")
    print(get_answer(lines, True))
    