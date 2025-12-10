def parse_patterns(lines):
    patterns = []
    empty = -1
    for i in range(len(lines)):
        if lines[i].strip() == "":
            patterns.append([lines[j].strip() for j in range(empty+1, i)])
            empty = i
    patterns.append([lines[j].strip() for j in range(empty+1, len(lines))])
    return patterns

def check_vert(i, pattern, diff_target):
    n = len(pattern[0])
    bottom, top = i, i+1
    diffs = 0
    while bottom >= 0 and top < n:
        for j in range(len(pattern)):
            if pattern[j][top] != pattern[j][bottom]:
                diffs += 1
                if diffs > diff_target:
                    return False
        bottom -= 1
        top += 1
    return True if diffs == diff_target else False

def scan_vert(pattern, diff_target):
    for i in range(len(pattern[0])-1):
        if check_vert(i, pattern, diff_target):
            return i
    return None

def check_hor(i, pattern, diff_target):
    n = len(pattern)
    bottom, top = i, i+1
    diffs = 0
    while bottom >= 0 and top < n:
        
        for j in range(len(pattern[0])):
            if pattern[top][j] != pattern[bottom][j]:
                diffs += 1
                if diffs > diff_target:
                    return False
        bottom -= 1
        top += 1
    return True if diffs == diff_target else False

def scan_hor(pattern, diff_target):
    for i in range(len(pattern)-1):
        if check_hor(i, pattern, diff_target):
            return i
    return None

def find_reflect_value(pattern, diff_target):
    vert = scan_vert(pattern, diff_target)
    if vert is not None:
        return vert + 1
    hor = scan_hor(pattern, diff_target)
    return 100*(hor+1)

def print_pattern(pattern):
    for line in pattern:
        print(line)

def get_answer(patterns, is_part2 = False):
    total = 0
    for pattern in patterns:
        result = find_reflect_value(pattern, 1 if is_part2 else 0)
        total += result
    return total

## Main ##  
if __name__ == "__main__":
    lines = open('inputs/day13.txt').readlines()
    patterns = parse_patterns(lines)
    print("Answer for Part 1:")
    print(get_answer(patterns))
    print("\nAnswer for Part 2")
    print(get_answer(patterns, True))