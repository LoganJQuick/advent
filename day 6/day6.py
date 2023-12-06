## Input ##
lines = open("day6.txt", 'r').readlines()

## Values ## 
times = [int(n) for n in lines[0].split(':')[1].split()]
distances = [int(n) for n in lines[1].split(':')[1].split()]
one_time = int(''.join(lines[0].split(':')[1].split()))
one_distance = int(''.join(lines[1].split(':')[1].split()))

## Functions ##
def ways_to_win(time, distance):
    lower = 0
    for i in range(time):
        if i*(time-i) > distance:
            lower = i - 1
            break
    return (time - 2*lower)-1

def get_part1_answer():
    result = 1
    for i in range(len(times)):
        result *= ways_to_win(times[i], distances[i])
    return result

## Answers ##
print("Part 1 Answer")
print(get_part1_answer())
print("Part 2 Answer")
print(ways_to_win(one_time, one_distance))