class Lens:
    label: str
    focal_length: int
    
    def __init__(self, label: str, focal_length: int):
        self.label = label
        self.focal_length = focal_length
        
    def __str__(self):
        return self.label + f": {self.focal_length}"
    
class Box:
    lenss: list[Lens]
    lens_set: set[str]
    box_num: int
    
    def get_lens_values(self):
        total = 0
        for i, lens in enumerate(self.lenss):
            fp = focusing_power(self.box_num, i, lens.focal_length)
            total += fp
        return total
    
    def add_lens(self, lens: Lens):
        label = lens.label
        if label in self.lens_set:
            pos = [i for i in range(len(self.lenss)) if self.lenss[i].label == label][0]
            self.lenss[pos] = lens
        else:
            self.lenss.append(lens)
            self.lens_set.add(label)
    
    def remove(self, label: str):
        if label in self.lens_set:
            pos = [i for i in range(len(self.lenss)) if self.lenss[i].label == label][0]
            self.lens_set.remove(self.lenss[pos].label)
            self.lenss.pop(pos)
    
    def __init__(self, num: int):
        self.lenss = []
        self.lens_set = set()
        self.box_num = num

def HASH(input_string: str):
    result = 0
    for c in input_string:
        result = ((result + ord(c))*17) % 256
    return result

def focusing_power(box_num: int, slot_num: int, focal_length):
    return (box_num+1)*(slot_num+1)*focal_length

def get_lens(lines: str):
    return lines[0].split(',')

def get_part1_answer(lines):
    result = 0
    for code in get_lens(lines):
        result += HASH(code)
    return result
    
def get_part2_answer(lines):
    lens = get_lens(lines)
    boxes = [Box(i) for i in range(256)]
        
    
    for len in lens:
        if '=' in len:
            label = len.split('=')[0]
            focal_length = int(len.split('=')[1])
            new_len = Lens(label, focal_length)
            boxes[HASH(label)].add_lens(new_len)
        else:
            label = len.split('-')[0]
            boxes[HASH(label)].remove(label)
    result = 0
    for box in boxes:
        val = box.get_lens_values()
        result += val
    return result
            



## Main ##  
if __name__ == "__main__":
    lines = open('inputs/day15.txt').readlines()
    print(get_part1_answer(lines))
    print(get_part2_answer(lines))