import re
from math import gcd

## Class ##
class Node:
    tag = None
    left = None
    right = None
    def __init__(self, tag: str):
        self.tag = tag

## Helper Functions ##
# builds nodes from input
def build_nodes(lines):
    nodes = {}
    neighbors = {}
    for line in lines[2:]:
        match = re.compile(r"(?P<tag>[1-9A-Z]+) = \((?P<left>[1-9A-Z]+),\s(?P<right>[1-9A-Z]+)\)").match(line)
        node = Node(match['tag'])
        nodes[match['tag']] = node
        neighbors[match['tag']] = [match['left'], match['right']]
    for node in nodes:
        left, right = neighbors[node]
        nodes[node].left = nodes[left]
        nodes[node].right = nodes[right]
    return nodes

# determines if all nodes end with 'Z'
def all_Zs(nodes):
    for node in nodes:
        if node.tag[-1] != 'Z':
            return False
    return True

# checks if at destination node for part 1
def part1_test(node):
    return node.tag == 'ZZZ'

# checks if at destination node for part 2
def part2_test(node):
    return node.tag[-1] == 'Z'

# finds number of steps to destination node using relevant check for end-node-edness
def num_steps(node, target_test, loops=1):
    dirs = lines[0].strip()
    i = 0
    count = 0
    curr = node
    loops_made = 0
    while not target_test(curr) or loops_made < loops:
        if dirs[i] == 'R':
            curr = curr.right
        else:
            curr = curr.left
        count += 1
        i = (i+1) % len(dirs)
        if target_test(curr):
            loops_made += 1
    return count

## Get Answers ##
def get_part1_answer(lines):
    nodes = build_nodes(lines)
    node = nodes['AAA']
    return num_steps(node, part1_test)

def get_part2_answer(lines):
    nodes = build_nodes(lines)
    start_nodes = [nodes[node] for node in nodes if node[-1] == 'A']
    counts = []
    for node in start_nodes:
        counts.append(num_steps(node, part2_test))
    lcm = 1
    for n in counts:
        lcm = lcm*n//gcd(lcm, n)
    return lcm


## Main ##  
if __name__ == "__main__":
    lines = open('inputs/day8.txt').readlines()
    print("Answer for Part 1")
    print(get_part1_answer(lines))
    print("\nAnswer for Part 2")
    print(get_part2_answer(lines))