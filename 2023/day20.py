from collections import deque
from math import gcd
class FlipFlop:
    state: bool
    outputs: list[str]

    def __init__(self, outputs: list[str]):
        self.outputs = outputs
        self.state = False

    def handle_pulse(self, pulse:bool, sender:str =None):
        if pulse:
            return (False, [])
        
        pulse = not self.state
        self.state = not self.state
        return (pulse, self.outputs)

    def __str__(self):
        return ' '.join(self.outputs)

class Conjunction:
    outputs: list[str]
    memory: dict[str, bool]

    def __init__(self, outputs: list[str]):
        self.outputs = outputs
        
    def init_memory(self, inputs: list[str]):
        self.memory = {}
        for input in inputs:
            self.memory[input] = False

    def handle_pulse(self, pulse:bool, sender:str):
        self.memory[sender] = pulse
        pulse = not all(self.memory[key] for key in self.memory.keys())
        return (pulse, self.outputs)
    
    def __str__(self):
        return ' '.join(self.outputs)

class Broadcaster:
    outputs: list[str]

    def __init__(self, outputs):
        self.outputs = outputs

    def handle_pulse(self, pulse: bool, sender: str):
        return (pulse, self.outputs)
    
    def __str__(self):
        return ' '.join(self.outputs)

def simulate_pulses(module_dict: dict, target):
    start = [(False, 'broadcaster', None)]
    q = deque(start)
    target_send_pulse = False
    while q:
        pulse, curr, sender = q.popleft()
        if pulse and sender == target:
            target_send_pulse =  True
        if curr not in module_dict:
            continue
        new_pulse, outputs = module_dict[curr].handle_pulse(pulse, sender)
        for output in outputs:
            q.append((new_pulse, output, curr))
    return target_send_pulse

def process_lines(lines):
    module_dict = {}
    inputs = {}
    conjunctions = []
    for line in lines:
        outputs = line.split('-> ')[1].split(', ')
        name = 'broadcaster' if line[0] == 'b' else line[1:].split()[0]
        for output in outputs:
            if output not in inputs:
                inputs[output] = []
            inputs[output].append(name)
        if line[0] == '%':
            flipflop = FlipFlop(outputs)
            module_dict[name] = flipflop
        elif line[0] == '&':
            conjunction = Conjunction(outputs)
            module_dict[name] = conjunction
            conjunctions.append(name)
        elif line[0] == 'b':
            broadcaster = Broadcaster(outputs)
            module_dict['broadcaster'] = broadcaster
    for conjunction in conjunctions:
        module_dict[conjunction].init_memory(inputs[conjunction])
    return module_dict

def print_modules(modules):
    for module in modules.keys():
        print(f'{module} | {modules[module]}')

def get_part1_answer(lines):
    module_dict = process_lines(lines)
    lcm = 1
    for target in ['tt', 'tt', 'tt']:
        count = 0
        while True:
            stop = simulate_pulses(module_dict, target)
            count += 1
            if stop:
                break
        print(count)
    return lcm

## Main ##  
if __name__ == "__main__":
    lines = [line.strip() for line in open('inputs/day20.txt').readlines()]
    # print('Part 1 Answer')
    get_part1_answer(lines)