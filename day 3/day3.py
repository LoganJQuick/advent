## Input ##
lines = open("day3.txt", 'r').readlines()
lines = list(map(lambda x: x.strip(), lines))

symbols = "*"
dirs = [(n, m) for n in [1,0,-1] for m in [1,0,-1]]

def is_adjacent_to_symbol(i, j):
    for n, m in dirs:
        if 0 <= i+n < len(lines) and 0 <= j+m < len(lines[0]) and lines[i+n][j+m] in symbols:
            return True
    return False

def gear_position(i, j):
    for n, m in dirs:
        if 0 <= i+n < len(lines) and 0 <= j+m < len(lines[0]) and lines[i+n][j+m] in symbols:
            return (i+n,j+m)

def get_number_length(i, j):
    length = 0
    while j < len(lines[0]) and lines[i][j].isdigit():
        length += 1
        j += 1
    return length

def num_adjacent(i, j):
    length = get_number_length(i, j)
    for n in range(length):
        if is_adjacent_to_symbol(i, j+n):
            return True
    return False

def new_num_adjacent(i, j):
    length = get_number_length(i, j)
    for n in range(length):
        gear_pos = gear_position(i, j+n)
        if gear_pos:
            return gear_pos
    return False


gear_nums = {}
i, j = 0, 0
while i < len(lines):
    j = 0
    while j < len(lines[0]):
        if lines[i][j].isdigit() and new_num_adjacent(i, j):
            gear_pos = new_num_adjacent(i, j)
            length = get_number_length(i, j)
            if gear_pos not in gear_nums:
                gear_nums[gear_pos] = []
            gear_nums[gear_pos].append(int(lines[i][j:j+length]))
            j += length
            continue
        j += 1
    i += 1
            
total = 0
for gear_num in gear_nums:
    if len(gear_nums[gear_num]) == 2:
        total += gear_nums[gear_num][0]*gear_nums[gear_num][1]
print(total)




def has33(number_list):
    return any(number_list[i] == 3 and number_list[i + 1] == 3 for i in range(len(number_list) - 1))
        
def has33_v2(number_list):
    return 33 in "".join(number_list)

