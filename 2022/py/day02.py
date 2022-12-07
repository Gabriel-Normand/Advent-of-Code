moves = {'A': 'R', 'B': 'P', 'C': 'S',
         'X': 'R', 'Y': 'P', 'Z': 'S'}
# rock paper scissors win draw lose
value = {'R': 1, 'P': 2, 'S': 3,
         'W': 6, 'D': 3, 'L': 0}


def part1(matches):
    moveList = [[moves[move]for move in match.split()]for match in matches]
    total = 0
    for a, b in moveList:
        if a == b:
            total += value['D']
        elif a == "R":
            if b == "P":
                total += value['W']
            elif b == "S":
                total += value['L']
        elif a == "P":
            if b == "S":
                total += value['W']
            elif b == "R":
                total += value['L']
        elif a == "S":
            if b == "R":
                total += value['W']
            elif b == "P":
                total += value['L']
        total += value[b]
    return total


moves2 = {'A': 'R', 'B': 'P', 'C': 'S',
          'X': 'L', 'Y': 'D', 'Z': 'W'}


def part2(matches):
    moveList = [[moves2[move]for move in match.split()]for match in matches]
    total = 0
    for a, b in moveList:
        if a == "R":
            if b == "W":
                total += value['P']
            elif b == "D":
                total += value['R']
            elif b == "L":
                total += value['S']
        elif a == "P":
            if b == "W":
                total += value['S']
            elif b == "D":
                total += value['P']
            elif b == "L":
                total += value['R']
        elif a == "S":
            if b == "W":
                total += value['R']
            elif b == "D":
                total += value['S']
            elif b == "L":
                total += value['P']
        total += value[b]
    return total


data = open("inputs/day02.txt").read().strip().split("\n")
print(part1(data))
print(part2(data))
