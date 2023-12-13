## Input ##
lines = open("inputs/day5.txt", 'r').readlines()
seeds = [int(n) for n in lines[0].split(":")[1].split()]
seeds2 = [n for n in seeds]

def parse_ranges(start_of_ranges):
    i = start_of_ranges + 1
    result = []
    while i < len(lines) and lines[i] != "\n":
        dest, source, length = [int(n) for n in lines[i].strip().split()]
        result.append(Ranges([dest, dest+length-1], [source, source+length-1]))
        i += 1
    return result

def get_ranges(lines):
    i = 1
    all_ranges = []
    while i < len(lines):
        line = lines[i]
        if line[0].isalpha():
            all_ranges.append(parse_ranges(i))
        i += 1
    return all_ranges

def map_num(num, ranges):
    for i in range(len(ranges)):
        if ranges[i].in_range(num):
            return ranges[i].map(num)
    return num
        
def in_seed_range(n):
    i = 0
    while i < len(part_2_seeds):
        if part_2_seeds[i] <= n < part_2_seeds[i]+part_2_seeds[i+1]:
            return True
        i += 2
    return False

class Ranges:
    source: [int]
    dest: [int]
    def __init__(self, dest, source):
        self.source = source
        self.dest = dest
    def in_source(self, n):
        return self.source[0] <= n <= self.source[1]
    def ranges_overlap(self, r2):
        return self.dest[0] <= r2.source[1] and r2.source[0] <= self.dest[1]
    def map(self, n):
        if self.in_source(n):
            return self.dest[0] + n - self.source[0]
        return n
    def divide_on_n(self, n):
        if self.dest[0] <= n <= self.dest[1]:
            ranges1 = Ranges([self.dest[0], n-1], [self.source[0], self.source[0] + n - self.dest[0]-1])
            ranges2 = Ranges([n, self.dest[1]], [self.source[0] + n - self.dest[0], self.source[1]])
            return [ranges1, ranges2]
        return [self]
    def compose_ranges(self, other):
        if not self.ranges_overlap(other):
            raise Exception()
        mid_lower = max(self.dest[0], other.source[0])
        mid_upper = min(self.dest[1], other.source[1])
        print(mid_lower)
        new_source_lower = self.source[0] + mid_lower - self.dest[0]
        new_source_upper = self.source[1] - self.dest[1] + mid_upper
        new_dest_lower = other.dest[0] + mid_lower - other.source[0]
        new_dest_upper = other.dest[1] - other.source[1] + mid_upper
        return Ranges([new_dest_lower, new_dest_upper], [new_source_lower, new_source_upper])
    def __str__(self):
        return f"[{self.source[0]}, {self.source[1]}] -> [{self.dest[0]}, {self.dest[1]}]"

def merge_ranges(r1, r2):
    i1, i2 = 0, 0
    r2.sort(key=lambda x: x.source[0])
    
def print_ranges(ranges):
    print([str(x) for x in ranges])

def get_part1_answer():
    rangess = get_ranges(lines)
    for ranges in rangess:
        seeds = [map_num(seed, ranges) for seed in seeds]
    return min(seeds)


rangess = get_ranges(lines)

ranges1 = rangess[0]
ranges2 = rangess[1]

ranges1.sort(key=lambda x: x.dest[0])
ranges2.sort(key=lambda x: x.source[0])
i, j = 0, 0
r1: Ranges = ranges1[i]
r2: Ranges = ranges2[i]
final = []
while i < len(ranges1) and j < len(ranges2):
    r1 = ranges1[i]
    r2 = ranges2[j]
    if r1.ranges_overlap(r2):
        new_r = r1.compose_ranges(r2)
        final.append(new_r)
    if r1.dest[1] < r2.source[1]:
        i += 1
    elif r2.source[1] < r1.dest[1]:
        j += 1
    else:
        i += 1
        j += 1

print_ranges(final)

ranges1 = Ranges([25, 44], [0, 15])
ranges2 = Ranges([80, 100], [30, 50])

print(ranges1.compose_ranges(ranges2))