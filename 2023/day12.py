dp_mem = {}

def dp(line, dots, i, di, curr):
    key = (i, di, curr)
    if key in dp_mem:
        return dp_mem[key]
    if i==len(line):
        if di==len(dots) and curr==0:
            return 1
        elif di==len(dots)-1 and dots[di]==curr:
            return 1
        else:
            return 0
    result = 0
    for c in ['.', '#']:
        if line[i]==c or line[i]=='?':
            if c=='.' and curr==0:
                result += dp(line, dots, i+1, di, 0)
            elif c=='.' and curr>0 and di<len(dots) and dots[di]==curr:
                result += dp(line, dots, i+1, di+1, 0)
            elif c=='#':
                result += dp(line, dots, i+1, di, curr+1)
    dp_mem[key] = result
    return result
        
def num_perms(line):
    counts = [int(n) for n in line.split()[1].split(',')]
    return dp(line.split()[0], counts, 0, 0, 0)

def convert(line):
    code = '?'.join([line.split()[0] for i in range(5)])
    nums = ','.join([line.strip().split()[1] for i in range(5)])
    return " ".join([code, nums])

def get_answer(lines, part2=False):
    total = 0
    for line in lines:
        line = line if not part2 else convert(line)
        dots,blocks = line.split()
        blocks = [int(x) for x in blocks.split(',')]
        dp_mem.clear()
        result = dp(dots, blocks, 0, 0, 0)
        
        total += result
        dp_mem.clear()
    return total

## Main ##  
if __name__ == "__main__":
    lines = open('inputs\day12.txt', 'r').readlines()
    print("Answer for Part 1")
    print(get_answer(lines))
    print("Answer for Part 2")
    print(get_answer(lines, True))