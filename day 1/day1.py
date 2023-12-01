# Input
lines = open('day1.txt', 'r').readlines()

# Part 1
sum1 = 0
for line in lines:
    i = 0
    while not line[i].isdigit():
        i += 1
    tens = int(line[i])*10
    i = len(line) - 1
    while not line[i].isdigit():
        i -= 1
    ones = int(line[i])
    sum1 += tens + ones

print("Answer for Part 1:")
print(sum1)
    

# Part 2

nums = {
    "one":   1,
    "two":   2,
    "three": 3,
    "four":  4,
    "five":  5,
    "six":   6,
    "seven": 7,
    "eight": 8,
    "nine":  9,
}

def CheckForNum(string, pos):
    if string[pos].isdigit():
        return (True, int(string[pos]))
    for length in [3,4,5]:
        if string[pos:pos+length] in nums:
            return (True, nums[string[pos:pos+length]])
    return (False, 0)

sum2 = 0
for line in lines:
    i = 0
    tens = 0
    while True:
        hit, num = CheckForNum(line, i)
        if hit:
            tens = num*10
            break
        i += 1
    i = len(line) - 1
    ones = 0
    while True:
        hit, num = CheckForNum(line, i)
        if hit:
            ones = num
            break
        i -= 1
    sum2 += tens + ones
    
print("Answer for Part 2:")
print(sum2)