## Input ##
lines = open("day4.txt", 'r').readlines()
point_total = 0
scratchcards_counts = [1 for _ in range(len(lines))]

def get_correct_nums(line):
    return list(map(lambda x: int(x), line.split(':')[1].split("|")[0].split()))

def get_guess_nums(line):
    return list(map(lambda x: int(x.strip()), line.split("|")[1].split()))

def num_correct(guesses, correct):
    return len(list(filter(lambda x: x in correct, guesses)))

# part 1

for line in lines:
    correct = get_correct_nums(line)
    guesses = get_guess_nums(line)
    points = .5
    correct_guesses = num_correct(guesses, correct)
    points = int(.5*(2**correct_guesses))
    point_total += points if points >= 1 else 0

print(point_total)

# part 2

for i, line in enumerate(lines):
    correct = get_correct_nums(line)
    guesses = get_guess_nums(line)
    correct_guesses = num_correct(guesses, correct)
    for j in range(1,correct_guesses+1):
        if i+j < len(scratchcards_counts):
            scratchcards_counts[i+j] += scratchcards_counts[i]
    
print(sum(scratchcards_counts))