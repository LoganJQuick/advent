## Input ##
lines = open("inputs/day5.txt", 'r').readlines()
seeds = [int(n) for n in lines[0].split(":")[1].split()]
part_2_seeds = [n for n in seeds]


def map_num(num, start_of_ranges):
    i = start_of_ranges + 1
    while i < len(lines) and lines[i] != "\n":
        dest, source, length = [int(n) for n in lines[i].strip().split()]
        if source <= num < source + length:
            return dest + (num - source)
        i += 1
    return num

def get_ranges(start_of_ranges):
    i = start_of_ranges + 1
    result = []
    while i < len(lines) and lines[i] != "\n":
        dest, source, length = [int(n) for n in lines[i].strip().split()]
        result.append(([dest, dest+length], [source, source+length]))
        i += 1
    return result

def map_with_range_reverse(num, ranges):
    for source_range, dest_range in ranges:
        if source_range[0] <= num < source_range[1]:
            return dest_range[0] + (num - source_range[0])
    return num
        
def in_seed_range(n):
    i = 0
    while i < len(part_2_seeds):
        if part_2_seeds[i] <= n < part_2_seeds[i]+part_2_seeds[i+1]:
            return True
        i += 2
    return False

i = 1
all_ranges = []
while i < len(lines):
    line = lines[i]
    if line[0].isalpha():
        for j, seed in enumerate(seeds):
            seeds[j] = map_num(seed, i)
    if line[0].isalpha():
        all_ranges.append(get_ranges(i))
    i += 1
    

    
print(min(seeds))

all_ranges.reverse()
i = 58370600
while True:
    n = i
    for ranges in all_ranges:
        n = map_with_range_reverse(n, ranges)
    if in_seed_range(n):
        print(i)
        break
    i += 1
