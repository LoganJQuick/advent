## Functions ##
def all_zeros(nums):
    return all([x == 0 for x in nums])

def parse_lines(lines):
    return [[int(num) for num in line.strip().split()] for line in lines]

def get_difference_sequence(sequence):
    return [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]

def difference_generator(curr):
    while ((yield curr) is None) and not all_zeros(curr): curr = get_difference_sequence(curr)

def extrapolate_line(line):
    seqs = list(difference_generator([x for x in line]))
    for i in range(1,len(seqs)):
        seqs[len(seqs)-i-1][-1] = seqs[len(seqs)-i-1][-1] + seqs[len(seqs)-i][-1]
    return seqs[0][-1]

def get_answer(lines):
    return sum([extrapolate_line(line) for line in lines])

def reverse_all_lines(lines):
    return [line[::-1] for line in lines]
      
## Main ##  
if __name__ == "__main__":
    lines = open('day 9/day9.txt').readlines()
    parsed_lines = parse_lines(lines)
    print("Answer for Part 1")
    print(get_answer(parsed_lines))
    reversed_lines = reverse_all_lines(parsed_lines)
    print("\nAnswer for Part 2")
    print(get_answer(reversed_lines))