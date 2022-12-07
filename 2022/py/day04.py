import re


def part1(data):
    total = 0
    for line in data:
        A, B, C, D = map(int, re.findall(r"\d+", line))
        if A >= C and B <= D:
            total += 1
        elif A <= C and B >= D:
            total += 1
    return total


def part2(data):
    total = 0
    for line in data:
        A, B, C, D = map(int, re.findall(r"\d+", line))
        if D < A or B < C:
            # no overlap
            continue
        total += 1
    return total


data = open("inputs/day04.txt").read().strip().split("\n")
print(part1(data))
print(part2(data))
