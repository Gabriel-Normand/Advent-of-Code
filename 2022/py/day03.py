value = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part1(data):
    total = 0
    for line in data:
        half = len(line) // 2
        first, second = line[:half], line[half:]
        # ({*first}&{*second}) gets the intersection of first and second
        total += value.index(({*first} & {*second}).pop())
    return total


def part2(data):
    total = 0
    for i in range(0, len(data), 3):
        first, second, third = data[i], data[i+1], data[i+2]
        total += value.index(({*first} & {*second} & {*third}).pop())
    return total


data = open("inputs/day03.txt").read().strip().split("\n")
print(part1(data))
print(part2(data))
