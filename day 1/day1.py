## Global Vars ##
lines = open('day1.txt', 'r').readlines()
nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine":  9}

## Functions ##
def not_none(n):
    return n is not None

def filter_none(lst):
    return list(filter(not_none, lst))

def try_digit(c):
    try:
        return int(c)
    except:
        return None

def try_word(string, position):
    words = filter_none([nums.get(string[position:position+length]) for length in [3,4,5]])
    return words[0] if len(words) > 0 else None

def digit_checker(string, position):
    return try_digit(string[position])

def digit_and_word_checker(string, position):
    dig = try_digit(string[position])
    word = try_word(string, position)
    return dig if dig else word if word else None

def get_answer(numChecker):
    result = 0
    for line in lines:
        hits = filter_none([numChecker(line, i) for i in range(len(line))])
        result += hits[0]*10 + hits[-1]
    return result

## Results ##
print("Answer for Part 1:")
print(get_answer(digit_checker))
print("Answer for Part 2:")
print(get_answer(digit_and_word_checker))