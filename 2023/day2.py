## Functions
def valid_num(col, num):
    return num <= colors[col]

def valid_game(game):
    hands = game.split(': ')[1].split('; ')
    for hand in hands:
        single_colors = hand.split(', ')
        for single_color in single_colors:
            col, num = single_color.split()[1], int(single_color.split()[0])
            if not valid_num(col, num):
                return False
    return True

def game_powers(game):
    cols = {'red': 0, 'green': 0, 'blue': 0}
    hands = game.split(': ')[1].split('; ')
    for hand in hands:
        single_colors = hand.split(', ')
        for single_color in single_colors:
            col, num = single_color.split()[1], int(single_color.split()[0])
            cols[col] = max(cols[col], num)
    return cols['red']*cols['blue']*cols['green']

def get_answers():
    game_total = 0
    game_reqs = 0
    for line in lines:
        game_num = int(line.split(': ')[0].split()[1])
        if valid_game(line):
            game_total += game_num
        game_reqs += game_powers(line)
    return game_total, game_reqs

## Main ##  
if __name__ == "__main__":
    lines = open("inputs/day2.txt", 'r').readlines()
    colors = {'red': 12, 'green': 13, 'blue': 14}
    part1_answer, part2_answer = get_answers()
    print("Part 1 Answer")
    print(part1_answer)
    print("Part 2 Answer")
    print(part2_answer) 