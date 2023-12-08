import re
from math import gcd
## Input ##
lines = open('day8.txt').readlines()

## Class ##
class Node:
    tag = None
    left = None
    right = None
    def __init__(self, tag: str):
        self.tag = tag

## Helper Functions ##
# builds nodes from input
def build_nodes():
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
def num_steps(node, target_test):
    dirs = lines[0].strip()
    i = 0
    count = 0
    curr = node
    while not target_test(curr):
        if dirs[i] == 'R':
            curr = curr.right
        else:
            curr = curr.left
        count += 1
        i = (i+1) % len(dirs)
    return count

## Get Answers ##
def get_part1_answer():
    nodes = build_nodes()
    node = nodes['AAA']
    return num_steps(node, part1_test)

def get_part2_answer():
    nodes = build_nodes()
    start_nodes = [nodes[node] for node in nodes if node[-1] == 'A']
    counts = []
    for node in start_nodes:
        counts.append(num_steps(node, part2_test))
    lcm = 1
    for n in counts:
        lcm = lcm*n//gcd(lcm, n)
    return lcm

print(get_part1_answer())
print(get_part2_answer())