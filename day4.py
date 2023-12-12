## Input ##
import re
lines = open("inputs/day4.txt", 'r').readlines()

def get_nums(line):
    # Using Borja's regex
    match = re.compile(r"Card\s+[0-9]+: (?P<correct_nums>[0-9 ]+) \| (?P<guess_nums>[0-9 ]+)").match(line)
    correct = [int(n) for n in match.group("correct_nums").split()]
    guesses = [int(n) for n in match.group("guess_nums").split()]
    return (correct, guesses)

def num_correct(line):
    guesses, correct = get_nums(line)
    return len(set(guesses) & set(correct))

def get_part1_answer():
    result = 0
    for line in lines:
        correct_guesses = num_correct(line)
        points = 2**(correct_guesses-1)
        result += points if points >= 1 else 0
    return result

def get_part2_answer():
    scratchcards_counts = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        correct_guesses = num_correct(line)
        for j in range(1,correct_guesses+1):
            if i+j < len(scratchcards_counts):
                scratchcards_counts[i+j] += scratchcards_counts[i]
    return sum(scratchcards_counts)

## Answers ##
print("Answer for Part 1")
print(get_part1_answer())
print("Answer for Part 2")
print(get_part2_answer())