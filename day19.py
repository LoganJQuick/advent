from collections import deque
class Part:
    xmas: dict[str, int]

    def __init__(self, str):
        self.xmas = {}
        str = str[1:-1]
        comps = str.split(',')
        for comp in comps:
            label, value = comp.split('=')
            value = int(value)
            self.xmas[label] = value

    def sum(self):
        return sum([val for val in self.xmas.values()])
    
    def __str__(self):
        result = ""
        for key in self.xmas.keys():
            result += f"{key}: {self.xmas[key]}, "
        return result

    def eval_rule(self, rule: str):
        if rule == 'A' or rule == 'R':
            return rule
        if '<' not in rule and '>' not in rule:
            return rule
        label = rule[0]
        test = rule[1]
        value = int(rule[2:].split(':')[0])
        dest = rule.split(':')[1]
        xmas_val = self.xmas[label]
        passed = xmas_val > value if test == '>' else xmas_val < value
        return dest if passed else None

def parse_input(lines):
    rule_dict = {}
    part_list = []
    i = 0
    line = lines[i]
    while line != "":
        i += 1
        line = lines[i]
    rules = lines[:i]
    parts = lines[i+1:]
    for rule in rules:
        label = rule.split('{')[0]
        r = rule.split('{')[1].split('}')[0].split(',')
        rule_dict[label] = r
    part_list = [Part(part) for part in parts]
    return (rule_dict, part_list)

def eval_rules(rule_dict, part: Part):
    curr = rule_dict['in']
    i = 0
    while True:
        rule = curr[i]
        eval = part.eval_rule(rule)
        if eval is not None:
            if eval == 'A':
                return part.sum()
            elif eval == 'R':
                return 0
            else:
                curr = rule_dict[eval]
                i = 0
        else:
            i += 1

def intersect(i1, i2):
    l1, u1 = i1
    l2, u2 = i2
    l3 = max(l1,l2)
    u3 = min(u1, u2)
    return (l3, u3) if u3 >= l3 else None

def eval_rule_ranges(xmas_ranges, rule):
    if '<' not in rule and '>' not in rule:
        return (rule, xmas_ranges, None)
    label = rule[0]
    test = rule[1]
    value = int(rule[2:].split(':')[0])
    dest = rule.split(':')[1]
    if test == '>':
        rule_pass_interval = (value+1, 4000)
        rule_fail_interval = (0, value)
    else:
        rule_pass_interval = (0, value-1)
        rule_fail_interval = (value, 4000)
    pass_interval = intersect(xmas_ranges[label], rule_pass_interval)
    fail_interval = intersect(xmas_ranges[label], rule_fail_interval)
    if pass_interval is None:
        xmas_pass_ranges = None
    else:
        xmas_pass_ranges = xmas_ranges.copy()
        xmas_pass_ranges[label] = pass_interval
    if fail_interval is None:
        xmas_fail_ranges = None
    else:
        xmas_fail_ranges = xmas_ranges.copy()
        xmas_fail_ranges[label] = fail_interval
    return (dest, xmas_pass_ranges, xmas_fail_ranges)

def eval_range_rules(rule_dict):
    q = deque([('in', 0, {'x': (1,4000), 'm': (1,4000), 'a': (1,4000), 's': (1,4000)})])
    result = 0
    while q:
        label, pos, ranges = q.popleft()
        dest, pass_ranges, fail_ranges = eval_rule_ranges(ranges, rule_dict[label][pos])
        if dest == 'A' and pass_ranges is not None:
            successes = 1
            for l1, u1 in pass_ranges.values():
                successes *= u1 - l1 + 1
            result += successes
        elif dest != 'R' and pass_ranges is not None:
            q.append((dest, 0, pass_ranges))
        if fail_ranges is not None:
            q.append((label, pos+1, fail_ranges))
    return result



def get_part1_answer(lines):
    rule_dict, part_list = parse_input(lines)
    result = 0
    for part in part_list:
        result += eval_rules(rule_dict, part)
    return result

def get_part2_answer(lines):
    rule_dict, _ = parse_input(lines)
    return eval_range_rules(rule_dict)

## Main ##  
if __name__ == "__main__":
    lines = [line.strip() for line in open('inputs/day19.txt').readlines()]
    print("Part 1 Answer")
    print(get_part1_answer(lines))
    print("Part 2 Answer")
    print(get_part2_answer(lines))
    
    
