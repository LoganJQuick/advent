def get_rock_pos(lines):
    rock_pos = set()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'O':
                rock_pos.add((i,j))
    return rock_pos

def get_rock_after_move(rock_pos, rocks_pos, lines, dir):
    i, j = rock_pos
    di, dj = dir
    counter = 0
    i, j = i+di, j+dj
    while i >= 0 and j >= 0 and i < len(lines) and j < len(lines[0]) and lines[i][j] != '#':
        if (i,j) in rocks_pos:
            counter += 1
        i, j = i+di, j+dj
    
    return (i + (counter + 1)*-di, j + (counter + 1)*-dj)

def hash_rocks(rocks):
    return sum([i*100 + j for (i, j) in rocks])
    
    

def get_rock_vals(rock_pos, lines, directions=[(-1,0)], times=1):
    past_pos = {}
    i = 0
    while i < times:
        for dir in directions:
            new_rock_pos = set()
            for pos in rock_pos:
                new_pos = get_rock_after_move(pos, rock_pos, lines, dir)
                new_rock_pos.add(new_pos)
            rock_pos = new_rock_pos
        hash = hash_rocks(rock_pos)
        if hash in past_pos:
            loop = i - past_pos[hash]
            num_loops = (times - i) // loop
            i = i + num_loops*loop
            i += 1
            continue
        past_pos[hash] = i
        i += 1
    result = 0
    for pos in rock_pos:
        i, _ = pos
        result += len(lines) - i
    return result

def get_part1_answer(lines):
    rock_pos = get_rock_pos(lines)
    return get_rock_vals(rock_pos, lines)

def get_part2_answer(lines):
    rock_pos = get_rock_pos(lines)
    return get_rock_vals(rock_pos, lines, [(-1,0), (0,-1), (1, 0), (0, 1)], 1000000000)

## Main ##  
if __name__ == "__main__":
    lines = open('inputs/day14.txt').readlines()
    lines = [line.strip() for line in lines]
    print("Answer for Part 1:")
    print(get_part1_answer(lines))
    print("\nAnswer for Part 2")
    print(get_part2_answer(lines))