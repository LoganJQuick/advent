from collections import Counter
## Input ##
lines = open("day7.txt", 'r').readlines()

card_types_1 = {"A": 13, "K": 12, "Q": 11, "J": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2, "2": 1}
card_types_2 = {"A": 13, "K": 12, "Q": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1}

def hand_type_1(hand):
    counts = Counter(hand)
    three = False
    twos = 0
    for card in counts.keys():
        if counts[card] == 5:
            return 7
        if counts[card] == 4:
            return 6
        if counts[card] == 3:
            three = True
        elif counts[card] == 2:
            twos += 1
    if three and twos:
        return 5
    if three:
        return 4
    if twos == 2:
        return 3
    if twos:
        return 2
    return 1

def hand_type_2(hand):
    counts = Counter(hand)
    jokers = 0
    if 'J' in counts:
        jokers = counts['J']
    three = False
    twos = 0
    for card in counts.keys():
        if counts[card] == 5:
            return 7
        if counts[card] == 4:
            return 7 if jokers else 6
        if counts[card] == 3:
            three = True
        elif counts[card] == 2:
            twos += 1
    if three and twos:
        return 7 if jokers else 5
    if three:
        return 6 if jokers else 4
    if twos == 2:
        return 6 if jokers == 2 else 5 if jokers else 3
    if twos:
        return 4 if jokers else 2
    return 2 if jokers else 1

def hand_value(hand, part1=True):
    result = hand_type_1(hand) if part1 else hand_type_2(hand)
    for c in hand:
        result *= 100
        result += card_types_1[c] if part1 else card_types_2[c]
    return result

def hand_sorter(hand_and_wager):
    hand, _ = hand_and_wager
    return hand_value(hand)

def hand_sorter_2(hand_and_wager):
    hand, _ = hand_and_wager
    return hand_value(hand, False)


def get_answer(key):
    hands = []
    for line in lines:
        hand = line.split()[0]
        wager = int(line.split()[1])
        hands.append((hand, wager))
    hands.sort(key=key)

    total = 0
    for i, hw in enumerate(hands):
        _, wager = hw
        total += (i+1)*wager
    return total

print(get_answer(hand_sorter))
print(get_answer(hand_sorter_2))

print(hand_value('JJJ2A', False))