lines = open('inputs\day12.txt', 'r').readlines()


def check_valid(line):
    groups = [s for s in line.split()[0].split('.') if s != '']
    nums = [int(n) for n in line.split()[1].split(',')] 
    if len(groups) != len(nums):
        return False
    
    for i in range(len(groups)):
        if len(groups[i]) != nums[i]:
            return False
    return True

def dp(dots: int, hashes: int, i: int, line):
    if dots == hashes == 0:
        return 1 if check_valid(line) else 0
    if line[i] != '?':
        return dp(dots, hashes, i+1, line)
    result = 0
    if dots>0:
        dot_line = line[:i] + '.' + line[i+1:]
        result += dp(dots-1, hashes, i+1, dot_line)
    if hashes>0:
        hash_line = line[:i] + '#' + line[i+1:]
        result += dp(dots, hashes-1, i+1, hash_line)
    return result

def num_perms(line):
    counts = [int(n) for n in line.split()[1].split(',')]
    hashes = sum(counts) - len([c for c in line if c=='#'])
    dots = len(line.split()[0]) - sum(counts) - len([c for c in line if c=='.'])
    return dp(dots, hashes, 0, line)

def convert(line):
    code = '?'.join([line.split()[0] for i in range(5)])
    nums = ','.join([line.strip().split()[1] for i in range(5)])
    return " ".join([code, nums])

total = 0
for line in lines:
    total += num_perms(line)
print(total)

print(num_perms(convert(lines[1])))