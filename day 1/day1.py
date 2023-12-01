# Input
lines = open('day1.txt', 'r').readlines()

# Functions
def getAnswer(lines, numChecker):
    result = 0
    for line in lines:
        tens, ones = 0, 0
        for i in range(len(line)):
            hit, num = numChecker(line, i)
            if hit:
                tens += 0 if tens != 0 else num*10
                ones = num
        result += tens + ones
    return result

def numChecker1(string, pos):
    return (True, int(string[pos])) if string[pos].isdigit() else (False, 0)

nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine":  9}
def numChecker2(string, pos):
    if string[pos].isdigit():
        return (True, int(string[pos]))
    for length in [3,4,5]:
        if string[pos:pos+length] in nums:
            return (True, nums[string[pos:pos+length]])
    return (False, 0)

# Results
print("Answer for Part 1:")
print(getAnswer(lines, numChecker1))
print("Answer for Part 2:")
print(getAnswer(lines, numChecker2))