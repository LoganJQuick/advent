## Input ##
lines = open("day3.txt", 'r').readlines()
lines = list(map(lambda x: x.strip(), lines))
dirs = [(n, m) for n in [1,0,-1] for m in [1,0,-1]]


## Classes ##
class Number:
    start_col: int
    end_col: int
    row: int
    val: int
    def __init__(self, start_col, end_col, row) -> None:
        self.start_col = start_col
        self.end_col = end_col
        self.row = row

    def overlap(self, num):
        return num.row == self.row and num.start_col <= self.end_col and self.start_col <= num.end_col

class Number_List:
    List: [Number]

    def __init__(self) -> None:
        self.List = []

    def add(self, Number: Number):
        for num in self.List:
            if num.overlap(Number):
                return
        self.List.append(Number)


## Functions ##
def process_symbols():
    symbols = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != '.' and not c.isdigit():
                if c not in symbols:
                    symbols[c] = []
                symbols[c].append((i, j))
    return symbols

def get_adj_nums(i, j):
    result = Number_List()
    for m, n in dirs:
        if lines[i+m][j+n].isdigit():
            result.add(get_num(i+m, j+n))
    return result.List

def get_num(i, j):
    k1, k2 = j, j
    while k1 >= 0 and lines[i][k1].isdigit():
        k1 -= 1
    while k2 < len(lines[i]) and lines[i][k2].isdigit():
        k2 += 1
    result = Number(k1+1, k2-1, i)
    result.val = int(lines[i][k1+1:k2])
    return result

def get_part1_answer(symbols):
    total = 0
    for symbol in symbols:
        for i, j in symbols[symbol]:
            adj_nums = get_adj_nums(i, j)
            for num in adj_nums:
                total += num.val
    return total

def get_part2_answer(symbols):
    total = 0
    for i,j in symbols['*']:
        adj = get_adj_nums(i, j)
        if len(adj) == 2:
            total += adj[0].val*adj[1].val
    return total


## Answers ##
symbols = process_symbols()
print("Part 1 Answer")
print(get_part1_answer(symbols))
print("Part 2 Answer")
print(get_part2_answer(symbols))